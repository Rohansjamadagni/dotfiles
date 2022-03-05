#!/usr/bin/env bash 
lxsession &
feh --bg-scale --no-xinerama  ~/Pictures/big10.jpg
/usr/bin/emacs --daemon &
killall ulauncher
ulauncher --no-window-shadow &
nm-applet &
conky -c ~/.config/conky/doomone-qtile.conkyrc &
conky -c ~/.config/conky/doomone-qtile-right.conkyrc &
picom -b --config .config/spectrwm/picom.conf --experimental-backend
flameshot &
