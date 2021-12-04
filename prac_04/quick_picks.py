"""
Cp1404 Practicals
Generate number of lines based on user input
"""
import random

NUMBER_OF_LINES = 6
MAXIMUM = 45
MINIMUM = 1


def main():
    """Asks user to input number of rows of quick picks they want"""
    quick_picks = int(input("How many quick picks? "))
    while quick_picks < 1:
        print("Invalid input. Try again.")
        quick_picks = int(input("How many quick picks? "))

    for i in range(quick_picks):
        quick_picks_values = []
        for j in range(NUMBER_OF_LINES):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_picks_values:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_picks_values.append(number)
        quick_picks_values.sort()
        print(" ".join("{:2}".format(number) for number in quick_picks_values))


main()
