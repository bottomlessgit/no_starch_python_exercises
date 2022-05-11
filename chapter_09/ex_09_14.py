from random import randint

class Dice():
    """class to simulate die and give random number from die sides"""
    def __init__(self, sides = 6):
        """initialize number of sides on die"""
        if sides and sides > 0:
            self.sides = sides
        else:
            self.sides = 6

    def roll_die(self):
        """prints random integer between 1 and sides (inclusive)"""
        print(randint(1, self.sides))


six_sided = Dice(-3)
print("We will now roll a " + str(six_sided.sides) +
      " sided die 10 times:")
for i in range(10):
    six_sided.roll_die()

ten_sided = Dice(10)
print("We will now roll a " + str(ten_sided.sides) +
      " sided die 10 times:")
for i in range(10):
    ten_sided.roll_die()

twenty_sided = Dice(20)
print("We will now roll a " + str(twenty_sided.sides) +
      " sided die 10 times:")
for i in range(10):
    twenty_sided.roll_die()
