#!/bin/bash
#set -e
#set -x

###[HP] run this if you want to run the experiment in the foreground

study="$(python3 experiments/default_study/get_param.py --get_default study_name)"

# DO NOT use underline ( _ ) in the experiments names
# delimiter is space, example:
#experiments=("exp1" "epx2")
# exps order is the same for all params

RESTART_ABORTED_EXPERIMENT=true
experiments="$(python3 experiments/default_study/get_param.py --get_default experiment_name)"
seasons_conditions="$(python3 experiments/default_study/get_param.py --get_default seasons_conditions)"
runs="$(python3 experiments/default_study/get_param.py --get_default total_runs)"
num_generations="$(python3 experiments/default_study/get_param.py --get_default num_generations)"
mainpath="$(python3 experiments/default_study/get_param.py --get_default mainpath)"
output_path="$(python3 experiments/default_study/get_param.py --get_default output_path)"

num_terminals=5


mkdir -p ${output_path}/${study}/analysis

possible_screens=()

# defines possible ports for screens
for t in $(seq 1 $((${num_terminals}))); do
    possible_screens+=($t)
done


while true
	do

    printf "\n  >>>> loop ... \n"

    # discover free terminals

    active_screens=()
    free_screens=()
    active_experiments=()


    declare -a arr="$(screen -list)"


    for obj in ${arr[@]}; do

        if [[ "$obj" == *"screen_"* ]]; then
          printf "\n screen ${obj} is on\n"
          screen="$(cut -d'_' -f2 <<<"$obj")"
          active_experiments+=("$(cut -d'_' -f3 -<<<"$obj")_$(cut -d'_' -f4 -<<<"$obj")")
          active_screens+=($screen)
        fi
    done

   for possible_screen in "${possible_screens[@]}"; do
       if [[ ! " ${active_screens[@]} " =~ " ${possible_screen} " ]]; then
           free_screens+=($possible_screen)
     fi
      done


    # discover unfinished experiments

    to_do=()
    unfinished=()
    for i in $(seq $runs)
    do
        run=$(($i))

        for experiment in "${experiments[@]}"
        do

         printf  "\n${experiment}_${run} \n"
         file="${output_path}/${study}/${experiment}_${run}.log";


         #check experiments status
         if [[ -f "$file" ]]; then

              lastgen=$(grep -c "Finished generation" $file);
              echo "latest finished gen ${lastgen}";

             if [ "$lastgen" -lt "$num_generations" ]; then
                unfinished+=("${experiment}_${run}")

                # [HP] REMOVES ABORTED EXPERIMENTS
                if [[ ! " ${active_experiments[@]} " =~ " ${experiment}_${run} " ]]; then
                  rm $file
                  rm -rf "${output_path}/${study}/${experiment}/run_${run}"
                fi
                # only if not already running. [HP] DISABLED CONTINUEING EXPERIMENT
                # if [[ ! " ${active_experiments[@]} " =~ " ${experiment}_${run} " ]]; then
                #    to_do+=("${experiment}_${run}")
                # fi
             fi
         else
             # not started yet
             echo " None";
               unfinished+=("${experiment}_${run}")
               # only if not already running
                if [[ ! " ${active_experiments[@]} " =~ " ${experiment}_${run} " ]]; then
                   to_do+=("${experiment}_${run}")
                fi
         fi

        done
    done


    # spawns N experiments (N is according to free screens)

    max_fs=${#free_screens[@]}
    to_do_now=("${to_do[@]:0:$max_fs}")

    p=0
    for to_d in "${to_do_now[@]}"; do

        exp=$(cut -d'_' -f1 <<<"${to_d}")
        run=$(cut -d'_' -f2 <<<"${to_d}")
        idx=$( echo ${experiments[@]/${exp}//} | cut -d/ -f1 | wc -w | tr -d ' ' )

        # nice -n19 python3  experiments/${study}/optimize.py
        screen -d -m -S screen_${free_screens[$p]}_${to_d} -L -Logfile ${output_path}/${study}/${exp}_${run}".log" python3  experiments/${study}/optimize.py \
               --experiment_name ${exp} --seasons_conditions ${seasons_conditions[$idx]} --run ${run} --study=${study} --num_generations ${num_generations};

        printf "\n >> (re)starting screen_${free_screens[$p]}_${to_d} \n\n"
        p=$((${p}+1))

    done

   if [ -z "$unfinished" ]; then
       printf "DONE. EXITING LOOP\n"
        exit
    fi

    printf "restarting loop in 180 seconds...\n"
    sleep 20;
    printf "restarting loop in 120 seconds...\n"
    sleep 20;
    printf "restarting loop in  60 seconds...\n"
    sleep 20;

done

# run from revolve root
# screen -ls  | egrep "^\s*[0-9]+.screen_" | awk -F "." '{print $1}' |  xargs kill
# killall screen
# screen -r naaameee
# screen -list



# run from revolve root
# screen -ls  | egrep "^\s*[0-9]+.screen_" | awk -F "." '{print $1}' |  xargs kill
# killall screen
# screen -r naaameee
# screen -list

