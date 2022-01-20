"""
CP1404 Practicals
Sort files into directory
"""

import os
import shutil

def main():
    os.chdir("FilesToSort")
    print(os.getcwd())
    categories = []

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')
        file_extension = extension[1]
        if file_extension not in categories:
            category = input(f"What category would you like to sort {file_extension} files into?")
            categories.append(category)
            try:
                os.mkdir(file_extension)
            except FileExistsError:
                pass
        print(f"{file_extension}/{filename}")
        os.rename(filename, f"{file_extension}/{filename}")




main()