import argparse


class Config():




    def _get_params(self):
        # defaults listed for easier use
        default_population_size             = 100                   # HP parameter 100
        default_offspring_size              = 100                    # HP parameter 100
        default_num_generations             = 200                     # HP parameter 200
        default_max_modules                 = 30
        default_substrate_radius            = 15
        default_plastic_body                = 0
        default_plastic_brain               = 0
        default_body_substrate_dimensions   = '2d'
        default_num_initial_mutations       = 10
        default_crossover_prob              = 0
        default_mutation_prob               = 1
        default_fitness_measure             = "speed_y"
        default_study_name                  = "default_study"       # HP parameter default_study
        default_experiment_name             = "rugged"
        default_mainpath                    = "~"         # HP parameter is "honours2021"
        default_output_path                 = "/storage/honours2021"
        default_total_runs                  = 10                     # HP parameter is 30
        default_run                         = 1
        default_simulation_time             = 30
        default_sampling_frequency          = 5
        default_get_default                 = "run"
        default_run_simulation              = 1
        default_control_frequency           = 20
        default_seasons_conditions          = '1.0_1.0_0'

        parser = argparse.ArgumentParser()

        # EA params

        parser.add_argument(
            "--population_size",    #HP parameter is 100
            required=False,
            default=default_population_size,
            type=int,
        )

        parser.add_argument(
            "--offspring_size",
            required=False,
            default=default_offspring_size,
            type=int,
        )

        parser.add_argument(
            "--num_generations",
            required=False,
            default=default_num_generations,            #HP parameter is 200
            type=int,
        )

        parser.add_argument(
            "--max_modules",
            required=False,
            default=default_max_modules,
            type=int,
            help="",
        )

        parser.add_argument(
            "--substrate_radius",
            required=False,
            default=default_substrate_radius,
            type=int,
            help="",
        )

        parser.add_argument(
            "--plastic_body",
            required=False,
            default=default_plastic_body,
            type=int,
            help="0 is not plastic, 1 is plastic",
        )

        parser.add_argument(
            "--plastic_brain",
            required=False,
            default=default_plastic_brain,
            type=int,
            help="0 is not plastic, 1 is plastic",
        )

        parser.add_argument(
            "--body_substrate_dimensions",
            required=False,
            default=default_body_substrate_dimensions,
            type=str,
            help="2d or 3d",
        )

        parser.add_argument(
            "--num_initial_mutations",
            required=False,
            default=default_num_initial_mutations,
            type=int,
        )  # number of initial mutations for body and brain CPPNWIN networks

        parser.add_argument(
            "--crossover_prob",
            required=False,
            default=default_crossover_prob,
            type=float,
        )

        parser.add_argument(
            "--mutation_prob",
            required=False,
            default=default_mutation_prob,
            type=float,
        )

        parser.add_argument(
            "--fitness_measure",
            required=False,
            default=default_fitness_measure,
            type=str,
        )

        # Simulation and experiment params

        parser.add_argument(
            "--study_name",
            required=False,
            default=default_study_name,
            type=str,
            help="",
        )

        parser.add_argument(
            "--experiment_name",
            required=False,
            default=default_experiment_name,
            type=str,
            help="Name of the experiment.",
        )

        parser.add_argument(
            "--mainpath",
            required=False,
            default=default_mainpath,
            type=str,
            help="directory in /home to run from",
        )

        parser.add_argument(
            "--output_path",
            required=False,
            default=default_output_path,
            type=str,
            help="directory in /home to output files",
        )

        parser.add_argument(
            "--total_runs",
            required=False,
            default=default_total_runs,
            type=int,
            help="total number of runs"
        )

        parser.add_argument(
            "--run",
            required=False,
            default=default_run,
            type=int,
            help="which run to run right now",
        )

        parser.add_argument(
            "--simulation_time",
            required=False,
            default=default_simulation_time,
            type=int,
        )

        parser.add_argument(
            "--sampling_frequency",
            required=False,
            default=default_sampling_frequency,
            type=int,
        )  # number of samples per sec from batch (snapshots of sim)

        parser.add_argument(        #HP, added this one to make the arguments available in bash
            "--get_default",
            required=False,
            default=default_get_default,
            type=str,
        )

        parser.add_argument(
            "--run_simulation",
            required=False,
            default=default_run_simulation,
            type=int,
            help="If 0, runs optimizer without simulating robots, so behavioral measures are none."
        )

        parser.add_argument(
            "--control_frequency",
            required=False,
            default=default_control_frequency,
            type=int,
        )

        parser.add_argument(
            "--seasons_conditions",
            required=False,
            default=default_seasons_conditions,
            type=str,
            # seasons separated by '#' and their params separated by '_': params order matters!
            help="staticfriction_dynamicfriction_yrotationdegrees|"
                 "staticfriction_dynamicfriction_yrotationdegrees|...",
        )
        args = parser.parse_args()

        return args

