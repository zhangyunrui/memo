- 显示grep行周围五行```<command> | grep [str] -C 5```
- 创建并进入文件夹```mkdir foo && cd $_```
- 选定后鼠标中键: 复制并粘贴
- 显示硬盘容量`df -h`
- `mkdir -p` -> no error if existing, make parent directories as needed
- 获取毫秒 `date +%s.%N`
- 同步系统时间 `ntpdate time.windows.com`


appSend   serverInitial   serverSend   routerRecv   routerReply   serverRecv   serverReply   appRecv
   |            |            |            |            |            |            |            |
   +------------+------------+------------+------------+------------+------------+------------+
   1            2            3            4            5            6            7            8
   
netTime = (t8-t1)-(t7-t2)
serverTime = (t7-t2)-(t6-t3)
mqttTime = (t6-t3)-(t5-t4)
routerTime = t5-t4 -> `routerReply-routerRecv`