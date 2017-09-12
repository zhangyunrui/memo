### 简介
一个开源的多协议分布式负载测试工具，使用erlang语言开发

### 作用
tsung使用了epoll技术，在一个进程中，就可以管理上万级别的socket（注意ulimit-n的限制），相对于其它使用多线程的压测工具（如webbench），tsung消耗小得多得多。另外，tsung使用多进程，使用系统的SMP？特性，相比于ab，可以更充分利用资源。

### 例子
```xml

```
- arrivalphase


tsung start

运行完，在 ~/.tsung/log 目录会生成一个以时间命名的目录，进入这个目录
cd ~/.tsung/log/xxxxx
/usr/lib/tsung/bin/tsung_stats.pl （有时可能是 /usr/local/lib/tsung/bin/tsung_stats.pl)

生成 html 的压力测试报告
firefox report.html
除了 http 以外 tsung 还可以压很多东西，比如：jabber, postgreSQL 还可以写插件来给任何你想要测试的东西加压.