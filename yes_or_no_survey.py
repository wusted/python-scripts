#!/usr/bin/python3

def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper()     # convert to uppercase
        if answer == "Y" or answer == "N":
            valid_input = True
        else:
            print("Please enter Y for yes or N for no. ")
    return answer

response = get_yes_or_no("Do you like yerba mate? Y)es or N)o: ")
if response == "Y":
    print("Awesome, yerba mate is delicious.")
else:
    print("Too bad, well made yerba mate can very healthy and energizing.")

        