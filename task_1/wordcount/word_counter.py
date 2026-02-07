"""
Word Counter - A simple program to count words in text files.

This module provides functionality to read text files and count the number
of words they contain, with robust error handling for common file operations.
"""

import sys
from typing import Optional



def count_words(text: str) -> int:
    """Count the number of words in the provided text.
    
    Words are defined as sequences of characters separated by whitespace.
    Multiple consecutive whitespace characters are treated as a single separator.
    
    Args:
        text: The text string to analyze
        
    Returns:
        The number of words in the text. Returns 0 for empty strings.
        
    Examples:
        >>> count_words("hello world")
        2
        >>> count_words("  multiple   spaces  ")
        2
        >>> count_words("")
        0
    """
    if not text:
        return 0
    
    # Split on whitespace and filter out empty strings
    words = text.split()
    return len(words)



def read_file(file_path: str) -> str:
    """Read and return the complete contents of a text file.
    
    Args:
        file_path: Path to the text file to read
        
    Returns:
        String containing the complete file contents
        
    Raises:
        FileNotFoundError: If the file does not exist
        PermissionError: If the file cannot be read due to permissions
        IOError: For other file reading errors
        
    Examples:
        >>> content = read_file("example.txt")
        >>> isinstance(content, str)
        True
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{file_path}' not found")
    except PermissionError:
        raise PermissionError(f"Error: Permission denied reading '{file_path}'")
    except Exception as e:
        raise IOError(f"Error: Could not read file '{file_path}': {str(e)}")



def count_words_in_file(file_path: str) -> int:
    """Count the number of words in a text file.
    
    This function orchestrates reading a file and counting its words.
    
    Args:
        file_path: Path to the text file to analyze
        
    Returns:
        The number of words in the file
        
    Raises:
        FileNotFoundError: If the file does not exist
        PermissionError: If the file cannot be read due to permissions
        IOError: For other file reading errors
        
    Examples:
        >>> count = count_words_in_file("example.txt")
        >>> isinstance(count, int)
        True
    """
    content = read_file(file_path)
    return count_words(content)



def main() -> None:
    """Main function to handle command-line interface.
    
    Parses command-line arguments, processes the specified file,
    and displays the word count or error messages.
    """
    # Check if file path argument is provided
    if len(sys.argv) < 2:
        print("Usage: python word_counter.py <file_path>")
        sys.exit(1)
    
    if len(sys.argv) > 2:
        print("Error: Too many arguments")
        print("Usage: python word_counter.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    try:
        word_count = count_words_in_file(file_path)
        print(f"\nWord Counter Results")
        print(f"--------------------")
        print(f"File: {file_path}")
        print(f"Word Count: {word_count}")
    except FileNotFoundError as e:
        print(f"\n{e}")
        sys.exit(1)
    except PermissionError as e:
        print(f"\n{e}")
        sys.exit(1)
    except IOError as e:
        print(f"\n{e}")
        sys.exit(1)
    except Exception as e:
        print(f"\nError: An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
