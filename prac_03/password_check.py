"""
Get person to input password, read number of letters and print out asterisks for number of letters

Created by Rui Xuan, 27/11/2021
"""

MINIMUM_LENGTH = 4


def main():
    """Get valid password length and print number of asterisks"""
    password = get_password(MINIMUM_LENGTH)
    print_password(password)


def get_password(minimum_length):
    """Get valid character strength"""
    password = input("Enter your password: ")
    while len(password) < minimum_length:
        print("Invalid number of stars. Try again.")
        password = input("Enter your password: ")
    return password


def print_password(asterisks):
    """Print the number of asterisks for the password"""
    print("Your password is:", "*" * len(asterisks))


main()
