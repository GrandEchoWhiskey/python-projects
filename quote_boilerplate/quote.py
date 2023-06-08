import json
import os
import random
from typing import List

class Quote:

    def __init__(self, value: str, author: str):
        self.__value = value
        self.__author = author

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data['quote'], data['author'])
    
    @property
    def value(self):
        return self.__value
    
    @property
    def author(self):
        return self.__author
    
    def __str__(self):
        return f"{self.value} ~ {self.author}"

def get_quote_files(path: str = '.') -> List[str]:
    """Get all files in a directory recursively."""
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.json') and 'quotes' in filename:
                files.append(os.path.abspath(os.path.join(dirpath, filename)))
    if len(files) == 0:
        raise FileNotFoundError('No quote files found.')
    return files

def search_quote_file(fragment: str):
    """Find a quotes file."""
    files = get_quote_files()
    results = []
    for file in files:
        filename = file.split('/')[-1]
        if fragment in filename:
            results.append(file)
    if len(results) == 0:
        raise FileNotFoundError('No quote files found.')
    return results

def get_quotes(file: str):
    """Get quotes from a file."""
    with open(file, 'r') as f:
        quotes = json.load(f)
    return quotes

def get_random_quote(file: str):
    """Get a random quote from a file."""
    quotes = get_quotes(file)
    return random.choice(quotes)

if __name__ == '__main__':
    using_file = random.choice(get_quote_files())
    q = Quote.from_dict(get_random_quote(using_file))
    print(q)