#!/usr/bin/env python

import os
from os.path import expanduser
import random
from shutil import copyfile
import subprocess

'''
Create the dir ~/.config/termite/themes and place some random configs into it
Run this script via: python random_termite_theme.py
Enjoy!
'''

# No place like ~/
home = expanduser("~")

# Current termite config file
config = home + '/.config/termite/config'

# Choose a random termite config
theme = random.choice(os.listdir(home + '/.config/termite/themes/'))

# Themite Main choices area
themite = input("1. Random 2. List Themes 3. Choose Theme [1/2/3]: ")

if themite == "1":
    # Copy the random config file into the correct config location
    copyfile(home + '/.config/termite/themes/' + theme, config) 

elif themite == "2":
    List = os.listdir(home + '/.config/termite/themes')
    for file in List:
        print(file)

elif themite == "3":
    Choice = input("Theme: ")
    copyfile(home + '/.config/termite/themes/' + Choice, config)

# Use subprocess to run the reload command
subprocess.check_call(['killall', '-USR1', 'termite'])
