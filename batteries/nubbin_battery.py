from batteries.battery import Battery
from datetime import datetime
from utils import add_years_to_date

class NubbinBattery(Battery):
    def __init_(self, last_service_date):
        super().__init__(self, last_service_date)
        self.last_service_date = last_service_date

    def battery_needs_service(self):
        service_threshold_date = add_years_to_date(self.last_service_date, 4)
        
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False