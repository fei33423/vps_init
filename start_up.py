#!/usr/bin/python
"""
A script that launch shadowsocks-libev service (server) automaticly by launching ss-server with all config files in /etc/shadowsocks-libev.
If using other version of shadowsocks, just modify the path (to the conf files) and command (of launching the service).
Written for Python2 because py3 is not included in CentOS.
"""
import os
'''
# Kill ss services launched by the installation script.
if 'config' in os.listdir('/root/'):
    os.system('kill {pid}'.format(pid=int(open('/root/config').readline())))
'''
list_of_files = ['shadowsocks-libev.pid']
for i in os.listdir('/etc/shadowsocks-libev/'):
    list_of_files.append(i.split('.')[0] + '.pid')

# Kill all existing ss services.
for i in os.listdir('/var/run/'):
    if i in list_of_files:
        os.system('kill {pid}'.format(pid=int(open('/var/run/{conf}'.format(conf=i)).readline())))

# Launch all config files.
path = '/etc/shadowsocks-libev'
files = os.listdir(path)
command = 'nohup ss-server -c /etc/shadowsocks-libev/{conf} -f /var/run/{pid}.pid'
for i in files:
    os.system(command.format(conf = i, pid = i.split('.')[0]))
