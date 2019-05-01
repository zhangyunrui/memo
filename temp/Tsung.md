- 启动时报错：`Erlang version has changed ! [5.9.1] != [5.10.4]` 解决办法: 
  - `sudo add-apt-repository ppa:tsung/stable`
  - `sudo apt-get update`
  
- 启动时报错: `Host key verification failed` 
这是因为tsung通过主机名（而不是ip地址）互相登陆，解决办法:
  - `ssh <host_name>` yes 之后会在 `.ssh/known_hosts` 文件中记下主机名的登录
  
- report 里报错: `error_connect_emfile`, 解决办法:
  - 改文件的 soft limits 和 hard limits `emacs /etc/security/limits.conf`

