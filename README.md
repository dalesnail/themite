<div align="center">
  <img src="https://raw.githubusercontent.com/dalesnail/themite/master/title.png"><br>
  Automated customization for termite and urxvt
</div>

# Update
This is now working as it should with xst, if you have any issues let me know and I will do my best to update this. 

# Install

- `git clone https://github.com/dalesnail/themite.git` into ~/.config

- `cd ~/.config/themite`

- `sudo python setup.py`

__Important__

- Make sure your termite config is stored at "/.config/termite/config", and your themes are stored in ~/.config/themite/themes/"Whatever terminal you use", __WILL NOT__ work in other config locations unless you edit the python script. I am working to make this more universal, but for now stick with this format. 

- I have set it up recently to be able to replace only colors with theme swaps, to keep fonts and other non color elements constant. But note, for URXVT color blocks in both Xresources and themes need to begin with "! special" and end with "! end-colors". In termite your color block should begin with "[colors]"

- Theme files names should be formatted as "config.themename" for termite, and ".Xresources.themename" for URXVT


# Usage

After install, just type in `themite` and you will be presented with options to use

Arguments have been added to the script here to make for quicker theme swapping. 

- '-h' - This will bring up a full list of avaliable arguments to use themite as a CLI program.

- -ttheme, -utheme, and -xstheme - This will change the theme for termite(-ttheme), URXVT(utheme), and xst(xstheme) if you use "Random" a random theme will be chosen. Format: 'themite -ttheme "ProfileName"'

- -list - This will list the available themes, t for termite, u for URXVT, and x for xst. e.g. "themite -list t"

- -font - this will put you into the prompt for a new font, x for xst, u for......yadda yadda you get it at this point. e.g. "themite -font t"

Enjoy!

----------------------------------------------------------------------------------------------

![Demo](demo.gif)
