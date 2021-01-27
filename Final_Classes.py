# HERE I SET UP VEHICLES -------------------------------------------------------------------
class Vehicle:
    '''
    This is the parent class for all the vehicles that are going to follow, all these attributes are consistent
    across all vehicles
    '''
    def __init__(self, name, cap, x, y, destination, speed, position):
        self.name = name
        self.capacity = cap
        self.passengers = []
        self.x = x
        self.y = y
        self.destination = destination
        self.speed = speed
        self.route = None
        self.position = position
        self.location = None

    def getCap(self):
        return self.capacity

    def getPassengers(self):
        return self.passengers

    def getPosition(self):
        return self.position

    def getRoute(self):
        return self.route

    def getSpeed(self):
        return self.speed

    def getName(self):
        return self.name

    def setRoute(self, route):
        self.route = route

    def addPassenger(self, person):
        self.passengers.append(person)

    def next(self):
        self.position += 1

    def full(self):
        return len(self.passengers) == self.capacity

    def movetowardsdest(self, destination):
        if self.x < destination.x:
            if self.x + self.speed <= destination.x:
                self.x += self.speed
            if destination.x - self.x < self.speed:
                self.x += destination.x - self.x
        if self.x > destination.x:
            if self.x - self.speed >= destination.x:
                self.x -= self.speed
            if destination.x - self.x < self.speed:
                self.x = destination.x - self.x
        if self.y < destination.y:
            if self.y + self.speed <= destination.y:
                self.y += self.speed
            if destination.y - self.y < self.speed:
                self.y += destination.y - self.y
        if self.y > destination.y:
            if self.y - self.speed >= destination.y:
                self.y -= self.speed
            if destination.y - self.y < self.speed:
                self.y = destination.y - self.y


    def location(self):
        return self.route[self.position]

    def getDestination(self):
        return self.destination

    def newDestination(self):
        return self.route[(self.position + 1) % len(self.route)]

class Airplane(Vehicle):

    def __init__(self, name, cap, x, y, destination, speed, position, takeoff):
        Vehicle.__init__(self, name, cap, x, y, destination, speed, position)
        self.cost = 100
        self.takeoff = takeoff
       # self.precheckin = checkin
       # self.postcheckin = checkout

    def getCost(self):
        return 100 # this is the cost of an airplane ticket

class Car(Vehicle):
    def __init__(self, name, cap, x, y, destination, speed, position, cost):
        Vehicle.__init__(self, name, cap, x, y, destination, speed, position)
        self.cost = 25

    def getCost(self):
        return 25

class Taxi(Vehicle):

    def __init__(self, name, cap, x, y, destination, speed, position, takeoff):
        Vehicle.__init__(self, name, cap, x, y, destination, speed, position)
        self.cost = 15
        self.takeoff = takeoff
    def getCost(self):
        return 15

class Bus(Vehicle):
    def __init__(self, name, cap, positionx, positiony, destination, speed, position):
        Vehicle.__init__(self, name, cap, positionx, positiony, destination, speed, position)
        self.cost = 1

    def getCost(self):
        return 1

class Bicycle(Vehicle):
    def __init__(self, name, cap, x, y, destination, speed, position):
        Vehicle.__init__(self, name, cap, x, y, destination, speed, position)

class Train(Vehicle):
    def __init__(self, name, cap, positionx, positiony, destination, speed, position):
        Vehicle.__init__(self, name, cap, positionx, positiony, destination, speed, position)
        self.cost = 15

    def getCost(self):
        return 15

# HERE I SET UP TOWNS --------------------------------------------------------------------------------------------------
class Town:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.roads = []
        self.rails = []
        self.population = []

    def getName(self):
        return self.name

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getRoads(self):
        return self.roads

    def getPopulation(self):
        return self.population

    def setPopulation(self, population):
        self.population = population

    def addRoad(self, road):
        if road not in self.roads:
            self.roads.append(road)

    def addRail(self, rail):
        if rail not in self.rails:
            self.rails.append(rail)

    def addPerson(self, person):
        return self.population.append(person)


# HERE I SET UP CONNECTIONS/ROADS ------------------------------------------------------------------------------------
''''
class Connections:

    def __init__(self, townA, townB, length):
        self.start = townA
        self.end = townB
        self.length = length

class Road(Connections):
    def __init__(self, townA, townB, length):
        Connections.__init__(self, townA, townB, length)
class Airpath(Connections):
    def __init__(self, townA, townB, length):
        Connections.__init__(self, townA, townB, length)
class Rail(Connections):
    def __init__(self, townA, townB, length):
        Connections.__init__(self, townA, townB, length)

'''
# instead of making it continuous, have it discrete...
# route might consist of x number of points along the way
# make sure the increments is along the connection
# function that each roads can be a line?

# HERE I SET UP PEOPLE ------------------------------------------------------------------------------------------
class Person:

    def __init__(self, name, location, destination, cash):
        self.name = name
        self.location = location
        self.destination = destination
        self.cash = cash

    def getName(self):
        return self.name
    def getLocation(self):
        return self.location
    def getDestination(self):
        return self.destination
    def getCash(self):
        return self.cash
    def setLocation(self, location):
        self.location = location

    def transfercash(self, transportation):
        self.cash = self.cash - transportation.cost



