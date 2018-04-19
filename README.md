<div align="center">
  <img src="https://raw.githubusercontent.com/dalesnail/themite/master/title.png"><br>
  Theme chooser / randomizer for Termite terminal
</div>

# Update
Updated this to work with URXVT. This is a trial for now, but it seems to be working as it should. Only difference from termite being you have to restart after setting the theme. 

If you only have one or the other installed, it should run the appropriate script for the installed program. 

In the unlikely event both are installed it will prompt you to choose which one to change. 

-----------------------------------------------

- Git clone or copy into '~/.config/'.

- Run with 'python ~/.config/themite/themite.py'. 

- Make a bash alias for this, pretty annoying to type in otherwise. 

__#Important#__

- Make sure your themes for termite are stored in ~/.config/themite/themes/termite/, __WILL NOT__ work in other termite config locations unless you edit the python script. 

- I have set it up recently to be able to replace only colors with theme swaps, to keep fonts and other non color elements constant. But note, your color blocks will have to begin with "[colors]", and end with "[end-colors]" for termite, and for URXVT they will need to begin with "! special" and end with "! end-colors".

- Theme files names should be formatted as "config.themename" for termite, and ".Xresources.themename" for URXVT


__Usage__

Arguments have been added to the script here to make for quicker theme swapping. 

- -ttheme and -utheme - This will change the theme for termite(-ttheme) and URXVT(utheme), if you use "Random" a random theme will be chosen. Format: 'themite -ttheme <ProfileName>

- -list - This will list the available themes, t for termite u for URXVT. Eg: "themite -list t"

- -font - this will put you into the prompt for a new font, same as above, t for termite u for urxvt. eg: "themite -font t"

Enjoy!

----------------------------------------------------------------------------------------------

![Demo](demo.gif)
