# String Manipulation Tool

A simple Python tool for manipulating and analyzing strings.

## Features

- Count words in a string
- Reverse a string
- Check if a string is a palindrome

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/StringManipulationTool.git
   ```

2. Navigate into the project folder:

   ```bash
   cd StringManipulationTool
   ```

3. Set up a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install dependencies (if any):

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Here are some examples of how to use the functions in this tool:

```python
from string_tool.main import count_words, reverse_string, is_palindrome

print(count_words("Hello world!"))  # Output: 2
print(reverse_string("Hello"))       # Output: "olleH"
print(is_palindrome("A man a plan a canal Panama"))  # Output: True
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
