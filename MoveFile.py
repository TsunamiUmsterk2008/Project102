import os
import shutil

from_dir = "/Users/tsunamiumsterk/Downloads"
to_dir = "/Users/tsunamiumsterk/Documents"
fileList = os.listdir(from_dir)
extensions = [".txt", ".doc", ".docx", ".pdf"]

for file in fileList:
    root, extension = os.path.splitext(file)
    if extension != '':
        if extension == ".txt" or extension == ".doc" or extension == ".docx" or extension == ".pdf":
            path1 = from_dir+'/'+file
            path2 = to_dir
            path3 = to_dir+'/'+extension

            if os.path.exists(path2):
                print("Moving " + file + ".....")
                shutil.move(path1, path3)
            else:
                os.makedirs(path2)
                print("Moving " + file + ".....")
                shutil.move (path1, path3)