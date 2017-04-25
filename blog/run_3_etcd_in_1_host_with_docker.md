### 目标
在一个主机内用docker生成一个3节点的etcd
### 知识点
- [docker network create](./coreos/docker/network.md#create)
- [docker run --ip](./coreos/docker/run.md#指定ip)
### 操作流程
1. 生成用户自定义的 bridge network，
shell： `docker network create dockeretcd --subnet 172.18.0.0/16` 
> subnet必须人为指定
2. 生成etcd1，shell：
```sh
docker run -d -v /usr/share/ca-certificates/:/etc/ssl/certs \
--network dockeretcd \
--ip 172.18.0.2 \
--name etcd1 elcolio/etcd \
-name etcd1 \
-advertise-client-urls http://172.18.0.2:2379,http://172.18.0.2:4001 \
-listen-client-urls http://0.0.0.0:2379,http://0.0.0.0:4001 \
-initial-advertise-peer-urls http://172.18.0.2:2380 \
-listen-peer-urls http://0.0.0.0:2380 \
-initial-cluster-token etcd-cluster-1 \
-initial-cluster etcd1=http://172.18.0.2:2380,etcd2=http://172.18.0.3:2380,etcd3=http://172.18.0.4:2380 \
-initial-cluster-state new
``` 
> --network指定1中生成的dockeretcd

> --ip必须在1中subnet指定的范围内
3. 把上述命令中除initial-cluster这行之外的`172.18.0.2`替换成`172.18.0.3`和`172.18.0.4`，把`etcd1`替换成`etcd2`和`etcd3`，
分别执行，以生成etcd2和etcd3
### 下一步
- 在docker跑的过程中加link
- 重新实现此目标，network用host模式
- 写docker-compose.yml时，etcd的参数到底该写在哪儿
- [关于docker的15个小tip](http://www.cnblogs.com/elnino/p/3899136.html)
- [容器间通信](https://docs.docker.com/engine/userguide/networking/default_network/container-communication/)
- 通过nginx等动态发现节点
- 集群管理，增加及删除节点等
