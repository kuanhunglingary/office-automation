# Rename a file using Python pathlib module
from pathlib import Path

path = Path("target file")

target = path.with_name(path.name.replace("08",'09'))

path.rename(target)