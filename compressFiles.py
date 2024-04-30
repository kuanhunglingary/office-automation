import pathlib
import zipfile

directory = pathlib.Path("/home/pythonPersonalTools/file")

# compress 
with zipfile.ZipFile("file.zip", mode="w") as archive:
    for file_path in directory.iterdir():
        archive.write(file_path, arcname=file_path.name)

# Read metadata from the zip file
with zipfile.ZipFile("file.zip", mode="r") as archive:
    archive.printdir()
