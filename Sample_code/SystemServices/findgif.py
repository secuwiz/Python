#!/usr/bin/python3

# Use the os interface to look for png files.
import os, sys, fnmatch

if len(sys.argv) > 1:
    dirs = sys.argv[1:]
else:
    dirs = [ '.' ]

# Go for it.
while dirs != []:
    dir = dirs.pop(0)
    if os.path.isdir(dir):
        # Add the contents.
        try:
            dirs.extend(map(lambda x: os.path.join(dir, x), os.listdir(dir)))
        except PermissionError:
            pass
    else:
        # If it's a .gif, print it
        if fnmatch.fnmatch(dir, '*.png'):
            print(dir)
