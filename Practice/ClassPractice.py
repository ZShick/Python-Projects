class World:
#creating a new class and its requirements
    name = "No Name Provided"
    solar_system = ""
    claimed_by = ""
    ID = 0
#defining how to initialize a new instance of this class
    def __init__(sphere, name, solar_system, claimed_by, ID):
        sphere.name = name
        sphere.solar_system = solar_system
        sphere.claimed_by = claimed_by
        sphere.ID = ID
#created a function that asks for input and then prints out one of two statements based on whether the information they gave matches up correctly
    def selectWorldTravel(self):
        world_name = input("Enter the name of the world you would like to visit: ")
        world_id = input("Enter that world's unique Galactic Travel ID #: ")
        if (world_name == self.name and world_id == self.ID):
            print("Have fun visiting {}!".format(world_name))
        else:
            print("The world name and/or world ID you entered are not in our system.")
        
#creating two instances of the World class
new_world = World("Earth", "Sol", "Humans", 1)
new_world = World("Mars", "Sol", "Martians", 2)
#creating two child classes off of World. Planet and Moon, each with unique attributes
class Planet(World):
    landable = True
    breathable = True

#1st polymorphism that shares a name with the function in the parent class. This one adds the new 'landable' boolean variable to communicate whether a planet is safe to land on or not
    def selectWorldTravel(self):
        planet_name = input("Enter the name of the planet you would like to visit: ")
        planet_id = input("Enter that planet's unique Galactic Travel ID #: ")
        if (planet_name == self.name and planet_id == self.ID and landable == True):
            print("Have fun visiting {}!".format(planet_name))
        elif (landable == False):
            print("There is not currently a safe way to land on this planet. Sorry!")
        else:
            print("The planet name and/or planet ID you entered are not in our system.")


class Moon(World):
    planet_orbiting = ""
    moon_number = 1
#similar to the above polymorphism, but this one asks for one extra piece of data (planet the moon is orbiting)
    def selectWorldTravel(self):
        moon_name = input("Enter the name of the moon you would like to visit: ")
        moon_id = input("Enter that moon's unique Galactic Travel ID #: ")
        orbit_around = input("Enter the name of the planet your desired destination moon is orbiting around: ")
        if (moon_name == self.name and moon_id == self.ID and orbit_around == self.planet_orbiting):
            print("Have fun visiting {}!".format(moon_name))
        else:
            print("The moon name and/or moon ID you entered are not in our system.")


travelWorld = World()
travelWorld.selectWorldTravel()

travelPlanet = Planet()
travelPlanet.selectWorldTravel()

travelMoon = Moon()
travelMoon.selectWorldTravel()
