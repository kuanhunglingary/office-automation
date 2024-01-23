# Using python to rename multiple files
import os

rootdir = r'target'

str = "08"

for filename in os.listdir(rootdir):
    if str in filename:
        filepath = os.path.join(rootdir, filename)
        newfilepath = os.path.join(rootdir, filename.replace(str, "09"))
        os.rename(filepath, newfilepath)