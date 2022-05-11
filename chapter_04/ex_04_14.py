cubes = [i**3 for i in range(1, 11)]
print(cubes)
print("The first 3 items in the list are: ") 
print(cubes[0:3])
print("The middle 3 items on the list are: ") 
print(cubes[ (len(cubes)//2 - 1) : (len(cubes)//2 + 2) ])
print("The last 3 items on the list are:")
print(cubes[-3:])

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

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:") 
for my_food in my_foods:
    print(my_food)
print("\nMy friend's favorite foods are:") 
for friend_food in friend_foods:
    print(friend_food)