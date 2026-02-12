import pandas as pd
df = pd.read_csv('planet_data.csv', index_col = 'eName')

df = df[["isPlanet","meanRadius", "orbit_type","orbits"]]

print(df.head())


class planet():
    def __init__(self,name, color = "blue", radius = 1):
        self.color = color
        self.radius = radius
        self.name = name
        self.moon_list = []
class moon():
    def __init__(self,name, color = "white", radius = 1,
                     tidally_locked=False, planet_companion =None):
        self.name = name
        self.radius = radius
        self.tidally_locked = tidally_locked
        self.planet_companion = planet_companion
    def update_planet(self):
        self.planet_companion.moon_list.append(self)

def print_largest(pl): #I did this whole thing for you - it selects the largest moon given a planet object 
    largest = None  #will be a moon type object
    for moon in pl.moon_list:
        if largest is None:
            largest = moon
        else:
            if largest.radius < moon.radius: largest = moon      
    if largest is not None:
        print(f"The largest moon of {pl.name} is {largest.name}")
