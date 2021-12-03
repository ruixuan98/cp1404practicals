"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    total_months = int(input("How many months? "))  # This variable stores the number of months

    for month in range(1, total_months + 1):
        income = float(input(f"Enter income for month {str(month)} : "))
        incomes.append(income)
    print(report_income(incomes))


def report_income(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    print(incomes)
    for month, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:10.2f} \
                Total: ${:10.2f}".format(month + 1, income, total))


main()
