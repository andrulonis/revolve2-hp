#!/bin/bash

study="default_study"
mainpath="honours2021"                   #TODO: absolute filepath
mkdir /home/${mainpath}/${study};
screen -d -m -S run_loop -L -Logfile /home/${mainpath}/${study}/setuploop.log ./experiments/${study}/setup-experiments.sh;