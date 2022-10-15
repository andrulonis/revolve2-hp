#!/bin/bash

# delimiter is comma, example:
#experiments="exp1,epx2"
# exps order is the same for all params

experiments=("defaultexperiment")                        #TODO: absolute filepath

# these params are the same for all exps
# gens for boxplots and snapshots
generations=(1)
#gen for lineplots
final_gen=1
runs=1                               #TODO; was 10
mainpath="honours2021"               #TODO: absolute filepath
study="default_study"                        #TODO: absolute filepath

python experiments/${study}/snapshots_bests.py $study $experiments $runs $generations $mainpath;
python experiments/${study}/bests_snap_2d.py $study $experiments $runs $generations $mainpath;
python experiments/${study}/consolidate.py $study $experiments $runs $final_gen $mainpath;
python experiments/${study}/plot_static.py $study $experiments $runs $generations $mainpath;
