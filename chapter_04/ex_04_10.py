cubes = [i**3 for i in range(1, 11)]
print(cubes)
print("The first 3 items in the list are: ") 
print(cubes[0:3])
print("The middle 3 items on the list are: ") 
print(cubes[ (len(cubes)//2 - 1) : (len(cubes)//2 + 2) ])
print("The last 3 items on the list are:")
print(cubes[-3:])