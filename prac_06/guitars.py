"""
Cp1404 Practicals
Program to get user to enter his guitar and keep in list of lists
"""

from prac_06.guitar import Guitar

guitars = []


def main():
    print("My guitars!")
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(guitar, "\n")
    print("Name:", "\n")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are my guitars:")
        vintage_string = ""
        for i, guitar in enumerate(guitars):
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            else:
                vintage_string = ""
            print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars ")


main()
