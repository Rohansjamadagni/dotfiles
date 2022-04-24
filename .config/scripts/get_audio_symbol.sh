#! /usr/bin/env bash

SINK=$(pactl info | grep 'Default Sink' | cut -d':' -f 2 | cut -d '.' -f2 | cut -d '-' -f1)

if [[ $SINK == "usb" ]]; then
  echo "H"
else
  echo "S"
fi
