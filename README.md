<div align="center">
  <img src="https://raw.githubusercontent.com/dalesnail/themite/master/title.png"><br>
  Theme chooser / randomizer for Termite terminal
</div>

-----------------------------------------------

- Git clone or copy into '~/.config/termite/'.

- Run with 'python ~/.config/termite/themite/themite.py'. 

- Make a bash alias for this, pretty annoying to type in otherwise. 

__#Important#__

- Make sure your themes are stored in ~/.config/termite/themite/themes, __WILL NOT__ work in other termite config locations unless you edit the python script. 

- I have set it up recently to be able to replace only colors with theme swaps, to keep fonts and other non color elements constant. But note, your color blocks will have to have the footer "[end-colors]" for this to work. 

- And again, because it has become so important to this script, __Begin your color section with [colors], and end your color sections with [end-colors]__

- Theme files names should be formatted as "config.themename"

Enjoy!

----------------------------------------------------------------------------------------------

![Demo](demo.gif)
