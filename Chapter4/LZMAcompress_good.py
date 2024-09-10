# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:08:55 2024

@author: Vincent Hall, Build Intellect Ltd.

Asking Claude 3 for some good code like that earlier: data compression with Python
Prompt for Claude 3: Please give me some Python 3.10 code that compresses tabular data with LZMA2 that is easy to understand because it’s well-written.
Here's a well-written Python 3.10 code that compresses tabular data using the LZMA2 algorithm. This code follows best practices and is designed to be easy to read and understand:
python"""

import lzma
from typing import List

def compress_tabular_data(tabular_data: List[List[str]]) -> bytes:
    """
    Compresses tabular data using the LZMA2 algorithm.

    Args:
        tabular_data: A list of lists representing tabular data, where each inner list is a row.

    Returns:
        A bytes object containing the compressed tabular data.
    """
    compressor = lzma.LZMACompressor(lzma.FORMAT_ALONE)
    compressed_data = []

    for row in tabular_data:
        row_bytes = '\t'.join(row).encode() + b'\n'
        compressed_data.append(compressor.compress(row_bytes))

    compressed_data.append(compressor.flush())

    return b''.join(compressed_data)

def decompress_tabular_data(compressed_data: bytes) -> List[List[str]]:
    """
    Decompresses tabular data compressed using the LZMA2 algorithm.

    Args:
        compressed_data: A bytes object containing the compressed tabular data.

    Returns:
        A list of lists representing the decompressed tabular data, where each inner list is a row.
    """
    decompressor = lzma.LZMADecompressor()
    decompressed_data = decompressor.decompress(compressed_data)
    rows = [row.split('\t') for row in decompressed_data.decode().split('\n') if row]
    return rows

if __name__ == '__main__':
    tabular_data = [
        ['Name', 'Age', 'City'],
        ['Alice', '25', 'New York'],
        ['Bob', '30', 'Los Angeles'],
        ['Charlie', '35', 'Chicago']
    ]

    # Compress tabular data
    compressed_data = compress_tabular_data(tabular_data)

    # Save compressed data to a file
    with open('compressed_data.lzma', 'wb') as file:
        file.write(compressed_data)

    # Load compressed data from the file
    with open('compressed_data.lzma', 'rb') as file:
        compressed_data = file.read()

    # Decompress tabular data
    decompressed_data = decompress_tabular_data(compressed_data)
    print(decompressed_data)

"""What Claude 3 says about its own good code

This code is easy to read and understand for the following reasons:
1.	Clear Function Names: The function names compress_tabular_data and decompress_tabular_data clearly describe the purpose of each function.
2.	Type Hints: The code uses type hints to specify the expected types of function arguments and return values, making it easier to understand the input and output formats.
3.	Docstrings: Each function has a docstring that provides a brief description of the function's purpose, its arguments, and its return value.
4.	Meaningful Variable Names: The variable names used in the code are descriptive and self-explanatory, making it easier to understand what each variable represents.
5.	Separation of Concerns: The code separates the compression and decompression logic into two distinct functions, making it easier to maintain and extend.
6.	Proper Indentation and Formatting: The code is properly indented and formatted, making it more readable and visually appealing.
7.	Error Handling: While not explicitly shown in this example, the code can be extended to include error handling mechanisms to handle potential exceptions or errors during compression or decompression.
8.	Modular Design: The code is designed in a modular way, allowing for easy integration into larger applications or libraries.
9.	Use of Standard Library: The code uses the standard lzma module from the Python standard library, which is well-documented and widely used.
10.	Example Usage: The code includes an example usage in the if __name__ == '__main__' block, making it easy to understand how to use the functions.
Overall, this code follows best practices for writing clean, readable, and maintainable Python code. It should be easy to understand for developers familiar with Python and the LZMA2 compression algorithm.

"""
