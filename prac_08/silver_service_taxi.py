"""
CP1404/CP5632 Practical
Car class
"""
from prac_08.car import Car
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Taxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.fanciness = fanciness * self.price_per_km
        self.flagfall = 4.50

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km plus flagfall of ${:.2f}".format(super().__str__(),
                                                             self.current_fare_distance,
                                                             self.fanciness,
                                                             self.flagfall)

    def get_fare(self):
        """Return the price for the silver taxi trip."""
        return (self.price_per_km * self.current_fare_distance + self.flagfall)

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
