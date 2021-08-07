import os
import os.path
from os import listdir
from os.path import isfile, join
import shutil
import time

source = r'E:\Documents\Data Science\Copying files based on date modified\Sample Files'
destination = r'E:\Documents\Data Science\Copying files based on date modified\Final Files'

os.chdir(source)

onlyfiles = [f for f in listdir(source) if isfile(join(source, f))]
print(onlyfiles)

for names in onlyfiles:
   
    print('File Name:' , names)
    print("Last modified: %s" % time.ctime(os.path.getmtime(names)))
    print("Created: %s" % time.ctime(os.path.getctime(names)))
    print('------------------------')

    restofname = str(time.ctime(os.path.getmtime(names)).replace(':', '_'))

    Newfolder = 'Date Modified ' + restofname[0:10] + ' ' + restofname [-4:-1] + restofname[-1]
    os.chdir(destination)
   
    if not os.path.exists(Newfolder):
         os.mkdir(Newfolder)

    src_path = source + '\\' + str(names)
    dest_path = destination + '\\' + str(Newfolder)
    shutil.copy(src_path, dest_path)

    os.chdir(source)
