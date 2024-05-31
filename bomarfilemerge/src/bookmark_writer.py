from typing import List
import os

class BookmarkWriter:
    """
    A class for writing bookmarks to a file.

    Attributes:
        output_file (str): The path to the output file.
    """

    def __init__(self, output_file: str):
        self.output_file = output_file

    def write(self, bookmarks: List[str]):
        """
        Writes the given bookmarks to the output file.

        Args:
            bookmarks (List[str]): A list of bookmarks to write.

        Returns:
            None
        """
        with open(self.output_file, 'w') as f:
            for bookmark in bookmarks:
                f.write(f'<a href="{bookmark}">\n')