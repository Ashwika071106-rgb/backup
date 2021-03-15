import os 
import shutil

#Write the name of the directory here that needs to get sorted
path = input("Enter the name of the directory to be sorted : ")

#This will create a properly organised list with all the file names that is there in the directory
list_of_files = os.listdir(path)

#This will go through each and every file
for file in list_of_files : 
    name,ext = os.path.splitext(file) 

    #this is goin to store the extension type
    ext = ext[1 : ]

    #this forces the next iteration if it is the directory
    if(ext == '') : 
        continue

    #this will move the file to the directory where the name ext already exists
    if(os.path.exists(path + '/' + ext)) : 
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)

    else : 
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)

    