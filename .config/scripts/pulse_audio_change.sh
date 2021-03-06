#!/usr/bin/env bash

sinks=($(pacmd list-sinks | grep index | \
    awk '{ if ($1 == "*") print "1",$3; else print "0",$2 }'))
inputs=($(pacmd list-sink-inputs | grep index | awk '{print $2}'))

[[ ${sinks[0]} = 0 ]] && swap=${sinks[1]} || swap=${sinks[3]}

echo $swap
pacmd set-default-sink $swap &> /dev/null
for i in ${inputs[*]}; do pacmd move-sink-input $i $swap &> /dev/null; done
