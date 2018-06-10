#!/usr/bin/python
"""
A script that launch shadowsocks-libev service (server) automaticly by launching ss-server with all config files in /etc/shadowsocks-libev.
If using other version of shadowsocks, just modify the path (to the conf files) and command (of launching the service).
Written for Python2 because py3 is not installed in CentOS by default.
If you do not want to launch any config file, just rename the file by removing the suffix.
"""
import os

list_of_files = ['shadowsocks-libev.pid'] # List of all pid files.
for i in os.listdir('/etc/shadowsocks-libev/'):
    list_of_files.append(i.split('.')[0] + '.pid')

# Kill all existing ss services.
for i in os.listdir('/var/run/'):
    if i in list_of_files:
        os.system('kill {pid}'.format(pid=int(open('/var/run/{conf}'.format(conf=i)).readline())))

# Launch all config files.
path_of_conf = '/etc/shadowsocks-libev/'
files = os.listdir(path_of_conf)
command = 'nohup ss-server -c {conf} -f /var/run/{pid}.pid'
for i in files:
    if 'json' in i:
        os.system(command.format(conf = path_of_conf + i, pid = i.split('.')[0]))
