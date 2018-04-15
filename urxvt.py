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

       ▄• ▄▌    ▄▄▄      ▐▄• ▄      ▌ ▐·    ▄▄▄▄▄ 
       █▪██▌    ▀▄ █·     █▌█▌▪    ▪█·█▌    •██  
       █▌▐█▌    ▐▀▀▄      ·██·     ▐█▐█•     ▐█.▪
       ▐█▄█▌    ▐█•█▌    ▪▐█·█▌     ███      ▐█▌
        ▀▀▀     .▀  ▀    •▀▀ ▀▀    . ▀       ▀▀▀ 

         1.          2.          3.           4. 
     _____________________________________________
    |                                             |
    | RANDOM | LIST THEMES | CHOOSE THEME |  FONT |
    |_____________________________________________|

"""


home = expanduser("~")
Xr = home + '/.Xresources'
theme_dir = home + '/.config/themite/themes/urxvt/'
#Function to swap colors
def theme_swap(t):
    f = open(Xr, 'r+')
    content = f.read()
    start = content.index('\n! special')
    end = content.index('\n! end-colors')
    config_colors = content[start:end]
    t = open(t, 'r+')
    tcontent = t.read()
    tstart = tcontent.index('\n! special')
    tend = tcontent.index('\n! end-colors')
    theme_colors = tcontent[tstart:tend]
    with open(Xr, 'r+') as swap:
        swap_content = swap.read()
        swap.seek(0)
        swap.truncate()
        swap.write(content.replace(config_colors, theme_colors))
#color block defined in .Xresources
#X = open(Xr, 'r+')
#content = X.read()
#start = content.index('\n! special')
#end = content.index('\n! end-colors')
#Xcolors = content[start:end]

subprocess.check_call(['clear'])

themite = input(splash)
if themite == "1":
    random = random.choice(os.listdir(home + '/.config/themite/themes/urxvt/'))
    theme_swap(theme_dir + random)
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
    theme_swap(choice)
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





