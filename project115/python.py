from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import shutil

source = "C:/Users/rahil/OneDrive/Documents/main.txt"
dest = "C:/Users/rahil/OneDrive/Documents/newfile.txt"

if os.path.exists(source):
    os.rename(source,dest)
else:
    os.makedirs(source)
    os.rename(source,dest)
#Ma'am we don't need the files as the code will check if there is a file or not
#if yes, then it will rename 
#if no, then it will make a file then rename it
