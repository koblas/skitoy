---
title: React and GraphQL, plus GoLang
author: koblas
type: post
date: 2016-10-11T16:29:24+00:00
url: /p/graphql-date-time/630
categories:
  - Development
tags:
  - react
  - graphql
  - golang

---

# GraphQL DateTime Scalar Value

Strings are not your friend when it comes to date time types. The problem is that with the naive definition you'll get the wrong value. For starters the naive definition looks like this:

```
// GraphQL
//     type Object {
//         updated_at  String
//     }
//

// The Go structure definition
struct {
	// ....
	UpdatedAt time.Time `json:"updated_at" sql:"NOT NULL"`
}

// GoLang GraphQL definition
oType := graphql.NewObject(
    graphql.ObjectConfig{
        Name: "Object",
        Fields: graphql.FieldsThunk(func () graphql.Fields {
            return graphql.Fields{
			    //  ...
                "updated_at": &graphql.Field{
                    Type: graphql.String,
                },
				//  ...
```

You've always serialized out time.Time as String with JSON and it's worked great. The Safari throws an Exception on parsing a date and you're perplexed, after all it worked in Chrome. You beging to debug and discover that:

* JSON Serialize a time.Time = `2016-11-10T11:34:33.91982067-05:00`
* Go GraphQL Serialize a time.Time = `2016-11-10 11:34:33.91982067 -0500 EST`

Clearly a big difference, but why? As it turns out GraphQL does a "%v" on all objects that aren't strings. While the JSON encoder knows that it should make a ISO time print. Not only that but Chrome is more forgiving about the parsing of Date() than other browsers.

## Give me the code

You should define a DateTime data type to support the output of ISO3339 (a stricter version of ISO8601). I will admit that I got the idea from reading the GitHub GraphQL definitions. 

Here's the code to define a DateTime for [GoLang's GraphQL](https://github.com/graphql-go/graphql) library. I do wonder a bit why DateTime isn't part of the GraphQL definition, since having a standard would be exceptionally useful.

```
package handlers

import (
    "time"
    "fmt"
    "github.com/graphql-go/graphql"
    "github.com/graphql-go/graphql/language/ast"
)

var dateTimeType = graphql.NewScalar(graphql.ScalarConfig{
        Name: "DateTime",
        Description: "DateTime is a DateTime in ISO 8601 format",
        Serialize: func(value interface{}) interface{} {
            switch value := value.(type) {
            case time.Time:
                return value.Format(time.RFC3339)
            }
            fmt.Println("Got invalid type %T", value)
            return "INVALID"
        },
        ParseValue: func(value interface{}) interface{} {
            switch tvalue := value.(type) {
            case string:
                if tval, err := time.Parse(time.RFC3339, tvalue); err != nil {
                    return nil
                } else {
                    return tval
                }
            }
            return nil
        },
        ParseLiteral: func(valueAST ast.Value) interface{} {
            switch valueAST := valueAST.(type) {
            case *ast.StringValue:
                return valueAST.Value
            }
            return nil
        },
    },
)
```

Now you have a very useful DateTime type to use in your GraphQL definitions so you can have a type that looks like:

```
type Object {
	updated_at	DateTime
}
```
