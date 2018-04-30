#!/usr/bin/python3
"""
Automatically push all git repo in current directory.
"""
import os
repo = os.listdir()
outlier = []
def exception():
    ask = input("Are there any repo you don't want to push?(y/n)")
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
        print('Pushing {}'.format(i))
        os.system('git push')

    except Error as err:
        print('Repository {} is unpushed or it is not a git repo.'.format(i))
        continue
    
    print('Finished!')
    os.chdir('/home/david/git')

print('All finished!')
