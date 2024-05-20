import shutil, os
from pathlib import Path

p = Path.cwd()
to_copy = Path.cwd() / 'origin'
to_paste = Path.cwd() / 'destination'

for folder_name, subfolder, filenames in os.walk(to_copy):
    parent_folder = Path(to_copy / folder_name)
    for i in filenames:
        if i[-4:] == '.pdf':
            print("Copying files....")
            file_to_copy = Path(parent_folder / i)
            shutil.copy(file_to_copy, to_paste)

print("Done!")
print(os.listdir(to_copy))
