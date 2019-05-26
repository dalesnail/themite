#!/usr/bin/env python

import os
from os.path import expanduser


home = expanduser("~")
cwd = os.getcwd()
src = f'{cwd}/themite.py'
dest = '/usr/local/bin/themite'

os.symlink(src, dest)
