"""
CP1404 Practicals
Sort files into directory
"""

import os
import shutil

def main():
    os.chdir("FilesToSort")
    print(os.getcwd())

    for filename in os.listdir('.'):
        extension = filename.split('.')
        file_extension = extension[1]
        print(file_extension)

    try:
        os.mkdir(extension)
    except FileExistsError:
        pass
    os.rename(filename, f"{file_extension},{filename}")
    shutil.move(filename, extension)





main()