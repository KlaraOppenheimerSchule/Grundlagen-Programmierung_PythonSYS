import os

file_oldname = os.path.join("c:\\Folder-1", "OldFileName.txt")
file_newname_newfile = os.path.join("c:\\Folder-1", "NewFileName.NewExtension")

os.rename(file_oldname, file_newname_newfile)