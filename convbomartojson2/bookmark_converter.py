# src/bookmark_converter.py
import json
from typing import List
from dataclasses import dataclass

# Define the Bookmark data class
@dataclass
class Bookmark:
    """Represents a single bookmark with title and url."""
    title: str
    url: str

def read_bookmarks(filepath: str) -> List[Bookmark]:
    """Reads the bookmarks from the given file path and returns them as a list of Bookmark objects."""
    bookmarks = []
    
    with open(filepath, 'r') as f:
        for line in f.readlines():
            parts = line.strip().split(',', 1)
            if len(parts) != 2:
                print(f"Skipping line: {line.strip()}")
                continue
            title, url = parts
            bookmarks.append(Bookmark(title=title, url=url))
            
    return bookmarks

# Define the write_bookmarks_to_json function
def write_bookmarks_to_json(filepath: str, bookmarks: List[Bookmark]):
    """Writes the given list of Bookmark objects to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump([vars(b) for b in bookmarks], f, indent=4)

# This script contains two main functions: `read_bookmarks` and `write_bookmarks_to_json`. 
# The former reads the bookmark file line by line, parsing each line into a Bookmark object using the provided title and url. 
# The latter writes these objects to a JSON file in an indented format for readability.