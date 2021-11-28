"""
CP1404/CP5632 - Practical

Broken program to determine score status
"""


score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
else:
    if score >= 90:
        print("Excellent")
    if 50 <= score < 90:
        print("Passable")
    if score < 50:
        print("Bad")
