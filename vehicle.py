class Vehicle:
    def __init__(self , name, brand, speed, kms):
        self.name = name
        self.brand = brand
        self.speed = speed
        self.kms = kms

class Boat(Vehicle):
    def __init__(self, name, brand, speed, kms, isArmy):
        Vehicle.__init__(self, name, brand, speed, kms)
        self.isArmy = isArmy

    def isArmy(self):
        return self.isArmy()

class Car(Vehicle):
    def __init__(self, name, brand, speed, kms, color, isDiesel, nbOfSeats, year):
        Vehicle.__init__(self, name, brand, speed, kms)
        self.color = color
        self.isDiesel = isDiesel
        self.nbOfSeats = nbOfSeats
        self.year = year

class Bike(Vehicle):
    def __init__(self, name, brand, speed, kms, color, motor):
        Vehicle.__init__(self, name, brand, speed, kms)
        self.color = color
        self.motor = motor

class Plane(Vehicle):
    def __init__(self, name, brand, speed, kms, isArmy):
        Vehicle.__init__(self, name, brand, speed, kms)
        self.isArmy = isArmy

    def isArmy(self):
        return self.isArmy()