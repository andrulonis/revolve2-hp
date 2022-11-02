#!/bin/bash

#[HP] run this if you want to run the experiment in the background

study="$(python3 experiments/default_study/get_param.py --get_default study_name)"
mainpath="$(python3 experiments/default_study/get_param.py --get_default mainpath)"
mkdir -p /home/${mainpath}/${study};

##BACKGROUND
screen -d -m -S run_loop_${study}_$(date +%F_%T) -L -Logfile /home/${mainpath}/${study}/logs/setuploop.log ./experiments/${study}/setup-experiments.sh
echo "running experiments in background. See progress in /home/${mainpath}/${study}/logs/"

##FOREGROUND
#screen -m -S run_loop -L -Logfile /home/${mainpath}/${study}/logs/setuploop.log ./experiments/${study}/setup-experiments.sh;