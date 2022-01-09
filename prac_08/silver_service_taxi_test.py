from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.car import Car
from prac_08.taxi import Taxi

fancy_taxi = SilverServiceTaxi("Hummer", 100, 4)
print(fancy_taxi)
fancy_taxi.drive(18)
print(fancy_taxi.get_fare())