import unittest

import sys
sys.path.append('/Users/jhan125/lyft-backend/lyft-backend-engineering-project')
from tires.carrigan_tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_sensor_data = [0.1, 0.3, 0.2, 0.9] # one value > 0.9
        tires = CarriganTire(tire_sensor_data)
        self.assertTrue(tires.tire_needs_service())

    def test_needs_service_false(self):
        tire_sensor_data = [0.1, 0.2, 0.4, 0.2]
        tires = CarriganTire(tire_sensor_data)
        self.assertFalse(tires.tire_needs_service())

if __name__ == '__main__':
    unittest.main()