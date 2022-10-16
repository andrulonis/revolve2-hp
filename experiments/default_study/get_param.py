###change default parameters in <revolve2>/core/revolve2/config.py

from revolve2.core.config import Config
import sys

args = Config()._get_params()
flag = sys.argv[2]

if  (flag=="body_substrate_dimensions"):
    print(args.body_substrate_dimensions)
elif (flag=="control_frequency"):
    print(args.control_frequency)
elif (flag=="crossover_prob"):
    print(args.crossover_prob)
elif (flag=="experiment_name"):
   print(args.experiment_name)
elif (flag=="fitness_measure"):
   print(args.fitness_measure)
elif (flag=="mainpath"):
   print(args.mainpath)
elif (flag=="max_modules"):
   print(args.max_modules)
elif (flag=="mutation_prob"):
   print(args.mutation_prob)
elif (flag=="num_generations"):
   print(args.num_generations)
elif (flag=="num_initial_mutations"):
   print(args.num_initial_mutations)
elif (flag=="offspring_size"):
   print(args.offspring_size)
elif (flag=="plastic_body"):
   print(args.plastic_body)
elif (flag=="plastic_brain"):
   print(args.plastic_brain)
elif (flag=="population_size"):
   print(args.population_size)
elif (flag=="run"):
   print(args.run)
elif (flag=="run_simulation"):
   print(args.run_simulation)
elif (flag=="sampling_frequency"):
   print(args.sampling_frequency)
elif (flag=="seasons_conditions"):
   print(args.seasons_conditions)
elif (flag=="simulation_time"):
   print(args.simulation_time)
elif (flag=="study_name"):
   print(args.study_name)
elif (flag=="substrate_radius"):
   print(args.substrate_radius)
elif (flag=="total_runs"):
   print(args.total_runs)
else:
    NotImplementedError("parameter not added in get_param.py")
