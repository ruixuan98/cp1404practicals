import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# TODO answer questions in prac_02
# 1. Got l14 on line 1
# Largest number i can get is 20, smallest 5
# 2. Got 7
# Largest numnber i can get is 9, smallest 3
# Line 2 could not have produced a 4 as it's in increments of +2, and it starts from 3.
# 3. Got 4.297187207974266
# Largest i can get is 5.5, smallest 2.5

print(random.uniform(1, 100))  # 4
