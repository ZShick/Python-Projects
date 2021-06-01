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
#creating two instances of the World class
new_world = World("Earth", "Sol", "Humans", 1)
new_world = World("Mars", "Sol", "Martians", 2)
#creating two child classes off of World. Planet and Moon, each with unique attributes
class Planet(World):
    landable = True
    breathable = True

class Moon(World):
    planet_orbiting = ""
    moon_number = 1


#not sure how to check my work but running the module did not give me any errors.
