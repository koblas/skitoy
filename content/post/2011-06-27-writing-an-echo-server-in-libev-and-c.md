---
title: Writing an echo server in libev and c++
author: koblas
layout: post
date: 2011-06-28T00:33:13+00:00
url: /p/writing-an-echo-server-in-libev-and-c/375
aktt_notify_twitter:
  - yes
pvc_views:
  - 33139
aktt_tweeted:
  - 1
dsq_thread_id:
  - 343898152
categories:
  - General
tags:
  - libev
  - programming

---
Looking at event IO frameworks and found some really good comments about the &#8220;ev&#8221; library, the challenge is that I would rather work in C++ than pure C &#8211; I like methods.. Found that the documentation is lacking for the C++ side of the library and needed to build a test harness.

This is a very basic TCP Echo server using libev in c++. The C++ side is only using std::list and the ev side is playing with loop, signals and basic socket IO. It should be a useful bread crumb for anybody trying to build their own service, which of course is my next big activity.

**Update**: Fixed the small file descriptor leak and now available as a Gist &#8211; <https://gist.github.com/3364414>

```c++
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>
#include <ev++.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <resolv.h>
#include <errno.h>
#include <list>
  
//
//   Buffer class - allow for output buffering such that it can be written out 
//                                 into async pieces
//
struct Buffer {
        char       *data;
        ssize_t len;
        ssize_t pos;
  
        Buffer(const char *bytes, ssize_t nbytes) {
                pos = 0;
                len = nbytes;
                data = new char[nbytes];
                memcpy(data, bytes, nbytes);
        }
  
        virtual ~Buffer() {
                delete [] data;
        }
  
        char *dpos() {
                return data + pos;
        }
  
        ssize_t nbytes() {
                return len - pos;
        }
};
  
//
//   A single instance of a non-blocking Echo handler
//
class EchoInstance {
private:
        ev::io           io;
        static int total_clients;
        int              sfd;
  
        // Buffers that are pending write
        std::list<Buffer*>     write_queue;
  
        // Generic callback
        void callback(ev::io &watcher, int revents) {
                if (EV_ERROR & revents) {
                        perror("got invalid event");
                        return;
                }
  
                if (revents & EV_READ) 
                        read_cb(watcher);
  
                if (revents & EV_WRITE) 
                        write_cb(watcher);
  
                if (write_queue.empty()) {
                        io.set(ev::READ);
                } else {
                        io.set(ev::READ|ev::WRITE);
                }
        }
  
        // Socket is writable
        void write_cb(ev::io &watcher) {
                if (write_queue.empty()) {
                        io.set(ev::READ);
                        return;
                }
  
                Buffer* buffer = write_queue.front();
                          
                ssize_t written = write(watcher.fd, buffer->dpos(), buffer->nbytes());
                if (written < 0) {
                        perror("read error");
                        return;
                }
  
                buffer->pos += written;
                if (buffer->nbytes() == 0) {
                        write_queue.pop_front();
                        delete buffer;
                }
        }
  
        // Receive message from client socket
        void read_cb(ev::io &watcher) {
                char       buffer[1024];
  
                ssize_t   nread = recv(watcher.fd, buffer, sizeof(buffer), 0);
  
                if (nread < 0) {
                        perror("read error");
                        return;
                }
  
                if (nread == 0) {
                        // Gack - we're deleting ourself inside of ourself!
                        delete this;
                } else {
                        // Send message bach to the client
                        write_queue.push_back(new Buffer(buffer, nread));
                }
        }
  
        // effictivly a close and a destroy
        virtual ~EchoInstance() {
                // Stop and free watcher if client socket is closing
                io.stop();

                close(sfd);
  
                printf("%d client(s) connected.\n", --total_clients);
        }
  
public:
        EchoInstance(int s) : sfd(s) {
                fcntl(s, F_SETFL, fcntl(s, F_GETFL, 0) | O_NONBLOCK); 
  
                printf("Got connection\n");
                total_clients++;
  
                io.set<EchoInstance, &EchoInstance::callback>(this);
  
                io.start(s, ev::READ);
        }
};
  
class EchoServer {
private:
        ev::io           io;
        ev::sig         sio;
        int                 s;
  
public:
  
        void io_accept(ev::io &watcher, int revents) {
                if (EV_ERROR & revents) {
                        perror("got invalid event");
                        return;
                }
  
                struct sockaddr_in client_addr;
                socklen_t client_len = sizeof(client_addr);
  
                int client_sd = accept(watcher.fd, (struct sockaddr *)&client_addr, &client_len);
  
                if (client_sd < 0) {
                        perror("accept error");
                        return;
                }
  
                EchoInstance *client = new EchoInstance(client_sd);
        }
  
        static void signal_cb(ev::sig &signal, int revents) {
                signal.loop.break_loop();
        }
  
        EchoServer(int port) {
                printf("Listening on port %d\n", port);
  
                struct sockaddr_in addr;
  
                s = socket(PF_INET, SOCK_STREAM, 0);
  
                addr.sin_family = AF_INET;
                addr.sin_port     = htons(port);
                addr.sin_addr.s_addr = INADDR_ANY;
  
                if (bind(s, (struct sockaddr *)&addr, sizeof(addr)) != 0) {
                        perror("bind");
                }
  
                fcntl(s, F_SETFL, fcntl(s, F_GETFL, 0) | O_NONBLOCK); 
  
                listen(s, 5);
  
                io.set<EchoServer, &EchoServer::io_accept>(this);
                io.start(s, ev::READ);
  
                sio.set<&EchoServer::signal_cb>();
                sio.start(SIGINT);
        }
          
        virtual ~EchoServer() {
                shutdown(s, SHUT_RDWR);
                close(s);
        }
};
  
int EchoInstance::total_clients = 0;
  
int main(int argc, char **argv) 
{
        int         port = 8192;
  
        if (argc > 1)
            port = atoi(argv[1]);
                  
        ev::default_loop       loop;
        EchoServer             echo(port);
  
        loop.run(0);
  
        return 0;
}
```
