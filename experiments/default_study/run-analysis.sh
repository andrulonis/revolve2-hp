#!/bin/bash

# delimiter is comma, example:
#experiments="exp1,epx2"
# exps order is the same for all params

experiments="$(python3 experiments/default_study/get_param.py --get_default experiment_name)"

# these params are the same for all exps
# gens for boxplots and snapshots
generations="$(python3 experiments/default_study/get_param.py --get_default num_generations)"
#gen for lineplots
final_gen="$(python3 experiments/default_study/get_param.py --get_default num_generations)"
runs="$(python3 experiments/default_study/get_param.py --get_default total_runs)"
mainpath="$(python3 experiments/default_study/get_param.py --get_default mainpath)"
study="$(python3 experiments/default_study/get_param.py --get_default study_name)"
output_path="$(python3 experiments/default_study/get_param.py --get_default output_path)"

#experiments="flat,icy,rugged,sine,slope,step"    #HP: optional manual experiment selection (no build required)

echo "[generating best snapshots...]"
python3 experiments/${study}/snapshots_bests.py $study $experiments $runs $generations $output_path;

echo "[generating best 2D snapshots...]"
python3 experiments/${study}/bests_snap_2d.py $study $experiments $runs $generations $output_path;

echo "[running consolidate.py...]"
python3 experiments/${study}/consolidate.py $study $experiments $runs $final_gen $output_path;

echo -e "\n[plotting static plots (no max)...]"
python3 experiments/${study}/plot_static.py $study $experiments $runs $generations $output_path 0;  #without max
echo -e "\n[plotting static plots (max)...]"
python3 experiments/${study}/plot_static.py $study $experiments $runs $generations $output_path 1;   #with max

echo "[making video recording...]"
./experiments/${study}/makevideos.sh

echo "[DONE ANALYSING!]"