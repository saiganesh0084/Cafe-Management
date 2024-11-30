#menu
menu = {'Pizza' : 40, 'Pasta' : 50, 'Burger' : 60, 'Salad' : 70, 'Coffee' : 80,}

#Greetings
print("Welcome to Bean Hive Cafe")
print("Pizza: 40/-\nPaste: 50/-\nBurger: 60/-\nSalad: 70/-\nCoffee: 80/-")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
	order_total += menu[item_1]
	print(f"Your item {intem_1} has been added to your order")
else:
	print(f"Ordered item {item_1} is not available yet")
another_order = input("Do you want add another item? (Yes / NO)")
if another_order == "Yes":
	item_2 = input("Enter the name of item you want to order = ")
	if item_2 in menu:
		order_total += menu[item_2]
		print(f"Your item {intem_2} has been added to your order")
	else:
		print(f"Ordered item {item_2} is not available yet")
print(f"The total amount of items to pay is {order_total}