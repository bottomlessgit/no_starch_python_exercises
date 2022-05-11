list_of_cysts = ["colloid", "epididymal", "arachnoid", "sebacious", "ganglion"]

print("List of cysts:")
print(list_of_cysts)

print("Length of list:")
print(len(list_of_cysts))

print("List sorted temporarily:")
print(sorted(list_of_cysts))

print("List reverse sorted temporarily:")
print(sorted(list_of_cysts, reverse=True))

print("Now changing lists:")
list_of_cysts[1] = "periapical"
del list_of_cysts[2]
list_of_cysts.append("tarlov")
list_of_cysts.insert(0, "acne")
list_of_cysts.pop()
list_of_cysts.pop(2)

print("New list:")
print(list_of_cysts)

print("New list reversed:")
list_of_cysts.reverse()
print(list_of_cysts)

print("New list reversed back:")
list_of_cysts.reverse()
print(list_of_cysts)

print("New list sorted permanently:")
list_of_cysts.sort()
print(list_of_cysts)

print("New list sorted in reverse permanently:")
list_of_cysts.sort(reverse=True)
print(list_of_cysts)



