import os
import shutil
src=input("enter source folder name")
dest=input("ender destination folder name")
src=src+"/"
dest=dest+"/"
list_of_files=os.listdir(src)
for file in list_of_files:
    shutil.copy((src+file),dest)