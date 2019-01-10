from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(x)


die_6 = Die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
print('\n')
die_10 = Die(10)
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
