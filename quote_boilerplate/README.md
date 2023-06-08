# Quote Manager

The `Quote` class represents a quote with its corresponding author. The `QuoteManager` class is responsible for managing a collection of quote files and providing methods to retrieve random quotes.

## Quote Class

### Constructor

- `__init__(self, value: str, author: str)`: Initializes a `Quote` object with the specified quote value and author.

### Class Methods

- `from_dict(cls, data: dict)`: Creates a `Quote` object from a dictionary representation.

### Properties

- `value`: Gets the value of the quote.
- `author`: Gets the author of the quote.

### String Representation

- `__str__()`: Returns a formatted string representation of the quote in the format: `<quote_value> ~ <quote_author>`

## QuoteManager Class

### Constructor

- `__init__(self, path: str = '.', filename: str = '*_quotes.json')`: Initializes a `QuoteManager` object with the specified path and filename pattern.

### Methods

- `get_files() -> List[str]`: Returns a list of quote file paths based on the specified path and filename pattern.
- `search_files(fragment: str) -> List[str]`: Searches for quote files that contain the specified fragment in their filenames.
- `get_quotes() -> List[Quote]`: Returns a list of `Quote` objects obtained from all the quote files.
- `get_random_quote() -> Quote`: Returns a random `Quote` object from the available quotes.

## Example

```python
if __name__ == '__main__':
    x = QuoteManager()
    print(x.get_random_quote())
```

In this example, a `QuoteManager` object is created, and a random quote is retrieved using the `get_random_quote()` method. The quote is then printed to the console.

> Note: Make sure to have the quote files in the specified format `('*_quotes.json')` in the specified directory or provide a custom path and filename pattern.

Feel free to customize and use the provided code to manage and retrieve quotes in your Python projects!
