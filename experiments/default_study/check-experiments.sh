#!/bin/bash
#set -e
#set -x


study="default_study"                            #TODO: absolute filepath
# arrays delimiter is space
experiments=("defaultexperiment")                #TODO: absolute filepath
runs=10
mainpath="honours2021"              #TODO: absolute filepath

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
