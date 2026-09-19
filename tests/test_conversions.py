import pytest

from conversions import (
    kilometres_to_miles,
    miles_to_kilometres,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kilograms_to_pounds,
    pounds_to_kilograms,
    litres_to_gallons,
    gallons_to_litres
)

from conversions import (
    kilometres_to_miles,
    miles_to_kilometres,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kilograms_to_pounds,
    pounds_to_kilograms,
    litres_to_gallons,
    gallons_to_litres
)

@pytest.mark.parametrize("kilometres, expected", [
    (10, 6.21371),
    (20, 12.42742),
    (0, 0),
])
def test_kilometres_to_miles(kilometres, expected):
    assert kilometres_to_miles(kilometres) == pytest.approx(expected)


def test_miles_to_kilometres():
    assert miles_to_kilometres(10) == pytest.approx(16.000)


@pytest.mark.parametrize("celsius, expected", [
    (0, 32),
    (100, 212),
    (-40, -40),
])
def test_celsius_to_fahrenheit(celsius, expected):
    assert celsius_to_fahrenheit(celsius) == pytest.approx(expected)

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == pytest.approx(0)

def test_kilograms_to_pounds():
    assert kilograms_to_pounds(10) == pytest.approx(22.0462)

def test_pounds_to_kilograms():
    assert pounds_to_kilograms(10) == pytest.approx(4.53592)

def test_litres_to_gallons():
    assert litres_to_gallons(10) == pytest.approx(2.19969)

def test_gallons_to_litres():
    assert gallons_to_litres(10) == pytest.approx(45.4609)


print("All tests passed!")

