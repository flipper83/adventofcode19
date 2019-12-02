import functools
from typing import List

INITIAL_VALUE = 0


class FuelMeasurer:

    @staticmethod
    def measure(mass: int):
        return int(mass / 3) - 2

    def measure_all(self, masses: List[int]) -> int:
        return functools.reduce(lambda total, mass: total + self.measure(mass),
                                masses,
                                INITIAL_VALUE)
