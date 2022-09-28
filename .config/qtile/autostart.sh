#!/usr/bin/env bash 
lxsession &
feh --bg-fill   ~/Pictures/wall4.jpg
nm-applet &
picom -b --config .config/spectrwm/picom.conf --experimental-backend
flameshot &
setxkbmap -option caps:swapescape &
xset r rate 200 50
