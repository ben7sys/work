import sys
from typing import List, Dict
from datetime import datetime
from dateutil.parser import parse
from bs4 import BeautifulSoup

class Bookmark:
    def __init__(self, url: str, description: str, icon: str, add_date: str, last_modified: str):
        self.url = url
        self.description = description
        self.icon = icon
        self.add_date = parse(add_date).strftime("%Y-%m-%d %H:%M:%S")
        self.last_modified = parse(last_modified).strftime("%Y-%m-%d %H:%M:%S")

def convert_bookmark_file(input_path: str, output_path: str):
    with open(input_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "lxml")
        bookmarks: List[Bookmark] = []
        for link in soup.find_all("a"):
            add_date = link["ADD_DATE"]
            last_modified = link["LAST_MODIFIED"]
            description = link.text
            url = link["HREF"]
            bookmarks.append(Bookmark(url, description, "", add_date, last_modified))
        output_dict: Dict[str, List[Bookmark]] = {"bookmarks": bookmarks}
        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(output_dict, file)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python bookmark_converter.py <input_path> <output_path>")
        sys.exit(1)
    convert_bookmark_file(sys.argv[1], sys.argv[2])