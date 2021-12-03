"""
CP1404 Practical
Lists numbers based on factors
"""

numbers = []
for i in range(5):
    user_numbers = int(input("Number: "))
    numbers.append(user_numbers)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
numbers.sort()
print(f"The smallest number is {numbers[0]}")
print(f"The largest number is {numbers[-1]}")
print(f"The average of the numbers is: {sum(numbers)/len(numbers)}")