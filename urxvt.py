#!/usr/bin/env python

import os
from os.path import expanduser
import random
import subprocess
import re
import sys
import fileinput
import signal

'''
Creating URXVT version of themite, this will be a WIP
Note: this does change the colors section and the fonts section of .Xresources
NOT .Xdefaults

Color blocks in both the .Xresources file, and your themes will have to end with "! end-colors"

'''

splash = """\

        URXVT

        1.          2.          3.           4. 
    ________________________________________________
   |                                                |
   | RANDOM   LIST THEMES   CHOOSE THEME    FONT    |
   |________________________________________________|

"""


home = expanduser("~")
Xr = home + '/.Xresources'
theme_dir = home + '/.config/themite/themes/urxvt/'
#color block defined in .Xresources
X = open(Xr, 'r+')
content = X.read()
start = content.index('\n! special')
end = content.index('\n! end-colors')
Xcolors = content[start:end]

#subprocess.check_call(['clear'])

themite = input(splash)
if themite == "1":
    random = random.choice(os.listdir(home + '/.config/themite/themes/urxvt/'))
    r = open(home + '/.config/themite/themes/urxvt/' + random, 'r+')
    r_content = r.read()
    r_start = r_content.index('\n! special')
    r_end = r_content.index('\n! end-colors')
    r_colors = r_content[r_start:r_end]
    #print(r_colors)
    with open(Xr, 'r+') as r:
        r.seek(0)
        r.truncate()
        r.write(content.replace(Xcolors, r_colors))
    subprocess.call('xrdb ~/.Xresources', shell=True)
    print('Random theme is now applied! Restart URXVT to see your changes!')

elif themite == "2":
    List = os.listdir(theme_dir)
    for filename in List:
        m = re.search('(?<=.Xresources.)\w+', filename)
        if m:
            print(m.group(0))

elif themite == "3":
    List = os.listdir(theme_dir)
    for filename in List:
        m = re.search('(?<=.Xresources.)\w+', filename)
        if m:
            print(m.group(0))
    choice = theme_dir + '.Xresources.' + input("Theme: ")
    t = open(choice, 'r+')
    t_content = t.read()
    t_start = t_content.index('\n! special')
    t_end = t_content.index('\n! end-colors')
    t_colors = t_content[t_start:t_end]
    with open(Xr , 'r+') as c:
        content = c.read()
        c.seek(0)
        c.truncate()
        c.write(content.replace(Xcolors, t_colors))
    subprocess.call('xrdb ~/.Xresources', shell=True)
    print('Theme is now applied! Restart URXVT to see your changes!')

elif themite == "4":
    font = 'URxvt.font: xft:'
    newfont = font + input('Font: ') + ':size=' + input('Size: ')
    x = fileinput.input(files=Xr, inplace=1)
    for line in x:
        if font in line:
            line = newfont
        print(line.strip())
    x.close()
    subprocess.call('xrdb ~/.Xresources', shell=True)
    print('New Font is now applied! Restart URXVT to see your changes!')





