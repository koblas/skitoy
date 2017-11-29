---
title: Spark and Avro – in a Docker
author: koblas
type: post
date: 2016-09-14T00:28:07+00:00
url: /p/spark-avro-docker/634
pvc_views:
  - 46
categories:
  - Development
tags:
  - spark
  - avro
  - docker

---
These are really cliff notes for the next person, but quite useful.

Was working with Spark in a local Docker using the very useful  [jupyter/docker-stacks][1], these are really nice to get a fully working Spark installation on your Mac without messing with lots of packages on your local machine. I&#8217;m now a big convert of working from Docker since I don&#8217;t have to keep on installing and installing things.

Basic Jupyter functionality &#8212;

```bash
docker run -d \
       -v /Users/koblas/spark_demo:/home/jovyan/work \
       -p 8888:8888 -p 4040:4040 \
       jupyter/all-spark-notebook
```

Quick explanation (for those not in the know):

  * -d == detached, run in the background
  * -v &#8230; == mount the local Mac path as the /work directory on the Docker
  * -p 8888:8888 == the Notebook UI port
  * -p 4040:4040 == the Spark UI

Nice part is that with this one command you have a fully functional environment to work from. With one exception, you can&#8217;t load an AVRO format file into Python Spark. You quickly find the reference for how to do it if you&#8217;ve got an exposed environment on the README https://github.com/databricks/spark-avro . Just one problem, it&#8217;s not at all clear what environment variable you need.

```bash
docker run -d \
       -v /Users/koblas/spark_demo:/home/jovyan/work \
       -e PYSPARK_SUBMIT_ARGS='--packages com.databricks:spark-avro_2.10:2.0.1 pyspark-shell'
       -p 8888:8888 -p 4040:4040 \
       jupyter/all-spark-notebook
```

What is needed is the magic with PYSPARK\_SUBMIT\_ARGS which will invoke the shell with the additional package. This will work as well, it would be great if the jupyter documentation could get updated.

 [1]: https://github.com/jupyter/docker-stack
