#!/usr/bin/env bash 
lxsession &
feh --bg-fill Pictures/wall2.jpg
/usr/bin/emacs --daemon &
picom -b
ulauncher &
nm-applet &
