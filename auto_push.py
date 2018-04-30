#!/usr/bin/python3
"""
Automatically push all git repo in current directory.
"""
import os
repo = os.listdir()
for i in repo:
    
    if '.' in i:
        continue
    
    print(i)
    os.chdir('/home/david/git/{}'.format(i))
    
    try:
        os.system('git push')
    except Error as err:
        print('Repository {} is unpushed or it is not a git repo.'.format(i))
    os.chdir('/home/david/git')
