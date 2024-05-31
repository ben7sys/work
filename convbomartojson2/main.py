# main.py
import os
from bookmark_converter import read_bookmarks, write_bookmarks_to_json

# Define the source and destination file paths
source_file = r"C:\tmp\BookmarkExports\bookmarks_31.05.24.html"
destination_file = r"C:\tmp\output.json"

# Ensure the source file exists
if __name__ == "__main__":
    bookmarks = read_bookmarks(source_file)
    write_bookmarks_to_json(destination_file, bookmarks)