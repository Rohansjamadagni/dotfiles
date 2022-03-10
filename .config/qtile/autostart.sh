#!/usr/bin/env bash 
lxsession &
feh --bg-fill Pictures/wall2.jpg
/usr/bin/emacs --daemon &
picom -b
ulauncher &
nm-applet &
conky -c ~/.config/conky/doomone-qtile.conkyrc &
conky -c ~/.config/conky/doomone-qtile-right.conkyrc &
setxkbmap -option caps:escape
