# Word Counter

A simple Python command-line program that reads text files and counts the number of words they contain.

## Features

- Read text files with UTF-8 encoding
- Count words accurately (whitespace-separated tokens)
- Handle multiple consecutive spaces correctly
- Comprehensive error handling (file not found, permission errors)
- Clear, user-friendly output
- Type-safe implementation with type hints

## Installation

No external dependencies required for basic usage. Uses Python standard library only.

For running property-based tests (optional):
```bash
pip install hypothesis
```

## Usage

Run the word counter with a file path:
```bash
python word_counter.py <file_path>
```

### Example

```bash
python word_counter.py sample.txt
```

Output:
```
Word Counter Results
--------------------
File: sample.txt
Word Count: 20
```

### Error Handling

**File not found:**
```bash
python word_counter.py nonexistent.txt
```
Output: `Error: File 'nonexistent.txt' not found`

**No arguments:**
```bash
python word_counter.py
```
Output: `Usage: python word_counter.py <file_path>`

## Running Tests

Run unit tests:
```bash
python -m unittest test_word_counter.py
```

Or with verbose output:
```bash
python -m unittest test_word_counter.py -v
```

## Code Quality

- ✅ Type hints for all functions
- ✅ Comprehensive docstrings
- ✅ Error handling with descriptive messages
- ✅ Clean, maintainable code structure
- ✅ Follows PEP 8 style guidelines

## Project Structure

```
task3/
├── word_counter.py       # Main implementation
├── test_word_counter.py  # Unit tests
├── sample.txt           # Example text file
└── README.md            # This file
```

## How It Works

1. **File Reading**: Opens and reads the specified file with UTF-8 encoding
2. **Word Splitting**: Splits text on whitespace characters
3. **Word Counting**: Counts non-empty tokens
4. **Output**: Displays filename and word count in a formatted output

## Requirements

- Python 3.7 or higher
- No external dependencies for core functionality
