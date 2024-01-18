import unittest

import sys
sys.path.append('/Users/sjhan125/lyft-backend/lyft-backend-engineering-project')
from engines.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.engine_needs_service())

    def test_needs_service_false(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.engine_needs_service())

if __name__ == '__main__':
    unittest.main()