from planet_classes import *
import pytest

earth = planet(name ="Earth",color = "blue",radius = 324.3)
mars = planet(name = "Mars",color = "red",radius =250.4)
mercury = planet(name = "Mercury",color ="grey",radius =100.3)
luna = moon(name= "Luna", radius = 300.4,tidally_locked = True, planet_companion = earth)
nave = moon(name = "Nave", radius = 289.4, tidally_locked = False, planet_companion = mars)
nana = moon(name = "Nana", radius = 99.99, tidally_locked = True, planet_companion = mercury)
major = moon(name = "Major", radius = 1231.3, tidally_locked = True, planet_companion = earth)

major.update_planet()
luna.update_planet()
nave.update_planet()
nana.update_planet()

def test_planet_update():
    first_moon = earth.moon_list[0]
    assert first_moon.name == "Luna"
    assert second_moon.name == "Major"


print_largest(earth)
print_largest(mars)
print_largest(mercury)

