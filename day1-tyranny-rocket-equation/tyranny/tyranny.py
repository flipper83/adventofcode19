import functools
from typing import List

INITIAL_VALUE = 0


class FuelMeasurer:

    def measure(self, mass: int, total: int = 0):
        fuel = int(mass / 3) - 2
        if fuel <= 0:
            return total

        return self.measure(fuel, total + fuel)

    def measure_all(self, masses: List[int]) -> int:
        return functools.reduce(lambda total, mass: total + self.measure(mass),
                                masses,
                                INITIAL_VALUE)
