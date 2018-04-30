#!/usr/bin/python
"""
A script that launch shadowsocks-libev service (server) automaticly by launching ss-server with all config files in /etc/shadowsocks-libev.
If using other version of shadowsocks, just modify the path (to the conf files) and command (of launching the service).
Written for Python2 because py3 is not included in CentOS.
"""
import os
path = '/etc/shadowsocks-libev'
files = os.listdir(path)
command = 'nohup ss-server -c /etc/shadowsocks-libev/{conf} -f {pid}'
for i in files:
    os.system(command.format(conf = i, pid = i.split('.')[0]))
