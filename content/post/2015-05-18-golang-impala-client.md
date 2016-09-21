---
title: Golang Impala Client
author: koblas
layout: post
date: 2015-05-18T21:31:50+00:00
url: /p/golang-impala-client/574
pvc_views:
  - 1279
dsq_thread_id:
  - 3775103059
categories:
  - Development
tags:
  - golang
  - thrift

---
Yesterday&#8217;s post where I figured out what it took to build thrift interfaces to attach to Cloudera Impala got a big improvement today. I combined my work with the hivething project that Derek Greentree wrote. It&#8217;s of course called [impalathing][1] over on github, it really does clean up the API.

The big thing is that since this behind the scenes uses the ImpalaServer Thrift API everything is marshaled back from the server as TAB delimitated strings.  No helping that, but it gets a working system up and running pretty quick.  Now off to pull this into a real application to test some service architecture and real performance.

Here is the code to make calls &#8211; which is much simpler than everything else. It&#8217;s been good to look at some API patterns to make it this simple.

```go
package main

import (
    "log"
    "fmt"
    "time"
    "github.com/koblas/impalathing"
)

func main() {
    host := "impala-host"
    port := 21000

    con, err := impalathing.Connect(host, port, impalathing.DefaultOptions)

    if err != nil {
        log.Fatal("Error connecting", err)
        return
    }

    query, err := con.Query("SELECT user_id, action, yyyymm FROM engagements LIMIT 10000")

    startTime := time.Now()
    total := 0
    for query.Next() {
        var (
            user_id     string
            action      string
            yyyymm      int
        )

        query.Scan(&user_id, &action, &yyyymm)
        total += 1

        fmt.Println(user_id, action)
    }

    log.Printf("Fetch %d rows(s) in %.2fs", total, time.Duration(time.Since(startTime)).Seconds())
}
```

 [1]: https://github.com/koblas/impalathing
