'''
Home Backup

This will be used to backup a home folder
for a specified user. The results of which will
be moved into a ZFS mountpoint
'''

import zipfile
import shutil
import os

'''
def backup():
    os.chdir('/home/')
    folder = os.path.abspath(user)
    print('Creating zip file...')
    for root, dirs, files in os.walk(folder):
        for filename in files:
            zippy.write(os.path.join(root, filename))
    zippy.close()
    move()

def move():
    os.chdir('/home/steve/homeautomation')
    shutil.move(zipname, '/mypool/backup')
    print('Done.')

user = raw_input('Backup which user: ')
zipname = user+'.zip'
zippy = zipfile.ZipFile(zipname, 'w', allowZip64 = True)

backup()
'''

def backup():
    cwd = os.getcwd()
    print('Creating zip file...')
    for root, dirs, files in cwd:
        for filename in files:
            zippy.write(os.path.join(root, filename))
    zippy.close()
    move()

def move():
    os.chdir('/home/steve/homeautomation')
    shutil.move(zipname, '/mypool/backup')
    print('Done.')

zipname = os.getcwd()+'.zip'
zippy = zipfile.ZipFile(zipname, 'w', allowZip64 = True)
