from djitellopy import tello
from time import sleep

me = tello.Tello() # creates a tello object for the drone
me.connect() # connects to the drone, takes care of ip address and communication for you
print(me.get_battery()) # shows battery percentage


# def __check__battery