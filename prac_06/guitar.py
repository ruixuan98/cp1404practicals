"""
CP1404 Practicals
Store guitars and find out which ones are vintage
"""

CURRENT_YEAR = 2021
VINTAGE_AGE = 50


class Guitar:
    """Class to store guitar details"""

    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        age = self.get_age()
        if age < VINTAGE_AGE:
            return False
        else:
            return True
