import unittest
from proj1 import *
#proj1.py should contain your data class and function definitions
#these do not contribute positivly to your grade. 
#but your grade will be lowered if they are missing

class TestRegionFunctions(unittest.TestCase):

    def setUp(self):
        self.rect = GlobeRect(34.0, 35.0, -118.0, -117.0)
        self.rc = RegionCondition(Region(GlobeRect(33,34,151, 152), 'Sydney', 'other'), 2026, 20, 520)

    def test_holder(self):
        pass

    def test_emissions_per_capita(self):
        self.assertAlmostEqual(emissions_per_capita(RegionCondition(Region(GlobeRect(34.0, 35.0, -118.0, -117.0), 'Los Angeles', 'other'), 2026, 3869890, 430)), 0.0001, 4)
        self.assertEqual(emissions_per_capita(RegionCondition(Region(GlobeRect(33,34,151, 152), 'Sydney', 'other'), 2026, 0, 520)), 0.0)
        self.assertAlmostEqual(emissions_per_capita(RegionCondition(Region(GlobeRect(35, 38, 120, 39), 'Paso Robles', 'other'), 2026, 30, 100)), 3.3333, 4)

    def test_area(self):
        self.assertAlmostEqual(area(self.rect), 10212.3475, 4)
        self.assertAlmostEqual(area(GlobeRect(33,34,151, 152)), 10333.2863, 4)

    def test_emissions_per_square_km(self):
        self.assertAlmostEqual(emissions_per_square_km(RegionCondition(Region(GlobeRect(34.0, 35.0, -118.0, -117.0), 'Los Angeles', 'other'), 2026, 3869890, 430)), 0.0421, 4)
        self.assertAlmostEqual(emissions_per_square_km(self.rc), 0.0503, 4)

    def test_densest(self):
        self.assertEqual(densest(region_conditions), 'Sydney')
        self.assertEqual(densest([self.rc]), 'Sydney')

    def test_growth_rate(self):
        self.assertEqual(growth_rate(RegionCondition(Region(GlobeRect(34.0, 35.0, -118.0, -117.0), 'Los Angeles', 'other'), 2026, 3869890, 430),5),5804)
        self.assertAlmostEqual(growth_rate(self.rc, 1), 0, 4)
        self.assertAlmostEqual(growth_rate(self.rc, 0), 0, 4)

    def test_scale_ghg(self):
        self.assertAlmostEqual(scale_ghg(RegionCondition(Region(GlobeRect(34.0, 35.0, -118.0, -117.0), 'Los Angeles', 'other'), 2026, 3869890, 430), 5), 430.6449, 4)
        self.assertAlmostEqual(scale_ghg(self.rc, 1), 520, 4)
        self.assertAlmostEqual(scale_ghg(self.rc, 0), 520, 4)

    def test_project_condition(self):
        self.assertEqual(project_condition(self.rc, 5), self.rc)

if __name__ == '__main__':
    unittest.main()
