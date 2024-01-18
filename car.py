from batteries.battery import Battery
from engines.engine import Engine

class Car(Engine, Battery):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def battery_needs_service(self):
        return self.battery.battery_needs_service()

    def engine_needs_service(self):
        return self.engine.engine_needs_service()

    def needs_service(self):
        return self.engine_needs_service() or self.battery_needs_service()
