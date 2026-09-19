# Unit Conversion App

A simple Python command-line unit converter.

## Supported conversions

1. Kilometres to miles
2. Miles to kilometres
3. Celsius to Fahrenheit
4. Fahrenheit to Celsius
5. Kilograms to pounds
6. Pounds to kilograms
7. Litres to gallons
8. Gallons to litres

The app also includes a conversion history, allowing the user to view or clear previous conversions.

## Project structure

- `src/unit_converter.py` – main application and menu flow
- `src/conversions.py` – conversion calculations
- `src/helpers.py` – input validation, display, history and other helper functions
- `tests/` – automated tests

## How to run

From the project root:

python src/unit_converter.py

## How to test

Run the test suite with:

pytest

To check test coverage:

pytest --cov=src --cov-report=term-missing

The project currently has 99% overall test coverage, with the conversion and helper modules at 100%.