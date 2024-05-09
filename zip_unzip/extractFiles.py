import zipfile

file_name ="/home/pythonPersonalTools/file.zip"

with zipfile.ZipFile("file.zip", mode="r") as archive:
    for file in archive.namelist():
        archive.extract(file,"/home/pythonPersonalTools/file.zip")

# import zipfile

# file_name ="/home/gary/Code/toolbox_gary/zipFile.zip"

# with zipfile.ZipFile(file_name, 'r') as file:
#     file.extractall()
