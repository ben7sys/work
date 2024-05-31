import os
from pathlib import Path

class DirectoryScanner:
    def __init__(self, directory: str):
        self.directory = directory

    def scan(self):
        bookmark_files = []
        for root, _, files in os.walk(self.directory):
            for file in files:
                if file.endswith('bookmark.html'):
                    bookmark_files.append(Path(root) / file)
        return bookmark_files