pizzas = ["avocado", "pineapple", "plain", "allTomato"]
for pizza in pizzas:
	print("I love " + pizza)
print("I rEaLlY lOvE PiZzA!!!!")
friend_pizzas = pizzas[:]
pizzas.append("sardine")
print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
friend_pizzas.append("lettuce")
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)