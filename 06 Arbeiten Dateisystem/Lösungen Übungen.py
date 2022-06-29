#Aufgabe 1
import os
import shutil as il
import glob
src_folder = r"C:/Users/xx/Documents"
dst_folder = r"C:/Users/xx/Documents/Textdateien/"
#Textdateien suchen
pattern = "\*.txt"
files = glob.glob(src_folder + pattern)
if not os.path.exists("C:/Users/xx/Documents/Textdateien/"):
    os.mkdir("C:/Users/xx/Documents/Textdateien/")

if not os.path.exists('C:/Users/xx/Desktop/test'):
    with open('C:/Users/xx/Desktop/test', "w"): pass
    print("file generated")
if os.path.exists("C:/Users/xx/Desktop/test"):
  os.remove("C:/Users/xx/Desktop/test")
  print("File Removed")
else:
    print("file doesn't exist")

if os.path.exists("C:/Users/xx/Desktop/Report"):
  os.remove("C:/Users/xx/Desktop/Report")
  print("File Removed")
else:
    with open('C:/Users/xx/Desktop/Report', "w"): pass
    print("file generated")
# move the files with txt extension
for file in files:
    # extract file name form file path
    file_name = os.path.basename(file)
    il.move(file, dst_folder + file_name)
    print('Moved:', file)
