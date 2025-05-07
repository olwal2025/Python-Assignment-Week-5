class Animal:
    def move(self):
        print("This animal moves in its own way.")

class Lion(Animal):
    def move(self):
        print(" The lion prowls stealthily across the savannah.")

class Eagle(Animal):
    def move(self):
        print(" The eagle soars high above the mountains and valleys.")

class Elephant(Animal):
    def move(self):
        print(" The elephant walks slowly through the jungle.")

class Snake(Animal):
    def move(self):
        print(" The snake slithers silently along the forest paths.")

def main():
    animals = [Lion(), Eagle(), Elephant(), Snake()]
    print(" Wild Animal Movements:")
    for animal in animals:
        animal.move()

if __name__ == "__main__":
    main()
