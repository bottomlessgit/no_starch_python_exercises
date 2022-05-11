print("This program repeatedly takes the input of two integers and"
      " prints their sum.\nTo exit, input a non-integer value.")
while True:
    try:
        num1 = int(input("input the first number: "))
        num2 = int(input("input the second number: "))
        sum = num1 + num2
        print(str(num1) + " + " + str(num2) + " = " + str(sum))
    except ValueError:
        print("You've input a non-integer value!\nGoodbye!")
        break