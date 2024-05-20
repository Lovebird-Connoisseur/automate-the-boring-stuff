# find all files with a given prefix in a single folder
# locates any gaps in the numbering
# renames all files in order to remove these gaps

import os, shutil
from pathlib import Path

p = Path.cwd()
operation_folder = Path.cwd() / 'filling_in_the_gaps'
filetype = '.txt'
filename = 'spam'
current_file_number = 0

for i in os.listdir(operation_folder):
    file_path = operation_folder / i
    if i[-4:] == filetype:
        if i[:4] == filename:
            current_file_number += 1
            if i[-5] != str(current_file_number):
                print(f'{i}: incorrect numbering')
                i_corrected = list(i)
                i_corrected[-5] = str(current_file_number)
                i_corrected = "".join(i_corrected)
                corrected_file = operation_folder / i_corrected
                shutil.move(file_path, corrected_file)
            else:
                print(f'{i} numbering is correct')
                pass
        else:
            pass
    else:
        pass