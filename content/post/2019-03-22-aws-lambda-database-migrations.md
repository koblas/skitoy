---
title: AWS Lambda Database Migrations
author: koblas
layout: post
date: 2019-03-22T13:53:52+00:00
url: /p/aws-lambda-database-migrations/644
categories:
  - technical

---

# AWS Lambda Database Migrations

Software development and deployment is very much like an adventure game.  Where you're faced with puzzles that might take you a day to solve, by picking up pieces and stumbling around in a dark room.  Once you've figured it out, you could go back and solve the puzzle in 10 minutes.

One of the manage challenges with serverless based architectures is that when you introduce a relational database sitting in a VPC you have more moving pieces.  With every SQL DB you have the challenge of schema migrations and how to apply them.  Traditionally this is done by having a machine or VPN tunnel somewhere that can talk to the database and apply migrations from the command line.  With serverless you just have a lonely DB sitting in a VPC which is ideally isolated.

## User Story

Build a lambda function that will apply database migrations when migrations are uploaded to an S3 bucket.  Bonus points; all of this needs to be configured and built with terraform.

## Flyway vs Migrate (Java vs Go)

When looking and standalone database migration tools, there are two really good choices [flyway](https://flywaydb.org/) or [migrate](https://github.com/golang-migrate/migrate).  From my experience there are a few key differences between these projects:

* migrate - supports "network" migration directories (e.g. S3)
* flyway - better rollback support (migrations are transactions)
* flyway - better schema version tracking
* migrate - golang
* flyway - java

I currently use flyway on a "daily" bases for my day-job, I've used migrate for some personal projects.  The key feature that is required for this project is the ability to read S3 -- otherwise the first list of my lambda is going to be copy the S3 bucket locally.

## Best Laid Plan

Since it's easy to bundle an executable and a driver in a zip file to make for a quick lambda function.  Whipped together this quick driver which calls `migrate`.  Was all ready to go, cool this is going to be easy.

```
import os

def lambda_handler(event, context):
    for r in event.get("Records",[]):
        key = r.get("s3", {}).get("object", "").get("key", "")

        table = key.strip("/").split("/")[0]

        print( "Invoking migrations on table={} objectkey={}".format(table, key))

        os.system("./migrate -source s3://%s/%s/ -database %s up" % (os.environ["S3BUCKET"], table, os.environ["DATABASE"].replace("DB_NAME", table)))
```

### Key feature

The original DB that AWS creates is not going to have a specific database, so while your regular migrations (e.g. `create table users (...`) will be on your own database, you need to have some key migrations on the root database itself, in this case `postgres` where you do a `create database some_db;`.  Quick design point is to put the database name in the first component of the migration path, so you can now migrate to any database on the instance.

Something like:

```
 BUCKET
   postgres
     1_create_projectdb.up.sql
   projectdb
     1_create_user_table.up.sql
     2_create_widget_table.up.sql
```

_Note: usually `1`, `2` are `YYYYMMDDHHMM` timestamps._

### Problem

Turns out that `GOOS=linux GOARCH=amd64 go build -o migrate github.com/golang-migrate/migrate` doesn't build an executable, but rather an archive.  Once I got all of the terraform configuration setup, got errors about 'unable to run' from the `os.system(` call.

This of course turned out to be a one hour hole to dig into, trying to figure out how.  Looks like it's a limitation in `golang` that you can't cross build executables from remote sources.

## Go Lambda Version 1

After figuring out I had spent too much time trying to make the originaly python driver calling exectuable.  Started to see if I could just write a lambda function based on migrate.

The first version was just going to wrap the cli method and call with a whacked up environment.  Didn't really want to get into too much of the internal of migrate.  **Key Learning** golang has a `internal` as a magic path in it's components, so if you write a package with `internal` nobody can import from that path.  As it turns out my script wanted to get some imports from there :(

## Go Lambda Version 2

After being really frustrated, looked and found that migrate is actually built to be a library.  Where they give this quick example:

```golang
import (
    "github.com/golang-migrate/migrate/v4"
    _ "github.com/golang-migrate/migrate/v4/database/postgres"
    _ "github.com/golang-migrate/migrate/v4/source/github"
)

func main() {
    m, err := migrate.New(
        "github://mattes:personal-access-token@mattes/migrate_test",
        "postgres://localhost:5432/database?sslmode=enable")
    m.Steps(2)
}
```

With that example in hand and a little bit of elbow grease, quickly converted it into a full fledged AWS Lambda function.  Taking into account some of the code from the original python version.

```golang
package main

import (
	"context"
	"fmt"
	"os"
	"strings"

	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
	"github.com/golang-migrate/migrate/v4"
	_ "github.com/golang-migrate/migrate/v4/database/postgres"
	_ "github.com/golang-migrate/migrate/v4/source/aws_s3"
)

func handler(ctx context.Context, s3Event events.S3Event) {
	fmt.Println("Lambda handler called")

	for _, record := range s3Event.Records {
		s3 := record.S3

		fmt.Printf("START [%s - %s] Bucket = %s, Key = %s \n", record.EventSource, record.EventTime, s3.Bucket.Name, s3.Object.Key)

		parts := strings.Split(strings.Trim(s3.Object.Key, "/"), "/")
		if len(parts) == 0 {
			fmt.Printf("Error - key has no leading part - %s\n", s3.Object.Key)
			continue
		}

		table := parts[0]
		fmt.Printf("Invoking migrations on table=%s objectkey=%s\n", table, s3.Object.Key)

		m, err := migrate.New(
			fmt.Sprintf("s3://%s/%s", s3.Bucket.Name, table),
			strings.ReplaceAll(os.Getenv("DATABASE"), "DB_NAME", table),
		)

		if err != nil {
			fmt.Println(err)
			continue
		}

		fmt.Printf("Starting UP migrations\n")

		if err := m.Up(); err != nil {
			fmt.Println(err)
		}

		fmt.Printf("END [%s - %s] Bucket = %s, Key = %s \n", record.EventSource, record.EventTime, s3.Bucket.Name, s3.Object.Key)
	}

	fmt.Println("Completed migrations")
}

func main() {
	lambda.Start(handler)
}
```

## Still Doesn't Work

Double check the obvious:

* AWS Policies to create EIP
* AWS Policies to access S3 bucket
* AWS Policies to run on S3 events

The short list of things that caused problems at the end:

**Lambda function times out at 3 seconds:**  Fix: up the timeout to 60 seconds and set the DB connection timeout to 20 seconds.

**Lambda function isn't in VPC** Fix: Add the VPC subnet and security group access

### The hard bug

The hardest final bug to find and fix turned out that since the VPC only contained the RDS instance, there was no route from the VPC to S3.  The only diagnostic was that the lambda function would timeout at 60 seconds (the new timeout) with no diagnostics.

## Summary (aka TLDR)

What you need to do to create a lambda function that does database migrations inclues the following steps:

* Create VPC
* Create RDS in VPC
* Create S3 bucket to host migrations
* Lambda: Create Role for Lambda Function
* Lambda: Create Policy that allows `s3:ListBucket` and `s3:*Object` access
* Lambda: Create Policy that allows ec2:EIP Access
* Lambda: Create Policy that allows for writing CloudWatch logs
* Lambda: Create the lambda function
* SNS: Create SNS event topic
* Lambda: Create Permission to execute from S3 Event
* Subscribe Lambda to SNS topic for S3 events
* VPC: Create route from VPC to S3 bucket

Sorry, I don't yet have a GitHub with everything as a package.



