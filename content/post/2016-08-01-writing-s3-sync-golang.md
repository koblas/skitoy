---
title: Writing S3 Sync in GoLang
author: koblas
type: post
date: 2016-08-01T18:01:16+00:00
url: /p/writing-s3-sync-golang/624
pvc_views:
  - 259
categories:
  - Development
tags:
  - golang
  - S3

---
One of the great challenges in software engineering is that you don&#8217;t know what the problem is until you&#8217;ve worked through it one. Sometimes this is the idea that you need to top down design a program which is a great start, but what&#8217;s interesting is when it comes to the language itself and what it makes easy and hard.

My latest project was a making a Go version of the [python s3cmd][1], there is now the [golang s3-cli][2] which supports most all of the basic file oriented commands that s3cmd has. While most commands are pretty easy &#8220;ls&#8221; for example, the challenging command is the &#8220;sync&#8221; command.

### The evolution of a sync command from basic approach to golang.

This is is a variation of the original code that was written for the sync command. As you can see it&#8217;s not complicated but if you wanted to use goroutines or other ways to improve performance you&#8217;re going to start splicing in a uglyness.

```go
// Retrieve a list of files from the source
src_files = getFiles(src)

// Retrieve a list of files from the destination
dst_files = getFiles(dst)

// Now figure out the differences
for _, file := range src_files {
    if in_slice(file, dst_files) {
       // check to see if it's the same (size/checksum) copy if needed
    } else {
       copyFile(...)
    }
}

for _, file := range dst_files {
    if !in_slice(file, src_files) {
       // destination file exists, remove since not in source
    }
}
```

### Version 2 &#8211; using queues

This version did exist, what you quickly see is that you&#8217;re creating a work queue with information. The idea was that it was a good way to start measuring the work to be done. How many bytes to transfer, show progress and percent completion since you&#8217;re not blocked on doing work in parallel to fetching data.

```go
type Action {
   src   string   // source file name
   dst   string   // destination file name
   action int     // action (COPY, DELETE, CHECKSUM)
}

// work queue
queue := make([]Action, 0)

// Retrieve a list of files from the source
src_files = getFiles(src)

// Retrieve a list of files from the destination
dst_files = getFiles(dst)

// Now figure out the differences
for _, file := range src_files {
    dst_path = transformPath(file)
    if in_slice(dst_file, dst_files) {
       // check to see if it's the same (size/checksum) copy if needed
    } else {
       queue = append(queue, Action{ src: file, dst: dst_path, action: COPY })
    }
}

for _, file := range dst_files {
    if !in_slice(file, src_files) {
       queue = append(queue, Action{ dst: file, action: REMOVE })
    }
}

for _, action := range queue {
   // do work, shared out with accounting.
}
```

### GoLang Native Sync

What&#8217;s great about evolving programs is that you originally start out with one idea and through a bit of cleanup and refactoring you realize that there is a more natural way of doing things in a language. It would be &#8220;easy&#8221; to take the queue that you just built above and start farming work out to workers. What&#8217;s really interesting is to realize that the queue could just be a set of channels.

So a more natural go program is going to look like (_note the actual code is more nuanced)._

```go
type Action {
   src   string   // source file name
   dst   string   // destination file name
   action int     // action (COPY, DELETE, CHECKSUM)
}

// Create some channels
chanCopy := make(chan Action, 1000)
chanRemove := make(chan Action, 1000)

// Create a few workers
for i := 0; i < 4; i++ {
   go workerCopy(chanCopy)
}
go workerRemove(chanRemove)


// Retrieve a list of files from the source
src_files = getFiles(src)

// Retrieve a list of files from the destination
dst_files = getFiles(dst)

// Now figure out the differences
for _, file := range src_files {
    dst_path = transformPath(file)
    if in_slice(dst_file, dst_files) {
       // check to see if it's the same (size/checksum) copy if needed
    } else {
       chanCopy <- Action{ src: file, dst: dst_path, action: COPY }
    }
}

for _, file := range dst_files {
    if !in_slice(file, src_files) {
       chanRemove <- Action{ dst: file, action: REMOVE }
    }
}
```

What&#8217;s really great is that now instead of creating a queue with work, we move the queue to a channel. We only have to start a set of workers to work on doing the copies. This is also now more natural go code.

 [1]: https://github.com/s3tools/s3cmd
 [2]: https://github.com/koblas/s3-cli
