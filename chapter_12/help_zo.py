"""
Given a list L0 that has inner tuples, inner lists, integers and strings. Write a py program that:

gathers all elements from all inner tuples from L0 into a list L1,
gathers all elements from all inner lists from L0 into a tuple T1, and place T1 as the last element of L1,
gathers all strings from the main list L0 into a list LST1,and place it as the first element of T1
gathers all integers from the main list L0 into a tuple TINT, as last element of LST1
prints the given list L0 and L1
"""


"""
L0 = [
# More complex test case
("This", "should", "be", "a"),
("fun", "little", "list", "that", "contains", "a", "list", ["I'm", "a", "list"]),
["And", "I'm", "a", "tuple"],
["that", "contains", "a", "tuple", ("I'm", "a", "tuple"), "and", "starts", "with", "a", "list", "of", "strings"],
"And", "I'm", "a", "list", "of", "strings", "ending", "in", "a", "tuple", "of", "numbers",
1, 2, 3, 4, 5, 
]
"""

# Simple test case
L0 = [
["hello", "I'm", "bob"],
1,
2,
3,
"hello",
"I'm",
"Zohar",
["who", "are", "you", 7],
(4, 5, 6),
(7, 8, "turtles")
]


L1 =[]
T1 = ()
LST1 = []
TINT = ()
for element in L0:
    # Check if each element is a tuple, list, string, or int, using the isinstance function

    if isinstance(element, tuple):
        # If element of outer list is tuple, take each member of that tuple and add to list L1
        for tuple_element in element:
            L1.append(tuple_element)

    if isinstance(element, list):
        # If element of outer list is list, take each member of that tuple and add to tuple T1
        for list_element in element:
            T1 += (list_element, )

    if isinstance(element, str):
        # If element of outer list is a string, add the string to list LST1
        LST1.append(element)

    if isinstance(element, int):
        # If element of outer list is an int, add the int to tuple TINT
        TINT += (element, )

# Print all of them just to check they're right
print("L0")
print(L0)
print("L1")
print(L1)
print("T1")
print(T1)
print("LST1")
print(LST1)
print("TINT")
print(TINT)
print()

# Make TINT the last element of LST1
LST1.append(TINT)
print("LST1 with TINT added to end")
print(LST1)
print()
# Make LST1 the first element of T1
print("T1 with new LST1 added to beginning")
T1 = (LST1, ) + T1
print(T1)
print()
# Make T1 the last element of L1
print("L1 with new T1 added to end")
L1.append(T1)
print(L1)



