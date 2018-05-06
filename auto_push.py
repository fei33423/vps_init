#!/usr/bin/python3
"""
Automatically push all git repo in current directory.
"""
import os
repo = os.listdir()
outlier = []
command = input('Do you want to push (defaut) or pull? ')
if command == '':
    command = 'push'
def exception():
    ask = input("Are there any repo you don't want to {}?(y/n) ".format(command))
    if ask == 'n' or ask == '':
        pass
    else:
        outlier.append(input('Enter the name of the exception: '))
        exception()

exception()

for i in repo:
    
    if '.' in i or i in outlier:
        continue

    os.chdir('/home/david/git/{}'.format(i))
    
    try:
        print('P{}ing {}'.format(command[1:], i))
        os.system('git {}'.format(command))

    except Error as err:
        print('Repository {} is un{}ed or it is not a git repo.'.format(i, command))
        continue
    
    print('Finished!')
    print('=' * 50)
    os.chdir('/home/david/git')

print('All finished!')
