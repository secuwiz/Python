#!/usr/bin/python3

# Script to copy standard input to standard output using the
# basic raw input function.  

#
# Here's an example: Copy standard input to standard output.
while 1:
    try:
        s = input()
    except EOFError:
        break
    print(s)
