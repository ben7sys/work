#!/usr/bin/env python3
import json
from bs4 import BeautifulSoup

def parse_html(file):
    with open(file, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        title = soup.title.string
        bookmarks = []
        for li in soup.find_all('li'):
            link = li.a.get('href') if li.a else None
            bookmarks.append({'title': li.text, 'url': link})
        return {'title': title, 'bookmarks': bookmarks}

if __name__ == "__main__":
    import sys
    file_path = sys.argv[1] if len(sys.argv) > 1 else "bookmark.html"
    data = parse_html(file_path)
    json_data = json.dumps(data, indent=4)
    print(json_data)