class House:
    def __init__(self, name, numberOfFloors):
        self.name = name
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self,floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.setNewNumberOfFloors(5)
h2.setNewNumberOfFloors(10)