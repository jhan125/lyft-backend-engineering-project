from car import Car
from engines.capulet_engine import CapuletEngine
from batteries.nubbin_battery import NubbinBattery

class Thovex(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        thovex_engine = CapuletEngine(current_mileage, last_service_mileage)
        thovex_battery = NubbinBattery(last_service_date)

        super().__init__(thovex_engine, thovex_battery)

        self.engine = thovex_engine
        self.battery = thovex_battery
    
    def needs_service(self):
        return super().needs_service()