"""
Cp1404 Practicals
Generate number of lines based on user input
"""
import random

NUMBER_OF_LINES = 6
MAXIMUM = 45
MINIMUM = 1


def main():
    quick_picks = int(input("How many quick picks? "))
    while quick_picks < 1:
        print("Invalid input. Try again.")
        quick_picks = int(input("How many quick picks? "))
    generate_quick_picks(quick_picks)


def generate_quick_picks():
    quick_pick_values = []
    for i in range(NUMBER_OF_LINES):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in quick_pick_values:
            number = random.randint(MINIMUM, MAXIMUM)
        quick_pick_values.append(number)
    return quick_pick_values


main()
