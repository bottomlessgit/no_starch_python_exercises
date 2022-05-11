print("Please input two integers, and we will print their sum:")
try:
    num1 = int(input("input the first number: "))
    num2 = int(input("input the second number: "))
    sum = num1 + num2
    print(str(num1) + " + " + str(num2) + " = " + str(sum))
except ValueError:
    print("You've input a non-integer value!")