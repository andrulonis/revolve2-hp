#!/bin/bash
##example of how to get a config.py parameter in a bash script

CONFIG_VAR="$(python3 experiments/default_study/get_param.py --get_default control_frequency)"
echo "${CONFIG_VAR}"

