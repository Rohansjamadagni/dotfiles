#!/bin/bash
# baraction.sh for spectrwm status bar

## DISK
hdd() {
  hdd="$(df -h | awk 'NR==4{print $3 }')"
  dev="$(df -h | awk 'NR==8{print $3 }')"
  games="$(df -h | awk 'NR==10{print $3 }')"
  win="$(df -h | awk 'NR==9{print $3 }')"
  echo -e "OS: $hdd  DEV: $dev  GAMES: $games  WIN: $win"
}

## RAM
mem() {
  mem=`free | awk '/Mem/ {printf "%dM/%dM\n", $3 / 1024.0, $2 / 1024.0 }'`
  echo -e "RAM: $mem "
}

health() {
  hf=`curl -s "https://api.debank.com/portfolio/list?project_id=matic_aave&user_addr=0x76d71b4b89605cf4875e67e10b02dd0495206aa7" | jq '.data.portfolio_list[0].detail.health_rate'| cut -c -5`
  echo -e "AAVE: $hf"
}

## CPU
cpu() {
  read cpu a b c previdle rest < /proc/stat
  prevtotal=$((a+b+c+previdle))
  sleep 0.5
  read cpu a b c idle rest < /proc/stat
  total=$((a+b+c+idle))
  cpu=$((100*( (total-prevtotal) - (idle-previdle) ) / (total-prevtotal) ))
  echo -e "CPU: $cpu% "
}

## VOLUME
vol() {
    vol=`amixer get Master | awk -F'[][]' 'END{ print $4":"$2 }' | sed 's/on://g'`
    echo -e "VOL: $vol"
}

print_date(){
  cdate=`date +"%a %h %d [%H:%M]"`
  echo -e "$cdate"
}

gpu_usage() {
    gpu_usage=`nvidia-smi --query-gpu=utilization.gpu --format=csv,nounits | awk '/[0-9]/ {print $1}' `
    echo -e "GPU: $gpu_usage%"
}
gpu_mem_usage() {

    gpu_mem_usage=` nvidia-smi --query-gpu=memory.used,memory.total --format=csv,nounits | awk '/[0-9]/ {printf "%dM/%dM",$1,$2}'`
    echo -e "VRAM: $gpu_mem_usage"
}
SLEEP_SEC=3
#loops forever outputting a line every SLEEP_SEC secs

# It seems that we are limited to how many characters can be displayed via
# the baraction script output. And the the markup tags count in that limit.
# So I would love to add more functions to this script but it makes the 
# echo output too long to display correctly.
while :; do
  echo "$(health)  | +@fg=1; +@fn=1;+@fn=0; $(cpu) $(gpu_usage)+@fg=0; | +@fg=2; +@fn=1;+@fn=0; $(mem) $(gpu_mem_usage) +@fg=0;| +@fg=3; +@fn=1;+@fn=0; $(hdd) +@fg=0; | +@fg=4; +@fn=1;+@fn=0; $(vol) +@fg=0; | $(print_date) "
	sleep $SLEEP_SEC
done

