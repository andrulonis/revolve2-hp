import math
import unittest

from nca.core.agent.individual import Individual
from nca.core.agent.individual_factory import IndividualFactory
from nca.core.ecology.population import Population
from nca.core.ecology.speciation.compatibility import Compatibility
from nca.core.ecology.speciation.genus import Genus
from nca.core.genome.initialization import BinaryInitialization
from nca.core.genome.representations.valued_representation import ValuedRepresentation


class GenusTest(unittest.TestCase):

    def test_add(self):
        genus = Genus(Compatibility(limit=math.inf))

        n = 3
        for _ in range(n):
            genus.add(Population(IndividualFactory().initialize().create(3)))

        self.assertEqual(len(genus.species), n)

    def test_insert(self):
        genus = Genus(Compatibility(limit=math.inf))

        n = 3
        factory = IndividualFactory(ValuedRepresentation).initialize(BinaryInitialization())
        genus.add(Population(factory.create(n)))

        individual: Individual = factory.create(1)[0]
        genus.insert(individual)

        self.assertEqual(len(genus.species), 1)
        self.assertEqual(len(genus.species[0].individuals), n+1)