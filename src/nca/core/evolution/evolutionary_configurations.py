from nca.core.abstract.configuration import Configuration
from nca.core.evolution.conditions.initialization import Initialization
from nca.core.evolution.conditions.special_features import SpecialFeatures
from nca.core.evolution.conditions.condition import Condition, EvaluationsCondition
from nca.core.evolution.selection.parent_selection import RouletteWheelSelection
from nca.core.evolution.selection.selection import ParentSelection, SurvivorSelection
from nca.core.evolution.selection.survivor_selection import GenerationalSteadyStateSelection, \
    FitnessSteadyStateSelection
from nca.core.genome.initialization import UniformInitialization
from nca.core.genome.operators.mutation_operator import MutationOperator, ReplaceMutation
from nca.core.genome.operators.recombination_operator import RecombinationOperator, OnePointCrossover


class EvolutionConfiguration(Configuration):

    def __init__(self,
                 recombination: RecombinationOperator,
                 mutation: MutationOperator,
                 parent_selection: ParentSelection,
                 survivor_selection: SurvivorSelection,
                 initialization: Initialization,
                 condition: Condition,
                 special_features: SpecialFeatures):

        super().__init__("evolution.config")
        self.recombination: RecombinationOperator = recombination
        self.mutation: MutationOperator = mutation
        self.parent_selection: ParentSelection = parent_selection
        self.survivor_selection: SurvivorSelection = survivor_selection
        self.initialization: Initialization = initialization
        self.condition: Condition = condition
        self.special_features: SpecialFeatures = special_features


class GeneticAlgorithmConfiguration(EvolutionConfiguration):

    def __init__(self,
                 recombination: RecombinationOperator = OnePointCrossover(),
                 mutation: MutationOperator = ReplaceMutation(),
                 parent_selection: ParentSelection = RouletteWheelSelection(),
                 survivor_selection: SurvivorSelection = FitnessSteadyStateSelection(),
                 initialization: Initialization = UniformInitialization(),
                 condition: Condition = EvaluationsCondition(10),
                 special_features: SpecialFeatures = SpecialFeatures()):
        super().__init__(recombination, mutation, parent_selection, survivor_selection,
                         initialization, condition, special_features)


"""
class EvolutionaryStrategiesConfiguration(EvolutionConfiguration):

    def __init__(self,
                 representation=RealValuedRepresentation(),
                 recombination=DiscreteCrossover(),
                 mutation=GaussianMutation(),
                 parent_selection : ParentSelection = UniformRandomSelection(),
                 survivor_selection: SurvivorSelection = ElitismSelection(),
                 initialization: Initialization = Initialization(),
                 termination_condition: TerminationCondition = TerminationCondition(),
                 special_features: SpecialFeatures = SpecialFeatures()):
        super().__init__(
            representation, recombination, mutation, parent_selection, survivor_selection,
            initialization, termination_condition, special_features)


class EvolutionaryProgrammingConfiguration(EvolutionConfiguration):

    def __init__(self,
                 representation: Representation = RealValuedRepresentation(),
                 recombination: RecombinationOperator = None,
                 mutation: MutationOperator = GaussianMutation(),
                 parent_selection: ParentSelection = DeterministicSelection(),
                 survivor_selection: SurvivorSelection = ProbabilisticSelection(),
                 initialization: Initialization = Initialization(),
                 termination_condition: TerminationCondition = TerminationCondition(),
                 special_features: SpecialFeatures = SpecialFeatures()):
        super().__init__(
            representation, recombination, mutation, parent_selection, survivor_selection,
            initialization, termination_condition, special_features)


class GeneticProgrammingConfiguration(EvolutionConfiguration):

    def __init__(self,
                 representation: Representation = TreeRepresentation(),
                 recombination: RecombinationOperator = SubtreesRecombination(),
                 mutation: MutationOperator = RandomTreeMutation(),
                 parent_selection: ParentSelection = ProportionalSelection("fitness"),
                 survivor_selection: SurvivorSelection = GenerationalSelection(),
                 initialization: Initialization = Initialization(),
                 termination_condition: TerminationCondition = TerminationCondition(),
                 special_features: SpecialFeatures = SpecialFeatures()):
        super().__init__(
            representation, recombination, mutation, parent_selection, survivor_selection,
            initialization, termination_condition, special_features)


class DifferentialEvolutionConfiguration(EvolutionConfiguration):

    def __init__(self,
                 representation: Representation = RealValuedRepresentation(),
                 recombination: RecombinationOperator = UniformCrossover(),
                 mutation: MutationOperator = DifferentialMutation(),
                 parent_selection: ParentSelection = UniformRandomSelection(),
                 survivor_selection: SurvivorSelection = ElitismSelection(),
                 initialization: Initialization = Initialization(),
                 termination_condition: TerminationCondition = TerminationCondition(),
                 special_features: SpecialFeatures = SpecialFeatures()):
        super().__init__(
            representation, recombination, mutation, parent_selection, survivor_selection,
            initialization, termination_condition, special_features)


class ParticleSwarmOptimisationConfiguration(EvolutionConfiguration):
    def __init__(self):
        super().__init__()
"""