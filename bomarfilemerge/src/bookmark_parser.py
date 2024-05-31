from typing import List
import re

class BookmarkParser:
    """
    A class for parsing bookmarks from an HTML file.

    Attributes:
        file_path (str): The path to the HTML file.

    Methods:
        parse(): Parses the bookmarks from the HTML file and returns a list of bookmark URLs.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.bookmarks = []

    def parse(self):
        """
        Parses the bookmarks from the HTML file.

        Returns:
            list: A list of bookmark URLs.
        """
        with open(self.file_path) as f:
            content = f.read()
            matches = re.findall(r'<a href="(.*?)"', content, re.DOTALL)
            for match in matches:
                self.bookmarks.append(match)
        return self.bookmarks