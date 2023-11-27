import random

class Hat:
    def __init__(self):
        self.houses = ["Gryff", "HuffPuff", "Rave", "Slyth"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

hat = Hat()
hat.sort("Harry")

MEOWS = 3

for _ in range(MEOWS):
    print("meow")