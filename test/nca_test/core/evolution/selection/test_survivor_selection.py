import unittest

from nca.core.abstract.configurations import PopulationConfiguration
from nca.core.agent.individual import Individual
from nca.core.agent.individual_factory import IndividualFactory
from nca.core.ecology.population import Population
from nca.core.evolution.selection.survivor_selection import NullSurvivorSelection, FitnessSteadyStateSelection, \
    GenerationalSteadyStateSelection, ElitismSelection


class TestSurvivorSelection(unittest.TestCase):

    def test_random_selection(self):
        population = Population(IndividualFactory().initialize().create(PopulationConfiguration().population_size))

        steady_state = NullSurvivorSelection()

        selected = steady_state(population.individuals)

        for element in selected:
            self.assertIsInstance(element, Individual)

        self.assertEqual(len(selected), len(population.individuals))

    def test_fitness_selection(self):
        population = Population(IndividualFactory().initialize().create(PopulationConfiguration().population_size))

        steady_state = FitnessSteadyStateSelection()

        selected = steady_state(population.individuals)

        for element in selected:
            self.assertIsInstance(element, Individual)

        self.assertEqual(len(selected), len(population.individuals))

    def test_age_selection(self):
        population = Population(IndividualFactory().initialize().create(PopulationConfiguration().population_size))

        steady_state = GenerationalSteadyStateSelection()

        selected = steady_state(population.individuals)

        for element in selected:
            self.assertIsInstance(element, Individual)

        self.assertEqual(len(selected), len(population.individuals))

    def test_elitism_selection(self):
        population = Population(IndividualFactory().initialize().create(PopulationConfiguration().population_size))

        steady_state = ElitismSelection()

        selected = steady_state(population.individuals)

        for element in selected:
            self.assertIsInstance(element, Individual)

        self.assertEqual(len(selected), len(population.individuals))