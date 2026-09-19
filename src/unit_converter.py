# Imports

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

from helpers import (
    get_number,
    pause,
    display_results,
    show_history,
    clear_history,
)
# Functions should stay at the top
# These functions do the user interaction
# :g gets rid of trailing zeros, :.2f rounds to 2 decimal places.

def convert_kilometres_to_miles(history):
    kilometres = get_number("Enter kilometres: ")
    miles = kilometres_to_miles(kilometres)
    display_results(kilometres, "km", miles, "miles", history)
    pause()

def convert_miles_to_kilometres(history):
    miles = get_number("Enter miles: ")
    kilometres = miles_to_kilometres(miles)
    display_results(miles, "miles", kilometres, "km", history)
    pause()

def convert_celsius_to_fahrenheit(history):
    celsius = get_number("Enter Celsius: ", allow_negative=True)
    fahrenheit = celsius_to_fahrenheit(celsius)
    display_results(celsius, "C", fahrenheit, "F", history)
    pause()

def convert_fahrenheit_to_celsius(history):
    fahrenheit = get_number("Enter Fahrenheit: ", allow_negative=True)
    celsius = fahrenheit_to_celsius(fahrenheit)
    display_results(fahrenheit, "F", celsius, "C", history)
    pause()

def convert_kilograms_to_pounds(history):
    kilograms = get_number("Enter Kilograms: ")
    pounds = kilograms_to_pounds(kilograms)
    display_results(kilograms, "kg", pounds, "lbs", history)
    pause()

def convert_pounds_to_kilograms(history):
    pounds = get_number("Enter Pounds: ")
    kilograms = pounds_to_kilograms(pounds)
    display_results(pounds, "lbs", kilograms, "kg", history)
    pause()

def convert_litres_to_gallons(history):
    litres = get_number("Enter litres: ")
    gallons = litres_to_gallons(litres)
    display_results(litres, "L", gallons, "gal", history)
    pause()

def convert_gallons_to_litres(history):
    gallons = get_number("Enter gallons: ")
    litres = gallons_to_litres(gallons)
    display_results(gallons, "gal", litres, "L", history)
    pause()

# Menu for Programme
def show_menu():
    print("UNIT CONVERTER")
    print("==============")
    print("1. Kilometres to Miles")
    print("2. Miles to Kilometres")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    print("7. Litres to Gallons")
    print("8. Gallons to Litres")
    print("9. Show History")
    print("10. Clear History")
    print("11. Quit")


# By defining a list we can make the if loop much more compact.
conversions = {
    "1": convert_kilometres_to_miles,
    "2": convert_miles_to_kilometres,
    "3": convert_celsius_to_fahrenheit,
    "4": convert_fahrenheit_to_celsius,
    "5": convert_kilograms_to_pounds,
    "6": convert_pounds_to_kilograms,
    "7": convert_litres_to_gallons,
    "8": convert_gallons_to_litres
}
# To make more than one selection post conversion, you need a while loop.
# Anything indented under a while loop will repeat
def main():
    # This is creating an empty list called history. We can add to it using history.append(conversion)
    history = []

    while True:

        show_menu()
        # Input Area
        choice = input("Choose an Option: ")

        # Input Selection and Conversion
        if choice in conversions:
            conversions[choice](history)

        elif choice == "9":
            show_history(history)

        elif choice == "10":
            clear_history(history)

    # break ends the loop
        elif choice == "11":
            print("Goodbye!")
            break

        else:
            print("Invalid Option")

if __name__ == "__main__":
    main()
