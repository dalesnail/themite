#!/usr/bin/env python

import os
from os.path import expanduser
import random
import subprocess
import re
import sys
import fileinput

'''                                                                          
Create the dir ~/.config/termite/themes and place some random configs into it
Run this script via: python termite.py                          
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
theme = random.choice(os.listdir(home + '/.config/themite/themes/termite/'))
#Function for theme swapping
def theme_swap(t):
    f = open(config, 'r+')
    content = f.read()
    start = content.index('\n[colors]')
    end = content.index('\n[end-colors')
    config_colors = content[start:end]
    t = open(t, 'r+')
    tcontent = t.read()
    tstart = tcontent.index('\n[colors]')
    tend = tcontent.index('\n[end-colors]')
    theme_colors = tcontent[tstart:tend]
    with open(config, 'r+') as swap:
        swap_content = swap.read()
        swap.seek(0)
        swap.truncate()
        swap.write(content.replace(config_colors, theme_colors))


subprocess.check_call(['clear'])
themite = input(splash)
if themite == "1":
    theme_dir = home + '/.config/themite/themes/termite/'
    theme_swap(theme_dir + theme)
    subprocess.check_call(['clear'])
    subprocess.call('~/.config/themite/color.sh', shell=True)

elif themite == "2":
    List = os.listdir(home + '/.config/themite/themes/termite/')
    for filename in List:
        m = re.search('(?<=config.)\w+', filename)
        if m:
            print(m.group(0))

elif themite == "3":
    List = os.listdir(home + '/.config/themite/themes/termite/')
    for filename in List:
        m = re.search('(?<=config.)\w+', filename)
        if m:
            print(m.group(0))
    theme_dir = home + '/.config/themite/themes/termite/config.'
    theme_swap(theme_dir + input("Theme: "))
    subprocess.check_call(['clear'])
    subprocess.call('~/.config/themite/color.sh', shell=True)

elif themite == "4":
    font = 'font = '
    new_font = "font = " + input('Font <Name> <Size>:')
    x = fileinput.input(files=config, inplace=1)
    for line in x:
        if font in line:
            line = new_font
        print(line.strip())
    x.close()

subprocess.check_call(['killall', '-USR1', 'termite'])
