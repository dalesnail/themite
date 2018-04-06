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


# Clear the terminal
subprocess.check_call(['clear'])

# No place like ~/
home = expanduser("~")

# Current termite config file
config = home + '/.config/termite/config'

# Choose a random termite config
theme = random.choice(os.listdir(home + '/.config/termite/themes/'))

# Themite Main choices area
themite = input(splash)

if themite == "1":
    # Copy the random config file into the correct config location
    copyfile(home + '/.config/termite/themes/' + theme, config) 

elif themite == "2":
    List = os.listdir(home + '/.config/termite/themes')
    for filename in List:
        m = re.search('(?<=config.)\w+', filename)
        if m:
            print(m.group(0))

elif themite == "3":
    List = os.listdir(home + '/.config/termite/themes')
    for filename in List:
        m = re.search('(?<=config.)\w+', filename)
        if m:
            print(m.group(0) + 
                   " ")
    Choice = input("Theme: ")
    copyfile(home + '/.config/termite/themes/config.' + Choice, config)

elif themite == "4":
    font = input("Font '<font name> <font size>': ")
    lines = open(config).read().splitlines()
    lines[9] = "font = " + font
    open(config, 'w').write('\n'.join(lines))

# Use subprocess to run the reload command
subprocess.check_call(['killall', '-USR1', 'termite'])
