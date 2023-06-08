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

class QuoteMenager:

    def __init__(self, path: str = '.', filename: str = '*_quotes.json'):
        self.__path = path
        self.__filename = filename

        if filename.count('*') > 1:
            raise ValueError('Filename can only contain one wildcard.')
        
        self.__files = self.get_files()
    
    def __is_file(self):
        return os.path.isfile(self.__path)
    
    @property
    def __prefix(self):
        splitted = self.__filename.split('*')
        if len(splitted) > 0:
            return splitted[0]
        return self.__filename
    
    @property
    def __suffix(self):
        splitted = self.__filename.split('*')
        if len(splitted) > 1:
            return splitted[1]
        return self.__filename
    
    def get_files(self) -> List[str]:
        files = []
        if self.__is_file():
            return files
        for dirpath, dirnames, filenames in os.walk(self.__path):
            for filename in filenames:
                if filename.endswith(self.__suffix) and filename.startswith(self.__prefix):
                    files.append(os.path.abspath(os.path.join(dirpath, filename)))
        if len(files) == 0:
            raise FileNotFoundError('No quote files found.')
        return files
    
    def search_files(self, fragment: str) -> List[str]:
        files = self.get_files()
        results = []
        for file in files:
            filename = file.split(os.sep)[-1]
            filename = filename[len(self.__prefix):len(self.__suffix) * -1]
            if fragment in filename:
                results.append(file)
        if len(results) == 0:
            raise FileNotFoundError('No quote files found.')
        self.__files = results
    
    def get_quotes(self) -> List[Quote]:
        if len(self.__files) == 0:
            raise FileNotFoundError('No quote files found.')
        quotes = []
        for file in self.__files:
            if not os.path.isfile(file):
                raise FileNotFoundError(f'File {file} not found.')
            with open(file, 'r') as f:
                quotes.extend(json.load(f))
        qs = []
        for q in quotes:
            qs.append(Quote.from_dict(q))
        return qs
    
    def get_random_quote(self) -> Quote:
        quotes = self.get_quotes()
        if len(quotes) == 0:
            raise ValueError('No quotes found.')
        return random.choice(quotes)

if __name__ == '__main__':
    x = QuoteMenager()
    print(x.get_random_quote())