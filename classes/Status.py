class Status():
    def __init__(self, name, starting_amount):
        self.name = name
        self.amount = starting_amount
        if type(self) == Status:
            raise TypeError("<Status> must be subclasses")

    def getName(self):
        return self.name

    def getAmount(self):
        return self.amount

    def setAmount(self, amount):
        self.amount = min(100, amount)

class Health(Status):
    def __init__(self, starting_amount):
        super().__init__("Health", starting_amount)

class Hunger(Status):
    def __init__(self, starting_amount):
        super().__init__("Hunger", starting_amount)

class Fitness(Status):
    def __init__(self, starting_amount):
        super().__init__("Fitness", starting_amount)

class Energy(Status):
    def __init__(self, starting_amount):
        super().__init__("Energy", starting_amount)
