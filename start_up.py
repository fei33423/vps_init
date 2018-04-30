#!/usr/bin/python
import os
path = '/etc/shadowsocks-libev'
files = os.listdir(path)
command = 'nohup ss-server -c /etc/shadowsocks-libev/{conf} -f {pid}'
for i in files:
    os.system(command.format(conf = i, pid = i.split('.')[0]))
