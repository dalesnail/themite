#!/usr/bin/env python

import os
from os.path import expanduser
import random
from shutil import copyfile
import subprocess
import re

'''                                                                          
Create the dir ~/.config/termite/themes and place some random configs into it
Run this script via: python random_termite_theme.py                          
Enjoy!                                                                       
'''                                                                          

splash = """\

       ▄▄▄▄▄▄     ▄ .▄    ▄▄▄ .    • ▄   ▄▄ ·.   ▀    ▄▄▄▄▄▄    ▄▄▄ .
        •██ ·    ██ ▐█    █ .▀·    ·██▄▐███ ▪   ██     •██      ▀▄.▀·
      ·  ▐█.▪·   ██▄ █  · █▀▀      ▐█ █▐▌▐█·    ▐█·   █ ▐█      █▀▀ ▄
       · ▐█▌·    █  ▐█    █ ▄▄▌ ·  ██ ██▌▐█▌ ·  ▐█▌     ▐█▌·    ▐█▄▄▌  ·
         ▀▀▀     ▀   █    █▀▀▀     ▀▀  █ ▀▀▀    ▀▀▀  ·  ▀▀▀  ·  ·  ·  

             1.              2.                3.                4. 
        _______________________________________________________________ 
       |                                                               |
      |   RANDOM   |   LIST THEMES   |   CHOOSE THEME   |  CHANGE FONT  |
       |_______________________________________________________________|

"""


home = expanduser("~")
config = home + '/.config/termite/config'
theme = random.choice(os.listdir(home + '/.config/termite/themite/themes/'))


subprocess.check_call(['clear'])

themite = input(splash)
if themite == "1":
    copyfile(home + '/.config/termite/themite/themes/' + theme, config) 

elif themite == "2":
    List = os.listdir(home + '/.config/termite/themite/themes')
    for filename in List:
        m = re.search('(?<=config.)\w+', filename)
        if m:
            print(m.group(0))

elif themite == "3":
    List = os.listdir(home + '/.config/termite/themite/themes')
    for filename in List:
        m = re.search('(?<=config.)\w+', filename)
        if m:
            print(m.group(0))
    Choice = input("Theme: ")
    copyfile(home + '/.config/termite/themite/themes/config.' + Choice, config)
    subprocess.check_call(['clear'])
    subprocess.call('~/.config/termite/themite/color.sh', shell=True)

elif themite == "4":
    font = input("Font '<font name> <font size>': ")
    lines = open(config).read().splitlines()
    lines[9] = "font = " + font
    open(config, 'w').write('\n'.join(lines))

subprocess.check_call(['killall', '-USR1', 'termite'])
