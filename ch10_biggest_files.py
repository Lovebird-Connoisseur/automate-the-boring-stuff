# walk through a directory (doesnt add to filepath when walks inside folders)

import os
from pathlib import Path

p = Path.cwd()

for folder, subfolder, filename in os.walk(p):
    current_folder = Path(folder)
    for i in filename:
        filepath = Path(current_folder / i)
        if os.path.getsize(filepath) > 1000:
            print(filepath)
