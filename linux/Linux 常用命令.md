[参考](http://www.codeceo.com/article/100-linux-useful-command.html)
#### 文件
---
常用命令
```
ls, mv, cp, scp, rm, touch, pwd, cd, mkdir, echo, cat, more, less,head, tail, vim/vi, which, whereis, locate, find, grep
```
- rmdir 删除空目录
- tac 反向显示
- nl 将输出内容自动加上行号
- file 判断文件类型
- gzip 压缩，解压
- gunzip 解压
- bzip压缩、解压
- bcat 无解压读取
- tar 多目录打包、压缩解压
- cut
- sort
- wc
- uniq

#### 用户
--- 
```
users,who,useradd, passwd, groupadd, 
```
- userdel 删除用户
- chage 修改用户密码相关属性
- usermod 修改用户相关属性
- id
- groups 群组
- newgrp 切换群组
- groupmod 修改组信息
- groupdel 删除群组
- gpasswd 群组管理员
- chfn 修改个人信息
#### 系统
----
```
eixt, logout,shutdown, date, ps, top, kill, crontab, wget,su, sudo, ping
```
- write 给当前联机用户发消息
- wall 给所有登陆在本机的用户发消息
- last 查看用户的登陆日志
- lastlog 查看每个用户最后登陆时间
- finger* 查看用户信息
- hostname 查看主机名
- alias 添加别名
- unalias 清除别名
- mount 挂载
- umount 取消挂载
- set
- env
- export
- unset
- read
- declare, typeset
- ulimit
- df 显示指定磁盘文件的可用空间,如果没有文件名被指定，则所有当前被挂载的文件系统的可用空间将被显示
- du 显示文件和目录磁盘使用空间
- ln 创建连接
- diff 比较单个文件或目录内容
- cal 查看日历
- free
- vmstat
- iostat
- at
- ifconfig
- route
- netstat
- telnet
- rcp
- awk
- sed
- paste
