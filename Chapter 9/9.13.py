from random import randint

class Die:
    def __init__(self, sides=6) -> None:
        self.sides = sides
    
    def roll_die(self):
        return randint(1, self.sides)


d1 = Die()
print([d1.roll_die() for _ in range(10)])

d2 = Die(10)
print([d2.roll_die() for _ in range(10)])

d3 = Die(20)
print([d3.roll_die() for _ in range(10)])