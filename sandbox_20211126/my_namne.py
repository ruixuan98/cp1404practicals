"""
Print author's name

Created by Rui, November .2021
"""


def main():
    print("cheebai")


main()

try:
    x = int("zero")
    print(10 / x)
except ZeroDivisionError:
    print("div")
except NameError:
    print("name")
except ValueError:
    print("value")
except:
    print("other")