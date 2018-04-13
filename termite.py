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
# Defining color block in config
f = open(home + '/.config/termite/config', 'r+')
content = f.read()
start = content.index('\n[colors]')
end = content.index('\n[end-colors]')
config_colors = content[start:end]


subprocess.check_call(['clear'])

themite = input(splash)
if themite == "1":
    theme_dir = home + '/.config/themite/themes/termite/'
    #Defining color block in theme
    r = open(theme_dir + theme, 'r+')
    r_content = r.read()
    r_start = r_content.index('\n[colors]')
    r_end = r_content.index('\n[end-colors]') 
    random = r_content[r_start:r_end]
    with open(config, 'r+') as r:
        r_content = r.read()
        r.seek(0)
        r.truncate()
        r.write(content.replace(config_colors, random))
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
    Choice = theme_dir + input("Theme: ")
    #Defining color block in theme
    t = open(Choice, 'r+')
    t_content = t.read()
    t_start = t_content.index('\n[colors]')
    t_end = t_content.index('\n[end-colors]')
    theme = t_content[t_start:t_end]

    with open(home + '/.config/termite/config', 'r+') as c:
        content = c.read()
        c.seek(0)
        c.truncate()
        c.write(content.replace(config_colors, theme))
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
