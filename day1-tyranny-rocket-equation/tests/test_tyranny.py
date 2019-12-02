from tyranny.tyranny import FuelMeasurer


def test_should_return_the_fuel_need_to_launch_when_is_not_should_be_rounded():
    fuel_measurer = FuelMeasurer()
    fuel_required = fuel_measurer.measure(mass=12)
    assert 2 == fuel_required


def test_should_return_the_fuel_need_to_launch_when_should_be_rounded():
    fuel_measurer = FuelMeasurer()
    fuel_required = fuel_measurer.measure(mass=100756)
    assert 33583 == fuel_required
