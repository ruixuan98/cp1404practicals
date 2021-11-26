# Files.py start from scratch

out_file = open("name.txt", "w")
input_name = input(str("Please enter your name: "))
print(input_name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.readline()
print("Your name is:", name)

out_file = open("numbers.txt", "w")
for i in (17, 42, 400):
    print(i, file=out_file)
out_file.close()

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total = total + number
print(total)
