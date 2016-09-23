---
title: Golang and Hive/Impala – Thrift
author: koblas
layout: post
date: 2015-05-17T21:57:54+00:00
url: /p/golang-and-hiveimpala-thrift/518
pvc_views:
  - 1459
dsq_thread_id:
  - 3772318812
categories:
  - Development
tags:
  - golang
  - hive
  - impala

---
This started out as a quick project to see about taking a component of our service and migrating it from Python to Go. We&#8217;ve been talking about migrating services from the semi-monolithic version to more loosely coupled &#8211; the general idea is to move to Thrift oriented services. We have a core component of our system that uses Impala as a key backend, it&#8217;s a very stable service that could be logically broken out.

As an exercise for the weekend, started looking at golang and the ability to migrate it. While I can&#8217;t share the full code / details. As I was putting this together the resources for Go and Thrift are weak at best.

The first thing is that you need to get your &#8220;thrift build&#8221; aka Makefile right

```bash
thrift:
    thrift -r -gen go:package_prefix=github.com/koblas/test/services/ interfaces/ImpalaService.thrift
    rm -rf ./services
    mv gen-go services
```

Turns out that **package_prefix **is a big deal, since the thrift build is going to build a collection (not-just one) interface we need a way to make sure that they&#8217;re all available and name spaced.

Also &#8211; worth noting that [HiveThing][1] is a useful reference &#8211; though useses Hive Server 2 not beeswax.

The example code I ended up writing is here &#8211; hopefully this helps somebody in the future, figure things out just a bit faster.

```go
package main

import (
    "git.apache.org/thrift.git/lib/go/thrift"
    impala "github.com/Tubular/audience-also-watches/services/ImpalaService"
    "github.com/Tubular/audience-also-watches/services/beeswax"
    "fmt"
    "log"
    "time"
)

func main() {
    addr := "impala-cluster"
    port := 21000

    log.Println("Starting")

    socket, err := thrift.NewTSocket(fmt.Sprintf("%s:%d", addr, port))

    if err != nil {
        log.Fatal("Error opening socket:", err)

        return
    }

    log.Println("Factory Land")

    transportFactory := thrift.NewTBufferedTransportFactory(24*1024*1024)
    protocolFactory := thrift.NewTBinaryProtocolFactoryDefault()

    transport := transportFactory.GetTransport(socket)
    defer transport.Close()

    log.Println("Doing Open")

    if err := transport.Open(); err != nil {
        log.Fatal("Unable to open transport", err)

        return
    }

    log.Println("Getting Client")

    client := impala.NewImpalaServiceClientFactory(transport, protocolFactory)

    if client == nil {
        log.Fatal("Unable to estalbish client")
        return
    }

    log.Println("Before ping")
    client.PingImpalaService()
    log.Println("DONE")

    //
    log.Println("Building Query")

    query := beeswax.Query{}

    query.Query = "SELECT * FROM engagements LIMIT 10000"
    query.Configuration = []string{}

    handle, err := client.Query(&query)
    log.Println("Query sent")

    if err != nil {
        log.Fatal("QUERY Failed")
        return
    }

    for true {
        time.Sleep(100 * time.Millisecond)

        state, err := client.GetState(handle)
        if err != nil {
            log.Println("GetState Error", err)
            break
        }

        log.Println("State = ", state)

        if state == beeswax.QueryState_FINISHED {
            log.Println("Got finish state of", state)
            break
        }
        if state == beeswax.QueryState_EXCEPTION {
            log.Println("Exception", state)
            return
        }
    }

    log.Println("Fetching results")

    // first := true
    total := 0
    startTime := time.Now()
    for true {
        // log.Println("Getting Row")
        result, err := client.Fetch(handle, false, 1000000)

        if err != nil {
            log.Fatal("Error in fetch", err)
            return
        }

        /*
        if first {
            first = false

            fmt.Println(result.Columns)
        }
        */

        // log.Println("Got count=", len(result.Data))

        total = total + len(result.Data)

        /*
        for _, row := range(result.Data) {
            fmt.Println(row)
        }
        */

        if ! result.HasMore {
            break
        }
    }
    log.Printf("Fetch %d rows(s) in %.2fs", total, time.Duration(time.Since(startTime)).Seconds())

    log.Println("All Done")
}
```

 [1]: https://github.com/derekgr/hivething
