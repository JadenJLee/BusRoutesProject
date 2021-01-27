import random
import tkinter as tk
from tkinter import *
from PIL import ImageTk
from Final_Classes import *


def read_lines(filename):
    """
    Returns all of the lines of text in a list, read from the file
    corresponding to the string filename.
    """
    out = []
    with open(filename, 'r') as file:
        for line in file.read().splitlines(): #loops over each line in file, not including newline
            out.append(line)
    return out

def createTown(nameoffile):
    '''
    Just to make the town load up from the file that has plain text in it
    '''
    townlist = read_lines(nameoffile)
    for a in range(len(townlist)):
        towninfo = townlist[a].split()
        town = towninfo[0]
        x = int(towninfo[1])
        y = int(towninfo[2])

        townlist[a] = (Town(town, x, y))#this initializes the object with the attributes of the town.

    return townlist

def createRoutes(nameoffile, townlist):
    '''
    essentially we are making routes that go in a circular pattern, takes the townlist from the towns we created above
    and make routes that routinely go through each town
    '''

    routelist = read_lines(nameoffile)
    for x in range(len(routelist)):
        routelist[x] = routelist[x].split() # Each line gets a list of its town names
    for x in range(len(routelist)): #this loops through all strings that are lists inside lists aka matrices sorta
        for y in range(len(routelist[x])):
            for z in range(len(townlist)):
                if routelist[x][y] == townlist[z].getName():
                    routelist[x][y] = townlist[z]

    for route in routelist:
        routelength = len(route)
        for x in range(routelength):
            next = (x + 1) % routelength
            previous = (x - 1) % routelength

    return routelist

def createPeople(nameoffile, townlist):
    '''
    info 0 will be id, info 1 will be location, info 2 will be destination, info 3 will be cash value
    '''
    peoplelist = read_lines(nameoffile)
    for x in range(len(peoplelist)):
        info = peoplelist[x].split() # this is done to split up the person's information from the textfile to separate lines
        personsid = info[0]
        location = info[1]
        destination = info[2]
        cash = int(info[3])


        for town in townlist:
            if location == town.getName():
                location = town
            if destination == town.getName():
                destination = town

        if location == None:
            location = None

        if type(destination) != Town:
            print('error')
            print(destination)
        peoplelist[x] = Person(personsid, location, destination, cash)
        if not location is None:
            location.addPerson(peoplelist[x])

    return peoplelist

def createBus(nameoffile, routelist, allpeoplelist):
    buslist = read_lines(nameoffile)

    for x in range(len(buslist)):
        businfo = buslist[x].split()
        name = businfo[0]
        capacity = businfo[1]
        positionx = int(businfo[2])
        positiony = int(businfo[3])
        destination = businfo[4]
        speed = int(businfo[5])
        position = int(businfo[6])
        buspassengers = []

        for passenger_name in businfo[7:]:
            for passenger in allpeoplelist:
                if passenger_name == passenger.getName():
                    buspassengers.append(passenger)

        buslist[x] = Bus(name, capacity, positionx, positiony, destination, speed, position)

    for x in range(len(buslist)):
        buslist[x].setRoute(routelist[x])

    return buslist

def createAirplane(nameoffile, routelist, allpeoplelist):
    airplanelist = read_lines(nameoffile)

    for a in range(len(airplanelist)):
        airplaneinfo = airplanelist[a].split()
        name = airplaneinfo[0]
        capacity = airplaneinfo[1]
        x = int(airplaneinfo[2])
        y = int(airplaneinfo[3])
        destination = airplaneinfo[4]
        speed = int(airplaneinfo[5])
        position = int(airplaneinfo[6])
        takeoff = int(airplaneinfo[7])
        airplanepassengers = []

        for passenger_name in airplaneinfo[8:]:
            for passenger in allpeoplelist:
                if passenger_name == passenger.getName():
                    airplanepassengers.append(passenger)

        airplanelist[a] = Airplane(name, capacity, x, y, destination, speed, position, takeoff)

    for x in range(len(airplanelist)):
        airplanelist[x].setRoute(routelist[x])

    return airplanelist

def createTrain(nameoffile, routelist, allpeoplelist):
    trainlist = read_lines(nameoffile)

    for a in range(len(trainlist)):
        traininfo = trainlist[a].split()
        for x in range(len(trainlist)):
            traininfo = trainlist[x].split()
            name = traininfo[0]
            capacity = traininfo[1]
            positionx = int(traininfo[2])
            positiony = int(traininfo[3])
            destination = traininfo[4]
            speed = int(traininfo[5])
            position = int(traininfo[6])
            trainpassengers = []

            for passenger_name in traininfo[7:]:
                for passenger in allpeoplelist:
                    if passenger_name == passenger.getName():
                        trainpassengers.append(passenger)

            trainlist[x] = Train(name, capacity, positionx, positiony, destination, speed, position)

        for x in range(len(trainlist)):
            trainlist[x].setRoute(routelist[x])

        return trainlist

def createTaxi(nameoffile, routelist, allpeoplelist):
    taxilist = read_lines(nameoffile)

    for a in range(len(taxilist)):
        for x in range(len(taxilist)):
            taxiinfo = taxilist[x].split()
            name = taxiinfo[0]
            capacity = taxiinfo[1]
            positionx = int(taxiinfo[2])
            positiony = int(taxiinfo[3])
            destination = taxiinfo[4]
            speed = int(taxiinfo[5])
            position = int(taxiinfo[6])
            takeoff = int(taxiinfo[7])
            taxipassengers = []

            for passenger_name in taxiinfo[8:]:
                for passenger in allpeoplelist:
                    if passenger_name == passenger.getName():
                        taxipassengers.append(passenger)

            taxilist[x] = Taxi(name, capacity, positionx, positiony, destination, speed, position, takeoff)

        for x in range(len(taxilist)):
            taxilist[x].setRoute(routelist[x])

        return taxilist

def createCars(nameoffile, routelist, allpeoplelist):
    carlist = read_lines(nameoffile)

    for a in range(len(carlist)):
        carinfo = carlist[a].split()
        for x in range(len(carlist)):
            carinfo = carlist[x].split()
            name = carinfo[0]
            capacity = carinfo[1]
            positionx = int(carinfo[2])
            positiony = int(carinfo[3])
            destination = carinfo[4]
            speed = int(carinfo[5])
            position = int(carinfo[6])
            cost = 25
            carpassengers = []

            for passenger_name in carinfo[7:]:
                for passenger in allpeoplelist:
                    if passenger_name == passenger.getName():
                        carpassengers.append(passenger)

            carlist[x] = Car(name, capacity, positionx, positiony, destination, speed, position, cost)

        for x in range(len(carlist)):
            carlist[x].setRoute(routelist[x])

        return carlist

def createBike(nameoffile, routelist, allpeoplelist):
    bikelist = read_lines(nameoffile)

    for a in range(len(bikelist)):
        bikeinfo = bikelist[a].split()
        for x in range(len(bikelist)):
            bikeinfo = bikelist[x].split()
            name = bikeinfo[0]
            capacity = bikeinfo[1]
            positionx = int(bikeinfo[2])
            positiony = int(bikeinfo[3])
            destination = bikeinfo[4]
            speed = int(bikeinfo[5])
            position = int(bikeinfo[6])
            bikepassengers = []

            for passenger_name in bikeinfo[7:]:
                for passenger in allpeoplelist:
                    if passenger_name == passenger.getName():
                        bikepassengers.append(passenger)

            bikelist[x] = Bicycle(name, capacity, positionx, positiony, destination, speed, position)

        for x in range(len(bikelist)):
            bikelist[x].setRoute(routelist[x])

        return bikelist


def movepeople(vehicle, town):
    print(vehicle.getName() + " has arrived at " + town.getName())

    peopleintown = town.getPopulation()
    initialpeopleintown = len(peopleintown) #this is to make sure this is a constant that doesnt change after every 'pop'
    townName = town.getName()
    amountofpeopleinformation = townName + " contains " + str(initialpeopleintown) + " people. Here are their names and " \
                                                                                        "their destinations"
    information = destinationandperson(peopleintown)

    if information == '':
        print(townName + " is empty!")
    else:
        print(amountofpeopleinformation)
        print(information)

    departed = 0
    passengers = vehicle.getPassengers()
    a = 0
    while int(a) < len(passengers):
        if passengers[a].getDestination() == town:
            bounce = passengers.pop(a)
            town.addPerson(bounce)
            bounce.setLocation(town)
            print(bounce.getName() + " has gotten off " + vehicle.getName())
            departed += 1
        else:
            a += 1
    if departed == 0:
        print("Nobody got off at this town!")

    peopleremaining = []

    for person in peopleintown:
        if person.getDestination() in vehicle.getRoute() and not vehicle.full() and person.getDestination() != town:
            person.cash -= vehicle.getCost()
            if person.cash < 0:
                print(person.getName() + " doesn't have enough money to ride " + vehicle.getName())
                peopleremaining.append(person)
                continue
            vehicle.addPassenger(person)
            print(person.getName() + " has gotten on the " + vehicle.getName())
            person.setLocation(None)
        else:
            peopleremaining.append(person)

    town.setPopulation(peopleremaining)

def destinationandperson(people):
    output = ""
    for person in people:
        destination = person.getDestination()
        output += '(' + person.getName() + "," + destination.getName() + '), '
    return output

def givepeopleinfo(peoplelist):
    for person in peoplelist:
        print("Name: " + person.getName())
        print("Money: " + str(person.getCash()))
        print("Destination: " + person.getDestination().getName())

def mainfunction(filename):

    sim = Simulation(filename)

    def enter():
        sim.enter()
        w.delete('all')
        drawings(w, sim, img)

    def getpeopleinfo():
        print(givepeopleinfo(sim.people))

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    button = tk.Button(frame,
                       text="QUIT",
                       fg="red",
                       command=quit)
    button.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                       text="Next",
                       command=enter)
    slogan.pack(side=tk.LEFT)

    peoplebutton = tk.Button(frame,
                       text="Show People Info",
                       command=getpeopleinfo)
    peoplebutton.pack(side=tk.LEFT)


    canvas_width = 1000
    canvas_height = 1000
    w = Canvas(root,
               width=canvas_width,
               height=canvas_height)
    w.pack(expand = True, fill = BOTH)

    w.configure(scrollregion=w.bbox("all")) #this essentially centers the canvas on the page
    img = ImageTk.PhotoImage(file="Newyorkstate.gif")


    root.mainloop()

def drawings(w, sim, img):
    w.create_image(-50, -50, image=img, anchor=NW)
    scaling = 30

    w.create_text(50, 700, text = "global time: " + str(sim.globaltime))

    for town in sim.towns:
        w.create_rectangle(((town.x) * scaling)+50, ((town.y) * scaling)+50, ((town.x * scaling)+25)+50, ((((town.y) * scaling))+25)+50)
        w.create_text(town.x * scaling+50, town.y * scaling+50, text = town.getName())
    #w.create_line(((town.x) * scaling)+25, ((town.y) * scaling)+25, ((town.x * scaling)+25)+50), (((town.y) * scaling))+25)+50

    for vehicle in sim.allvehicles:
        color = "orange"
        if type(vehicle) == Airplane:
            color = "red"
        if type(vehicle) == Bicycle:
            color = "black"
        if type(vehicle) == Car:
            color = "blue"
        if type(vehicle) == Taxi:
            color = "yellow"
        if type(vehicle) == Train:
            color = "brown"
        if type(vehicle) == Bus:
            color = "green"

        w.create_oval(vehicle.x*scaling+50, vehicle.y*scaling+50, vehicle.x*scaling+25+50, vehicle.y*scaling+25+50, fill = color)

        w.create_text(vehicle.x*scaling+50, vehicle.y*scaling+50, text = vehicle.getName())




class Simulation:
    def __init__(self, filename):
        self.filename = filename
        self.towns = createTown(filename[0])
        self.routes = createRoutes(filename[1], self.towns)
        self.people = createPeople(filename[2], self.towns)
        self.buses = createBus(filename[3], self.routes, self.people)
        self.airplanes = createAirplane(filename[4], self.routes, self.people)
        self.trains = createTrain(filename[5], self.routes, self.people)
        self.taxis = createTaxi(filename[6], self.routes, self.people)
        self.cars = createCars(filename[7], self.routes, self.people)
        self.bikes = createBike(filename[8], self.routes, self.people)

        self.globaltime = 0
        self.allvehicles = self.buses + self.airplanes + self.trains + self.taxis + self.cars + self.bikes

    def enter(self):
        for vehicle in self.allvehicles:
            currenttown = None
            for town in self.towns:
                if vehicle.x == town.x and vehicle.y == town.y:
                    currenttown = town
            if not currenttown is None:
                vehicle.location = currenttown
                vehicle.destination = vehicle.newDestination()
                print()
                movepeople(vehicle, currenttown)
                print()
                informationaboutpassengers = destinationandperson(vehicle.getPassengers())
                if not informationaboutpassengers == "":
                    print("The passengers' of vehicle " + vehicle.getName() + "names and destinations are... ")
                    print(informationaboutpassengers)
                else:
                    print(vehicle.getName() + " is completely empty!")
                print()
                if vehicle.location == vehicle.newDestination():
                    vehicle.position += 1
                print("The " + vehicle.getName() + "\'s coordinates are: " + str(vehicle.x) + ', '+ str(vehicle.y))
            if type(vehicle) == Taxi:
                if vehicle.full:
                    if self.globaltime >= vehicle.takeoff + 1:
                        if vehicle.location == vehicle.newDestination():
                            continue
                        vehicle.movetowardsdest(vehicle.newDestination())
                        print("The " + vehicle.getName() + "\'s coordinates are: " + str(vehicle.x) + ', ' + str(
                            vehicle.y))
                        print("destination for " + vehicle.getName() + " is: " + vehicle.newDestination().getName())
            elif type(vehicle) == Airplane:
                if self.globaltime == vehicle.takeoff - 2:
                    print(vehicle.getName() + " is boarding")
                if self.globaltime >= vehicle.takeoff:
                    if vehicle.location == vehicle.newDestination():
                        continue
                    vehicle.movetowardsdest(vehicle.newDestination())
                    print("The " + vehicle.getName() + "\'s coordinates are: " + str(vehicle.x) + ', ' + str(vehicle.y))
                    print("destination for " + vehicle.getName() + " is: " + vehicle.newDestination().getName())
                if self.globaltime == vehicle.takeoff + 1:
                    print(vehicle.getName() + "is unloading")
            else:
                vehicle.movetowardsdest(vehicle.newDestination())
                print("The " + vehicle.getName() + "\'s coordinates are: " + str(vehicle.x) + ', ' + str(vehicle.y))
                print("destination for " + vehicle.getName() + " is: " + vehicle.newDestination().getName())

        #
        self.globaltime += 1
        print()
        print(str(self.globaltime) + " hours have passed!")

file_names = "FinalTowns.txt", "FinalRoutes.txt", "FinalPeople.txt", "FinalBus.txt", "FinalAirplanes.txt",\
              "FinalTrains.txt", "FinalTaxis.txt", "FinalCars.txt", "FinalBikes.txt"

if __name__ == '__main__':
    mainfunction(file_names)
