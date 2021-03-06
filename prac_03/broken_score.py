"""
CP1404/CP5632 - Practical

Broken program to determine score status
"""

import random


def main():
    """Get integer and determine grade"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    print(calculate_grade(score))
    random_score = calculate_grade(random.randint(1, 100))
    print(random_score)


def calculate_grade(score):
    """Determine grade"""
    if score >= 90:
        return "Excellent"
    elif 50 <= score < 90:
        return "Passable"
    else:
        return "Bad"


main()
