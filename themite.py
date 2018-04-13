#!/usr/bin/env python

import subprocess
import os
from os.path import expanduser

splash = """

   ▄▄▄▄▄▄     ▄ .▄    ▄▄▄ .    • ▄   ▄▄ ·.   ▀    ▄▄▄▄▄▄    ▄▄▄ .
    •██ ·    ██ ▐█    █ .▀·    ·██▄▐███ ▪   ██     •██      ▀▄.▀·
  ·  ▐█.▪·   ██▄ █  · █▀▀      ▐█ █▐▌▐█·    ▐█·   █ ▐█      █▀▀ ▄
   · ▐█▌·    █  ▐█    █ ▄▄▌ ·  ██ ██▌▐█▌ ·  ▐█▌     ▐█▌·    ▐█▄▄▌  ·
     ▀▀▀     ▀   █    █▀▀▀     ▀▀  █ ▀▀▀    ▀▀▀  ·  ▀▀▀  ·  ·  ·                                        

                 1.                                    2.
  ___  ___  __          ___  ___                  __           ___ 
   |  |__  |__)  |\/| |  |  |__             |  | |__) \_/ \  /  |  
   |  |___ |  \  |  | |  |  |___            \__/ |  \ / \  \/   |

"""

home = expanduser("~")
urxvt = '/usr/bin/urxvt'
termite = f'{home}/.config/termite/'

if os.path.exists(urxvt) == True and os.path.exists(termite) == False:
    os.system('python ~/.config/themite/urxvt.py')

elif os.path.exists(termite) == True and os.path.exists(urxvt) == False:
    os.system('python ~/.config/themite/termite.py')

elif os.path.exists(termite) == True and os.path.exists(urxvt) == True:
    Choose = input(splash)
    if Choose == '1':
        os.system('python ~/.config/themite/termite.py')

    elif Choose == '2':
        os.system('python ~/.config/themite/urxvt.py')
