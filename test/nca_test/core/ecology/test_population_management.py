import unittest

from nca.core.agent.agents import Agents
from nca.core.agent.individual_factory import IndividualFactory
from nca.core.ecology.population_management import PopulationManagement


class PopulationManagementTest(unittest.TestCase):
    n=3

    def test_management(self):
        population_management = PopulationManagement()

        agents1: Agents = IndividualFactory().initialize().create(self.n)
        population_management.initialize(agents1)

        self.assertEqual(population_management.population.individuals, agents1)

        agents2: Agents = IndividualFactory().initialize().create(self.n)
        population_management.initialize(agents2)

        self.assertEqual(population_management.population.individuals, agents2)