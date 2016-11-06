'''
Directory Backup

Run inside any directory to zip the contents of that current working directory.
Once zipped, this will move them into a ZFS mountpoint which is mapped to a
dataset on an external drive.
'''

import zipfile
import shutil
import os
import datetime

# Directory to be backed up
source = os.getcwd()

# Absolute path of current working directory
absolutePath = os.path.abspath(os.getcwd())

# ZFS mountpoint to store zip file
destination = '/mypool/backup'

# Current date and time
now = str(datetime.datetime.now().strftime('%m-%d-%Y-%H-%M-%S'))

# Zip file name
zipname = source + '-' + now + '.zip'

# Create zip file object in write mode
zipper = zipfile.ZipFile(zipname, 'w', allowZip64 = True)

# Walk through each file in the current working directory and write to zip file
def backup():
    print('Creating ' + zipname + ' file...')
    for files in os.listdir(source):
        zipper.write(files)
    zipper.close()
    print('Done.')

# Move zip file to ZFS mountpoint
def move():
    print('Moving to ZFS mountpoint')
    os.chdir(absolutePath)
    shutil.move(zipname, destination)
    print('Done.')

#Main function
def main():
    backup()
    move()

if __name__ == '__main__':
    main()
