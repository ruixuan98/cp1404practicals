##start from scratch
##shop calculator

number_of_items = int(input("Number of items= "))

total_price_of_items = 0

while number_of_items <= 0:
    print("Invalid number.")
    number_of_items = int(input("Number of items= "))
else:
    for i in range(0, number_of_items):
        price_of_each_item = float(input("Price of item: "))
        total_price_of_items = total_price_of_items + price_of_each_item

if total_price_of_items > 100:
    total_price_of_items = total_price_of_items * 9 / 10

print(print("Total price for", number_of_items, "items: ${:.2f}".format(total_price_of_items)))
