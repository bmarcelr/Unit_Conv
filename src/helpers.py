# This function asks for a number. If anything other than a number is entered, it asks for one,
# and will continue to do so until it receives one, at which the function will end. Error handling.
# Adding allow_negative into the number calc allows assing of positive or negative to
# conversions. It is now the default assumption, that it can't be negative.
def get_number(prompt, allow_negative=False):
    while True:
        try:
            number = float(input(prompt)) 
            # This checks if the number is <0 and if it is, continues through the loop.
            # It does not immediately return it.
            # If not, it prints the text and waits for the user to try again.
            if not allow_negative and number < 0: 
                print("Please enter a positive number")
                continue

            return number
        
        except ValueError:
            print("Please enter a number.")

def pause():
    input("Press Enter to return to the menu...")

def display_results(value, unit_from, result, unit_to, history):
    conversion = f"{value:g} {unit_from} = {result:.2f} {unit_to}"
    print()
    print(conversion)
    print()

    history.append(conversion)

# History functions
def show_history(history):
    print()
    print("CONVERSION HISTORY")
    print("==================")

    if not history:
        print("No conversions yet.")
    else:
        for conversion in history:
            print(conversion)

    print()
    pause()

def clear_history(history):
    history.clear()
    print("Conversion history cleared.")
    pause()