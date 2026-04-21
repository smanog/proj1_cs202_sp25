import unittest
from proj1 import *
#proj1.py should contain your data class and function definitions
#these do not contribute positivly to your grade. 
#but your grade will be lowered if they are missing

class TestRegionFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test_holder(self):
        pass

    def test_emissions_per_capita(self):
        self.assertEqual(emissions_per_capita(RegionCondition(Region(GlobeRect(34.0, 35.0, -118.0, -117.0), 'Los Angeles', 'other'), 2026, 3869890, 430)), 0.00011111426939783818)


if __name__ == '__main__':
    unittest.main()
