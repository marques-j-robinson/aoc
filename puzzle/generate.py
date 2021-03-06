import re
import sys
import fileinput
from shutil import copyfile


event = 2015
day = 4


if __name__ == '__main__':
    filename = f'{event}_{str(day).zfill(2)}.py'
    copyfile('puzzle/template.py', filename)
    with open(filename, 'r+') as f:
        text = f.read()
        text = re.sub('EVENT', str(event), text)
        text = re.sub('DAY', str(day), text)
        f.seek(0)
        f.write(text)
        f.truncate()
