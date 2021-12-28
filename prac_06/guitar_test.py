"""
CP1404 Practicals
Program to test if class is working
"""

from prac_06.guitar import Guitar

def main():
    """Get data stored and initialized"""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2000, 1300.50)

    print(f"{gibson.name} get_age() - Expected 99. Got {gibson.get_age()}")
    print(f"{another_guitar} get_age() - Expected 21. Got {another_guitar.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")

main()
