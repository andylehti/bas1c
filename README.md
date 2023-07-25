# Base10 to Bas1c Number Converter

This repository contains a Python code that provides functions to convert numbers between Bas1c and base-10 representations.

## Features

- `generate_start_number(n)`: Generates the start number for a given length `n`. The start number is calculated as a string of `n` ones followed by a zero, and it is returned as an integer.
- `convert_to_bas1c(number)`: Converts a base-10 number to its Bas1c representation. Bas1c is a numeral system where the numbers are represented as strings of digits, and each digit is the number of zeros between consecutive ones. The function takes a base-10 `number` and returns its Bas1c representation as a string.
- `convert_to_base10(compact_number)`: Converts a Bas1c number to its base-10 representation. The function takes a `compact_number` string in Bas1c format and returns its base-10 equivalent as an integer.

## Usage

To use the functions in your Python code:

1. Call the desired function(s) with the appropriate arguments.
2. Bas1c to Base10 must be a string since it deals with leading 0s.
Here's an example:

```python

# decimal does not have to be input as a string, but the compact form does:
convert_to_bas1c(100) #000
convert_to_base10("000") #100

# authored by Andrew Lehti
```

## license
licensed under the Public Resource License v2
[https://github.com/andylehti/bas1c/LICENSE](https://github.com/andylehti/bas1c/blob/main/LICENSE)
