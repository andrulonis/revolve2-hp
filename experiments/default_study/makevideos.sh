#!/bin/bash

#ONLY WORKS IF YOU HAVE 1 MONITOR

study="$(python3 experiments/default_study/get_param.py --get_default study_name)"
mainpath="$(python3 experiments/default_study/get_param.py --get_default mainpath)"
WIDTH=$(xrandr --current | grep '*' | uniq | awk '{print $1}' | cut -d 'x' -f1)
HEIGHT=$(xrandr --current | grep '*' | uniq | awk '{print $1}' | cut -d 'x' -f2)
file="/home/${mainpath}/${study}/analysis/video_bests.mpg";
rm $file

printf " \n making video...\n"
screen -d -m -S HP_videos ffmpeg -video_size "${WIDTH}"x"${HEIGHT}" -f x11grab -r 25 -i "$DISPLAY" -qscale 0 $file
printf "starting python visualization scripts\n"
#python3 experiments/${study}/watch_robots.py
sleep 5
killall screen
printf "\n finished video!"

