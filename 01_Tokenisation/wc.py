"""
count the number of lines, tokens and characters
hint: by counting the number of space characters you can count the number of tokens
"""
import sys
import re
number_line = 0
number_token = 0
number_characters = 0

for c in sys.stdin.read():
    if c == '\n':
        number_line = number_line + 1
    elif c == ' ':
        number_token = number_token + 1
    else:
        number_characters = number_characters + 1

print(number_line)
print(number_token)
print(number_characters)

