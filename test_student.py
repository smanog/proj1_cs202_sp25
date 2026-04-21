import unittest
from proj1 import *
#proj1.py should contain your data class and function definitions
#these do not contribute positivly to your grade. 
#but your grade will be lowered if they are missing

class TestRegionFunctions(unittest.TestCase):

    def setUp(self):
        self.rect = GlobeRect(34.0, 35.0, -118.0, -117.0)

    def test_holder(self):
        pass

    def test_emissions_per_capita(self):
        self.assertEqual(emissions_per_capita(RegionCondition(Region(GlobeRect(34.0, 35.0, -118.0, -117.0), 'Los Angeles', 'other'), 2026, 3869890, 430)), 0.00011111426939783818)
        self.assertEqual(emissions_per_capita(RegionCondition(Region(GlobeRect(33,34,151, 152), 'Sydney', 'other'), 2026, 0, 520)), 0.0)

    def test_area(self):
        self.assertEqual(area(self.rect), 10212.347546343432)
        self.assertEqual(area(GlobeRect(33,34,151, 152)), 10333.286269130025)

    def test_emissions_per_square_km(self):
        self.assertEqual(emissions_per_square_km(RegionCondition(Region(GlobeRect(34.0, 35.0, -118.0, -117.0), 'Los Angeles', 'other'), 2026, 3869890, 430)), 0.04210589172065174)

    def test_densest(self):
        self.assertEqual(densest(region_conditions), 'Sydney')

    def test_growth_rate(self):
        self.assertEqual(growth_rate(RegionCondition(Region(GlobeRect(34.0, 35.0, -118.0, -117.0), 'Los Angeles', 'other'), 2026, 3869890, 430),5),5804)

    def test_scale_ghg(self):
        self.assertEqual(scale_ghg(RegionCondition(Region(GlobeRect(34.0, 35.0, -118.0, -117.0), 'Los Angeles', 'other'), 2026, 3869890, 430), 5), 430.64490721958504)

if __name__ == '__main__':
    unittest.main()
