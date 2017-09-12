- nginx脚本所在位置: "/etc/init.d"  
  > 大多数的启动脚本都在此处
- nginx.conf所在位置: "/etc/nginx/"
  - 类似"user","woker_processes"等参数应该定义在第一级目录的nginx.conf
  - 具体的某个项目的配置放在conf.d内
    ```
    ├── conf.d
    │   └── nginx.conf
    └── nginx.conf
    ```
- 反向代理：http>server>location /[static]/>proxy_pass [https://api-id.hyku.org/v2/]
