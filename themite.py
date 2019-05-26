#!/usr/bin/env python

import argparse
import sys
import subprocess
import os
from os.path import expanduser
import random
import re
import fileinput

splash = """

        T H E M I T E
      -----------------  
1. TERMITE  2. URXVT  3. XST

"""

home = expanduser("~")
urxvt = os.path.exists('/usr/bin/urxvt')
termite = os.path.exists(f'{home}/.config/termite/')
xst = os.path.exists('/usr/bin/xst')
t_random = random.choice(os.listdir(home + '/.config/themite/themes/termite/'))
u_random = random.choice(os.listdir(home + '/.config/themite/themes/urxvt/'))
x_random = random.choice(os.listdir(home + '/.config/themite/themes/xst/'))
t_config = f'{home}/.config/termite/config'
x_config = f'{home}/.Xresources'

def termite_swap(t):
    f = open(t_config, 'r+')
    content = f.read()
    start = content.index('[colors]')
    config_colors = content[start:]
    termthem = open(t, 'r+')
    t = termthem.read()
    tstart = t.index('[colors]')
    theme_colors = t[tstart:]
    with open(t_config, 'r+') as swap:
        swap_content = swap.read()
        swap.seek(0)
        swap.truncate()
        swap.write(content.replace(config_colors, theme_colors))
    subprocess.check_call(['killall', '-USR1', 'termite'])
    

def u_swap(u):
    f = open(x_config, 'r+')
    content = f.read()
    start = content.index('\n! special')
    end = content.index('\n! end-colors')
    config_colors = content[start:end]
    t = open(u, 'r+')
    tcontent = t.read()
    tstart = tcontent.index('\n! special')
    tend = tcontent.index('\n! end-colors')
    t_colors = tcontent[tstart:tend]
    with open(x_config, 'r+') as swap:
        swap_content = swap.read()
        swap.seek(0)
        swap.truncate()
        swap.write(content.replace(config_colors, t_colors))
    subprocess.call('xrdb ~/.Xresources', shell=True)
    print('Theme is now applied! Restart URXVT to see your changes!')

def x_swap(x):
    f = open(x_config, 'r+')
    content = f.read()
    start = content.index('\n! special')
    end = content.index('\n! end-colors')
    config_colors = content[start:end]
    t = open(x, 'r+')
    tcontent = t.read()
    tstart = tcontent.index('\n! special')
    tend = tcontent.index('\n! end-colors')
    t_colors = tcontent[tstart:tend]
    with open(x_config, 'r+') as swap:
        swap_content = swap.read()
        swap.seek(0)
        swap.truncate()
        swap.write(content.replace(config_colors, t_colors))
    subprocess.call('xrdb ~/.Xresources', shell=True)
    subprocess.check_call(['killall', '-USR1', 'xst'])
    

parser = argparse.ArgumentParser()
parser.add_argument('-ttheme', help='This will change the theme for Termite, just "-ttheme <ProfileName>" If you use -ttheme with "random" it will choose a random theme')
parser.add_argument('-list', help="This will list all available themes, t for termite, u for urxvt, x for xst. eg: themite -list t")
parser.add_argument('-font', help='This will put you into the prompt for font changes, same as before t for termite, u for urxvt, x for xst. eg: "themite -font t"')
parser.add_argument('-utheme', help='This will change the them for URXVT, just "-utheme <ProfileName>" If you use -utheme with "random" it will choose a random theme')
parser.add_argument('-xstheme', help='This will change the theme for xst, just "-xstheme <ProfileName>" You can use random for the argument, and it will pick a random theme')
args = parser.parse_args()

if args.ttheme:
    if args.ttheme == 'random':
        termite_swap(f'{home}/.config/themite/themes/termite/{t_random}')
    else:
        termite_swap(f'{home}/.config/themite/themes/termite/config.{args.ttheme}')

if args.utheme:
    if args.utheme == 'random':
        u_swap(f'{home}/.config/themite/themes/urxvt/{u_random}')
    else:
        u_swap(f'{home}/.config/themite/themes/urxvt/.Xresources.{args.utheme}')

if args.xstheme:
    if args.xstheme == 'random':
        x_swap(f'{home}/.config/themite/themes/xst/{x_random}')
    else:
        x_swap(f'{home}/.config/themite/themes/xst/.Xresources.{args.xstheme}')

if args.list:
    if args.list == 't':
        List = os.listdir(f'{home}/.config/themite/themes/termite/')
        for filename in List:
            m = re.search('(?<=config.)\w+', filename)
            if m:
                print(m.group(0))
    elif args.list == 'u':
        List = os.listdir(f'{home}/.config/themite/themes/urxvt/')
        for filename in List:
            x = re.search('(?<=.Xresources.)\w+', filename)
            if x:
                print(x.group(0))
    elif args.list == 'x':
        List = os.listdir(f'{home}/.config/themite/themes/xst/')
        for filename in List:
            s = re.search('(?<=.Xresources.)\w+', filename)
            if s:
                print(s.group(0))
    else:
        print("Nothing here!")

if args.font:
    if args.font == 't':
        font = 'font = '
        new_font = f'font = {input("Font <Name> <Size>:")}'
        x = fileinput.input(files=t_config, inplace=1)
        for line in x:
            if font in line:
                line = new_font
            print(line.strip())
        x.close()
        subprocess.check_call(['killall', '-USR1', 'termite'])
    elif args.font == 'u':
        font = 'URxvt.font: xft:'
        newfont = f"{font}{input('Font: ')}:size={input('Size: ')}"
        x = fileinput.input(files=x_config, inplace=1)
        for line in x:
            if font in line:
                line = newfont
            print(line.strip())
        x.close()
        subprocess.call('xrdb ~/.Xresources', shell=True)
        print('New font is now applied! Restart URXVT to see your changes!')
    elif args.font == 'x':
        font = 'st.font: '
        newfont = f"{font}{input('Font: ')}:size={input('Size: ')}:antialias=true:autohint=true;"
        x = fileinput.input(files=x_config, inplace=1)
        for line in x:
            if font in line:
                line = newfont
            print(line.strip())
        x.close()
        subprocess.call('xrdb ~/.Xresources', shell=True)
        subprocess.check_call(['killall', '-USR1', 'xst'])

   


if len(sys.argv)==1:
    if urxvt and not termite and not xst:
        os.system('python ~/.config/themite/urxvt.py')

    elif termite and not urxvt and not xst:
        os.system('python ~/.config/themite/termite.py')

    elif not termite and not urxvt and xst:
        os.system('python ~/.config/themite/xst.py')
   
 
    elif (not termite and urxvt and xst) or (termite and not urxvt and xst):
        subprocess.check_call(['clear'])
        Choose = input(splash)
        if Choose == '1':
            os.system('python ~/.config/themite/termite.py')

        elif Choose == '2':
            os.system('python ~/.config/themite/urxvt.py')

        elif Choose == '3':
            os.system('python ~/.config/themite/xst.py')

    elif not termite and not urxvt and not xst:
        print("!!!Could not find supported terminal!!!")
