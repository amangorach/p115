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