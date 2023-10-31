import os
import shutil

from_dir="c://Users//Bob//Downloads"
to_dir="c://Users//Bob//105"

list_of_files=os.listdir(from_dir)

for file_name in list_of_files:

    name,ext=os.path.splitext(file_name)

    if ext==" ":
        continue
    if ext in ['.jpeg','.jpg','.png','.gif','.jfif']:
        path1=from_dir+'//'+file_name
        path2=to_dir+'//'+file_name
        path3=to_dir+'//'+'moved_files'

        if os.path.exists(path3):
            print('moving'+file_name+'...')
            shutil.move(path1,path2)
        else:
            os.makedirs(path3)
            print('moving'+file_name+'...')
            shutil.move(path1,path2)
