import random
from typing import List

from nca.core.actor.actors import Actors
from nca.core.actor.individual import Individual
from nca.core.analysis.statistics import fitness_key
from nca.core.evolution.selection.selection import SurvivorSelection


class FitnessSteadyStateSelection(SurvivorSelection):

    def __init__(self):
        super().__init__()

    def __call__(self, individuals: List[Individual]) -> List[Individual]:
        return sorted(individuals, key=lambda x: x.get_fitness(), reverse=True)


class GenerationalSteadyStateSelection(SurvivorSelection):

    def __init__(self):
        super().__init__()

    def __call__(self, individuals: List[Individual]) -> List[Individual]:
        return sorted(individuals, key=lambda x: x.age.generations, reverse=False)


class ElitismSelection(SurvivorSelection):

    def __init__(self):
        super().__init__()

    def __call__(self, individuals: List[Individual]) -> List[Individual]:
        sorted_individuals: List[Individual] = sorted(individuals, key=lambda x: x.fitness, reverse=False)
        elite_individuals: List[Individual] = sorted_individuals[:self.configuration.selection_size]
        non_elite_individuals: List[Individual] = sorted_individuals[self.configuration.selection_size:]

        new_individuals = elite_individuals
        random.shuffle(non_elite_individuals)
        new_individuals.extend(non_elite_individuals)
        return new_individuals


class RoundRobinTournament(SurvivorSelection):

    def __init__(self):
        super().__init__()

    def __call__(self, individuals: Actors) -> List[Individual]:
        new_individuals = []
        for _ in self.configuration.population_size:
            tournament_individuals = random.choices(individuals, k=2) # TODO parameterize
            new_individuals.append(max(tournament_individuals, key=fitness_key))
        return new_individuals


class MuLambdaSelection(SurvivorSelection):

    def __init__(self):
        super().__init__()

    def __call__(self, individuals: Actors) -> List[Individual]:
        raise Exception("Unimplemented Mu Lambda Selection")
        return []


class NullSurvivorSelection(FitnessSteadyStateSelection):
    pass
