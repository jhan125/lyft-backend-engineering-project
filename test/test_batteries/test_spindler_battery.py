import unittest
from datetime import date

import sys
sys.path.append('/Users/jhan125/lyft-backend/lyft-backend-engineering-project')
from batteries.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = date.fromisoformat("2017-01-25")
        battery = SpindlerBattery(last_service_date)
        self.assertTrue(battery.battery_needs_service())

    def test_needs_service_false(self):
        last_service_date = date.fromisoformat("2024-01-10")
        battery = SpindlerBattery(last_service_date)
        self.assertFalse(battery.battery_needs_service())

if __name__ == '__main__':
    unittest.main()