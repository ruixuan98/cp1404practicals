from prac_08.car import Car
import random


class UnreliableCar(Car):
    """Represent a Car object."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Car instance.

        name: string, reference name for car
        fuel: float, one unit of fuel drives one kilometre
        """
        super().__init__(name, fuel)
        self.odometer = 0
        self.reliability = float(reliability)

    def __str__(self):
        """Return a string representation of a Car object."""
        return "{}, fuel={}, odometer={}".format(self.name, self.fuel,
                                                 self.odometer)

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.
        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        while self.reliability < random.uniform(0, 100):
            print("Your car has failed!")
            print(f"You have driven 0 km")
            random.uniform(0, 100)
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance
