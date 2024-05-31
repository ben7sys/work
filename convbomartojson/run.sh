$ python3 bookmark_script.py
Installing dependencies...
Done!
Running all necessary parts of the codebase...
Done!

#!/usr/bin/env python3
import subprocess

def install_dependencies():
    subprocess.call(['pip', 'install', 'requests'])

def run_codebase():
    with open('bookmark.html') as f:
        print("Installing dependencies...")
        install_dependencies()
        print("Done!\n")

        print("Running all necessary parts of the codebase...")
        subprocess.call(['python', 'bookmark_script.py'])
        print("Done!")

run_codebase()

import os

def find_files(folder_path, ext):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(ext):
                print(os.path.join(root, file))

find_files('/Users/username/Documents', '.txt')

import os
import re

def find_files(folder_path, ext, pattern):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(ext) and re.match(pattern, file):
                print(os.path.join(root, file))

find_files('/Users/username/Documents', '.txt', '^[a-zA-Z]+$')
