from car import Car
from engines.sternman_engine import SternmanEngine
from batteries.spindler_battery import SpindlerBattery


class Palindrome(Car):
    def __init__(self, last_service_date, warning_indicator_on):
        palindrome_engine = SternmanEngine(warning_indicator_on)
        palindrome_battery = SpindlerBattery(last_service_date)
        
        super().__init__(palindrome_engine, palindrome_battery)

        self.engine = palindrome_engine
        self.battery = palindrome_battery
        
    def needs_service(self):
        return super().needs_service()
