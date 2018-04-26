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
#constants

#home directory
home = expanduser("~")  

#config directory
config = home + '/.config/termite/config' 

#get the current theme for printing

#random theme selected
theme = random.choice(os.listdir(home + '/.config/themite/themes/termite/')) #random theme selected

#Function for theme swapping
def theme_swap(t):
    #open the existing config file
    f = open(config, 'r+')
    content = f.read()

    #grab the index range of the relevant part (the colors)
    start = content.index('[colors]')
    config_colors = content[start:]

    #opens the theme they selected
    t = open(t, 'r+')
    currentTheme = t.name[(t.name.index("config.") + 7):]
    tcontent = t.read()
    tstart = tcontent.index('[colors]')
    theme_colors = tcontent[tstart:]

    #with block to open and close the existing config file
    with open(config, 'r+') as swap:
        #remove the existing color options
        swap_content = swap.read()
        swap.seek(0)
        swap.truncate()
        #write the new theme colors onto the file
        swap.write(content.replace(config_colors, theme_colors))

    return currentTheme

#created method so it can be called again when asking to list the themes
def main():
    #clear the screen, and print out the splash
    subprocess.check_call(['clear'])
    #themite = input(splash + "\nCurrent theme: " + currentTheme)
    themite = input(splash)

    #handle each case
    if themite == "1":
        #get the theme dir, and append the randomly selected theme to create the path
        #call the theme_swap method on newly created path
        theme_dir = home + '/.config/themite/themes/termite/'
        #clear the screen, and call the color.sh script
        subprocess.check_call(['clear'])
        subprocess.call('~/.config/themite/color.sh', shell=True)
        print("Current theme: " + theme_swap(theme_dir + theme))


    elif themite == "2":
        #get the list of all the themes in the termite folder
        List = os.listdir(home + '/.config/themite/themes/termite/')
        print("\n")

        #for each file, print out the part after 'config.', which should be the name
        for filename in List:
            m = re.search('(?<=config.)\w+', filename)
            if m:
                print(m.group(0))
        temp = input("\nPress ENTER to continue")
        main()

    elif themite == "3":
        #get the list of all the themes in the termite folder
        List = os.listdir(home + '/.config/themite/themes/termite/')
        
        #print out the name of the themes
        for filename in List:
            m = re.search('(?<=config.)\w+', filename)
            if m:
                print(m.group(0))

        #take user input and give it as an argument for the theme swap method
        theme_dir = home + '/.config/themite/themes/termite/'
        theme_swap(theme_dir + "config." + input("Theme: "))
        #reset the terminal so changes occur immediately, and run color script
        subprocess.check_call(['clear'])
        subprocess.call('~/.config/themite/color.sh', shell=True)
    
    elif themite == "4":
        #feel like this part can be improved somewhat - maybe provide a list of the system installed fonts?
        font = 'font = '
        new_font = "font = " + input('Font <Name> <Size>:')
        x = fileinput.input(files=config, inplace=1)
        for line in x:
            if font in line:
                line = new_font
            print(line.strip())
        x.close()
    #Display current theme

main()

#exit from termite, and reopen
subprocess.check_call(['killall', '-USR1', 'termite'])
