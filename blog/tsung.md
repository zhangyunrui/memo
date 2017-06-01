### 简介
一个开源的多协议分布式负载测试工具，使用erlang语言开发

### 作用
tsung使用了epoll技术，在一个进程中，就可以管理上万级别的socket（注意ulimit-n的限制），相对于其它使用多线程的压测工具（如webbench），tsung消耗小得多得多。另外，tsung使用多进程，使用系统的SMP？特性，相比于ab，可以更充分利用资源。

### 例子
```xml

```
- arrivalphase