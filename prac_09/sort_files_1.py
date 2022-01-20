"""
CP1404 Practicals
Sort files into directory
"""

import os

def main():
    os.chdir("FilesToSort")

    for filename in os.getcwd():
        extension = filename.split('.')






main()