#!/usr/bin/env python

import subprocess
import os
from os.path import expanduser

splash = """

        TEST TEST

        1 = Termite
        2 = URXVT

"""

home = expanduser("~")
urxvt = '/usr/bin/urxvt'
termite = f'{home}/.config/termite/'

if os.path.exists(urxvt) == True and os.path.exists(termite) == False:
    os.system('python urxvt.py')

elif os.path.exists(termite) == True and os.path.exists(urxvt) == False:
    os.system('python termite.py')

elif os.path.exists(termite) == True and os.path.exists(urxvt) == True:
    Choose = input(splash)
    if Choose == '1':
        os.system('python termite.py')

    elif Choose == '2':
        os.system('python urxvt.py')
