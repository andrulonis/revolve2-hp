#!/bin/bash
#set -e
#set -x

study=$(python3 experiments/default_study/get_param.py --get_default study_name)"
# arrays delimiter is space
experiments="$(python3 experiments/default_study/get_param.py --get_default experiment_name)"
runs=$(python3 experiments/default_study/get_param.py --get_default total_runs)"
mainpath=$(python3 experiments/default_study/get_param.py --get_default mainpath)"

# discover unfinished experiments

to_do=()
for i in $(seq $runs)
do
    run=$(($i))

    for experiment in "${experiments[@]}"
    do

     printf  "\n${experiment}_${run} \n"
     file="/home/${mainpath}/${study}/${experiment}_${run}.log";

     #check experiments status
     if [[ -f "$file" ]]; then

            lastgen=$(grep -c "Finished generation" $file);
            echo " latest finished gen ${lastgen}";

     else
         # not started yet
         echo " None";
     fi

    done
done
