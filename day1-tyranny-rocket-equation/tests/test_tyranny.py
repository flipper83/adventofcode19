from tests.mass_mock_values import get_masses_mock_values
from tyranny.tyranny import FuelMeasurer


def test_should_return_the_fuel_need_to_launch_when_is_not_should_be_rounded():
    fuel_measurer = FuelMeasurer()
    fuel_required = fuel_measurer.measure(mass=12)
    assert fuel_required == 2


def test_should_return_the_fuel_need_to_launch_when_should_be_rounded():
    fuel_measurer = FuelMeasurer()
    fuel_required = fuel_measurer.measure(mass=100756)
    assert fuel_required == 50346


def test_should_return_the_total_fuel_consume_to_launch_all_modules():
    fuel_measurer = FuelMeasurer()
    total_fuel_required = fuel_measurer.measure_all(masses=[12, 14])
    assert total_fuel_required == 4


def test_should_return_the_total_fuel_consume_to_the_input_values():
    fuel_measurer = FuelMeasurer()
    total_fuel_required = fuel_measurer.measure_all(masses=get_masses_mock_values())
    assert total_fuel_required == 5115927
