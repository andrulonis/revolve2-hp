#!/bin/bash

study="$(python3 experiments/default_study/get_param.py --get_default study_name)"
mainpath="$(python3 experiments/default_study/get_param.py --get_default mainpath)"
file="home/${mainpath}/${study}/analysis/video_bests.mpg";

printf " \n making video..."
screen -d -m -S videos ffmpeg -f x11grab -r 25 -i :1 -qscale 0 $file
python3 experiments/${study}/watch_robots.py
killall screen
printf " \n finished video!"

