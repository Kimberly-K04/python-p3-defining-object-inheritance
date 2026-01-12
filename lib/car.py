# car.py
from vehicle import Vehicle

class Car(Vehicle):
    # We inherit everything from Vehicle
    # Override the go() method to make it specific to Car
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
