import re, os, shutil
from pathlib import Path

text_to_match = input('> ')
p = Path.cwd()
to_search = re.compile(fr'{text_to_match}')
print(to_search)


for i in os.listdir(p):
    if str(i[-4:]) == '.txt':
        f = open(i, "r")
        contents = str(f.read())
        matches = to_search.findall(contents)
        print(matches)