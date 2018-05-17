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

splash = f"""\

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

#fonts director
fonts_dir = "/usr/share/fonts/"

#random theme selected
theme = random.choice(os.listdir(home + '/.config/themite/themes/termite/'))

#Function for theme swapping
def theme_swap(t):
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
        swap.write(content.replace(config_colors, theme_colors) + "\n#" + currentTheme)

    return currentTheme

#method to print out fonts
def print_fonts():
    #gets the output of the command 'fc-list' which lists all the fonts installed
    fonts = subprocess.run(['fc-list'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    #split it on each newline
    fonts = fonts.split("\n")

    #loop thru each font, and grabbing the important part (its name)
    for font in fonts:
        #makes sure its a valid entry in the list
        if len(font) > 3:
            #some fonts have commas and show up weird, so we append fix those here
            if "," in font:
                font = font[font.index(",") + 1:]
                #some of those fonts with commas also have colons so we fix that here
                if ':' in font:
                    font = font[:font.index(":")]   
            #otherwise, we just grab the part in between the colons and print it out 
            else:
                font = font[font.index(":") + 2:]
                font = font[:font.index(":")]   
            print(font)
 
def print_themes():
    #creates list of themes
    List = os.listdir(home + '/.config/themite/themes/termite/')

    #loops thru list, and prints out the name of the theme
    for filename in List:
        m = re.search('(?<=config.)\w+', filename)
        if m:
            print(m.group(0))

def main():
    #clear screen
    subprocess.check_call(['clear'])
    
    #get current theme installed
    current = open(config, "r")
    lineList = current.readlines()
    current.close()
    currentTheme = lineList[len(lineList) - 1]
    currentTheme = currentTheme[1:]    
    
    #get the current font
    currentFont = ""

    #loops thru already exising lineList and gets the necessary line
    for line in lineList:
        if "font" in line:
            currentFont = line[line.index("=") + 1:] 
        

    #print out splash, current theme, and current font
    themite = input(splash + "\tCurrent theme: " + currentTheme + "\n\tCurrent Font: " + currentFont + "\n" )

    #Random
    if themite == "1":
        #get the theme dir, append the randomly selected theme and create path
        theme_dir = home + '/.config/themite/themes/termite/'
        #clear the screen, and call the color.sh script
        subprocess.check_call(['clear'])
        subprocess.call('~/.config/themite/color.sh', shell=True)
        print("\tRandom theme: " + theme_swap(theme_dir + theme) + "\n")

    #List
    elif themite == "2":
        print_themes()
        temp = input("\nPress ENTER to continue")
        main()

    #Choose theme
    elif themite == "3":
        #prints the themes
        print_themes()

        #take user input and give it as an argument for the theme swap method
        theme_dir = home + '/.config/themite/themes/termite/config.'

        #reset the terminal so changes occur immediately, and run color script
        theme_swap(theme_dir + input("Theme: "))
        subprocess.check_call(['clear'])
        subprocess.call('~/.config/themite/color.sh', shell=True)
    
    elif themite == "4":
        #prints fonts
        print_fonts() 
        
        #takes user input
        font = 'font = '
        new_font = "font = " + input('Font <Name> <Size>: ')
        
        #open the config file and replace the proper line
        current = open(config, "r+")
        lines = current.readlines()
        current.close()

        #checks if an options menu is present
        has_options = "[options]\n" in lines

        if has_options:
            #reopens the file in write mode
            current = open(config, "w")

            #copies over the file, replacing the one font line
            for line in lines:
                if "font = " in line:
                    current.write(new_font + "\n")
                else:
                    current.write(line)
        else:
            #reopens the file in write mode
            current = open(config, "w")

            #manually add the options section with the new font
            current.write("[options]\n" + new_font + "\n")
            
            #copies over everything 
            for line in lines:
                current.write(line)

        subprocess.check_call(['clear'])
        subprocess.call('~/.config/themite/color.sh', shell=True)
        print("\tCurrent theme: " + currentTheme + "\n\tCurrent Font: " + currentFont + "\n")


#run main method  
main()

#exit from termite, and reopen
subprocess.check_call(['killall', '-USR1', 'termite'])
