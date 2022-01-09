from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.car import Car
from prac_08.taxi import Taxi

"""
CP1404 Practicals
Taxi simulator to allow users to choose which taxi they want
"""

MENU = """q)uit, c)hoose taxi, d)rive"""

def main():
    """Get user input and drive taxi"""
    current_taxi = None
    current_bill = 0
    total_bill = 0
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print(MENU)
    user_option = input(">>> ").lower()
    while user_option != "q":
        if user_option == "c":
            print("Taxis available:")
            list_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            print(f"Bill to date: {total_bill}")
            user_option = input(">>> ").lower()
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif user_option == "d":
            if current_taxi:
                distance = float(input("Drive how far? "))
                current_taxi.start_fare()
                current_bill = current_taxi.drive(distance)
                current_bill = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${current_bill:.2f}")
                total_bill += current_bill
                print(f"Bill to date: {total_bill:.2f}")
                user_option = input(">>> ").lower()
        else:
            print("invalid option.")
            user_option = input(">>> ").lower()
    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    list_taxis(taxis)


def list_taxis(taxis):
    """Lists taxis"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()