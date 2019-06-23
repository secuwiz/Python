#!/usr/bin/python3

# The os.path module has operations for manipulating file name paths
# for whaterver system you're running on.
from os.path import *

for fn in [ '/', '/home/bennet', 'path.py', '/var/log/messages', 'bogus' ]:
    print('%-15s' % fn + ':',end=' ')

    # Don't forget: These operations are os.path.whatever.

    # Is it there?
    if exists(fn):
        print('exists,',end=' ')
    else:
        print('nonexistent')
        print()
        continue

    # Absolute path?
    if isabs(fn):
        print('absolute,',end=' ')
        print('directory', dirname(fn)+',', 'base', basename(fn)+',')
        print(' ' * 16,end=' ')
    else:
        print('relative,',end=' ')

    # What sort of thing is it?
    if isfile(fn): print('plain file,',end=' ')
    elif isdir(fn): print('directory,',end=' ')
    else: print('strange,',end=' ')

    # Extension.
    print('extension', splitext(fn)[1]+',',end=' ')

    # Size
    print(getsize(fn), 'bytes.')

    print()
