import unittest

import sys
sys.path.append('/Users/jhan125/lyft-backend/lyft-backend-engineering-project')
from tires.octoprime_tire import OctoprimeTire

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.8, 0.8, 0.8, 0.7] # sum >= 3.0
        tires = OctoprimeTire(tire_wear)
        self.assertTrue(tires.tire_needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.1, 0.2, 0.4, 0.2]
        tires = OctoprimeTire(tire_wear)
        self.assertFalse(tires.tire_needs_service())

if __name__ == '__main__':
    unittest.main()