#!/bin/bash

#[HP] run this if you want to run the experiment in the background

study="$(python3 experiments/default_study/get_param.py --get_default study_name)"
mainpath="$(python3 experiments/default_study/get_param.py --get_default mainpath)"
output_path="$(python3 experiments/default_study/get_param.py --get_default output_path)"
printf "output_path = ${output_path}\n"
mkdir -p ${mainpath}/${study};

##BACKGROUND
screen -d -m -S run_loop_${study}_$(date +%F_%T) -L -Logfile ${output_path}/${study}/setuploop.log ./experiments/${study}/setup-experiments.sh
echo "running experiments in background. See progress in ${output_path}/${study}"

##FOREGROUND
#screen -m -S run_loop_${study}_$(date +%F_%T) -L -Logfile ${output_path}/${study}/setuploop.log ./experiments/${study}/setup-experiments.sh