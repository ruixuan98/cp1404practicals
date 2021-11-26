for i in range(1, 21, 2):
    print(i, end=' ')
print()
for c in range(0, 101, 10):
    print(c, end=' ')
print()
for d in range(20, 0, -1):
    print(d, end=' ')
print()
choice_number_of_stars = int(input('Number of stars: '))
if choice_number_of_stars > 0:
    for p in range(choice_number_of_stars):
        print('*', end='')
        print()
else:
    print("Invalid input.")
print()
choice_number_of_incremental_stars = int(input('Number of stars: '))
if choice_number_of_incremental_stars > 0:
    for r in range(1, choice_number_of_incremental_stars + 1):
        print("*" * r, end='')
        print()
else:
    print("Invalid input.")

print("Thank you.")
