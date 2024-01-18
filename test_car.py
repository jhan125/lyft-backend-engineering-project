import unittest
from datetime import datetime

from models.calliope import Calliope
from models.glissade import Glissade
from models.palindrome import Palindrome
from models.rorschach import Rorschach
from models.thovex import Thovex

# Calliope:	    Capulet Engine	|| Spindler Battery   || Octoprime Tire
#       once every 30,000 miles || once every 3 years || sum >= 3.0
class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.8, 0.9, 0.7]

        car = Calliope(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.8, 0.9, 0.7]

        car = Calliope(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.8, 0.9, 0.7]

        car = Calliope(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.8, 0.9, 0.7]

        car = Calliope(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = [0.1, 1.8, 0.9, 0.7]

        car = Calliope(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.8, 0.9, 0.7]

        car = Calliope(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertFalse(car.needs_service())

# Glissade:	    Willoughby Engine	|| Spindler Battery    || Carrigan Tire
#           once every 60,000 miles || once every 3 years  || any >= 0.9
class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.8, 0.5, 0.7]

        car = Glissade(current_mileage, last_service_mileage,last_service_date, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.8, 0.5, 0.7]

        car = Glissade(current_mileage, last_service_mileage,last_service_date, tire_sensor_data)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.8, 0.5, 0.7]

        car = Glissade(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.8, 0.5, 0.7]

        car = Glissade(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.9, 0.5, 0.7]

        car = Glissade(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.8, 0.5, 0.7]

        car = Glissade(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertFalse(car.needs_service())


# Palindrome:	     Sternman Engine    || Splinder Battery   ||  OctoprimeTire
# only when the warning indicator is on || once every 3 years ||  sum  >= 3.0
class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        warning_light_is_on = False
        tire_sensor_data = [0.1, 0.9, 0.5, 0.7]

        car = Palindrome(last_service_date, warning_light_is_on, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False
        tire_sensor_data = [0.1, 0.9, 0.5, 0.7]

        car = Palindrome(last_service_date, warning_light_is_on, tire_sensor_data)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        tire_sensor_data = [0.1, 0.9, 0.5, 0.7]

        car = Palindrome(last_service_date, warning_light_is_on, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tire_sensor_data = [0.1, 0.9, 0.5, 0.7]

        car = Palindrome(last_service_date, warning_light_is_on, tire_sensor_data)
        self.assertFalse(car.needs_service())
    
    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tire_sensor_data = [0.1, 1.9, 0.5, 0.7]

        car = Palindrome(last_service_date, warning_light_is_on, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tire_sensor_data = [0.1, 0.9, 0.5, 0.7]

        car = Palindrome(last_service_date, warning_light_is_on, tire_sensor_data)
        self.assertFalse(car.needs_service())

# Rorschach:	     Willoughby Engine    || Nubbin Battery     || Octoprime Tire
#                 once every 60,000 miles || once every 4 years || sum >= 3.0
class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.9, 0.5, 0.7]

        car = Rorschach(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.9, 0.5, 0.7]

        car = Rorschach(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.9, 0.5, 0.7]

        car = Rorschach(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.9, 0.5, 0.7]

        car = Rorschach(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertFalse(car.needs_service())
    
    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_sensor_data = [0.1, 1.9, 0.5, 0.7]

        car = Rorschach(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.9, 0.5, 0.7]

        car = Rorschach(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertFalse(car.needs_service())

# Thovex:	    Capulet Engine   || Nubbin Battery      || Carrigan Tire 
#       once every 30,000 miles  || once every 4 years  || any >= 0.9
class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.8, 0.5, 0.7]

        car = Thovex(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.8, 0.5, 0.7]

        car = Thovex(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.8, 0.5, 0.7]

        car = Thovex(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.8, 0.5, 0.7]

        car = Thovex(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.9, 0.5, 0.7]

        car = Thovex(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_sensor_data = [0.1, 0.8, 0.5, 0.7]

        car = Thovex(current_mileage, last_service_mileage, last_service_date, tire_sensor_data)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
