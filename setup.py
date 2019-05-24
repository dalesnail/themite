#!/usr/bin/env python

import os
import sys
import stat


def make_executable(run):
    mode = os.stat(run).st_mode
    mode|= (mode & 0o444) >> 2
    os.chmod(run, mode)

mitepath = os.getcwd()
run = "/usr/local/bin/themite"

#Create file in runpath
f = open(run,"w+")
f.write(F"""#!/bin/sh
python {mitepath}/themite.py""")
f.close()

#Make executable
make_executable(run)
