import os
import shutil

source = input("Enter the source folder name : ")
dest = input("Enter the destination folder name : ")

source = source + '/'
dest = dest + '/'

list_of_files = os.listdir(source)

for file in list_of_files : 
    shutil.move((source + file),dest)