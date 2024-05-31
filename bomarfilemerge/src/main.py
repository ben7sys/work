import sys
from dataclasses import asdict
from typing import List

from bookmark_parser import BookmarkParser
from directory_scanner import DirectoryScanner
from bookmark_writer import BookmarkWriter

def main():
    """
    Entry point of the program.

    Usage: python3 main.py <directory>

    This function takes a directory path as a command-line argument and performs the following steps:
    1. Scans the directory for bookmark files.
    2. Parses each bookmark file.
    3. Combines all the bookmarks into a single list.
    4. Writes the consolidated bookmarks to a file named 'consolidated_bookmarks.html'.
    5. Prints a message indicating the completion of the consolidation process.

    If the number of command-line arguments is not equal to 2, it displays the usage message and exits the program.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    scanner = DirectoryScanner(directory)
    bookmark_files = scanner.scan()
    combined_bookmarks = []

    for file in bookmark_files:
        parser = BookmarkParser(file)
        bookmarks = parser.parse()
        combined_bookmarks += bookmarks

    writer = BookmarkWriter('consolidated_bookmarks.html')
    writer.write(combined_bookmarks)
    print("Consolidation complete!")

if __name__ == "__main__":
    main()