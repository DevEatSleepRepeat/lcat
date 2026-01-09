"""
lcat is a simple python script based off of "cat" to allow for the easier debugging and reading of long files.

MIT License

Copyright (c) 2025 Sam Bullock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys

def read(filename):
    # Open a file and return the internal data
    with open(filename, "r") as file:
        data = file.read()
        file.close()
        return data

def numerize(data):
    # Split lines to allow for each line to be modified individually
    split_data = data.splitlines()
    # Set a counter of lines
    counter = 0
    # Set the length of the max counters digits to set a reference for accurate line alignment
    numeral_len = len(str(len(split_data)))

    for i in split_data:
        # Create a dynamic spacing system to allow for accurate line alignment
        spacing = ""
        while len(spacing)+len(str(counter)) < numeral_len+1:
            spacing += " "

        # Modify and print the new string
        string = str(counter) + spacing + str(i)
        print(string)

        counter += 1

# Set a colored usage text for errors.
usage_text = "\033[0mUsage: \033[34mlcat\033[0m <filename/flag>\n  -i --info    | Display Program Info\n  -l --licence | Display Program Licence"

try:
    # Check Flags
    if sys.argv[1] == "-i" or sys.argv[1] == "--info":
        print(info+"\n"+usage_text)
    elif sys.argv[1] == "-l" or sys.argv[1] == "--license":
        print(license)
    else:
        # If no flags, numerize lines.
        file_data = read(sys.argv[1])
        numerize(file_data)

except FileNotFoundError:
    print("\033[31mError: The file \""+sys.argv[1]+"\" was not found in the current working directory\033[0m\n"+usage_text)

except IndexError:
    print("\033[31mError: No file was specified\n"+usage_text)

except UnicodeDecodeError:
    print("\033[31mError: File not supported by unicode\n"+usage_text)