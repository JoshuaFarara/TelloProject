from djitellopy import tello
from time import sleep  # add some delays between each command

# before running the program ensure the tello drone is connected via wifi
me = tello.Tello() # creates a tello object for the drone
me.connect() # connects to the drone, takes care of ip address and communication for you
print(me.get_battery()) # shows battery percentage

# me.takeoff()
# # send_rc_control(self, left_right_velocity: int, forward_backward_velocity: int, up_down_velocity: int,  yaw_velocity: int):
# me.send_rc_control(0, 50, 0, 0)
# sleep(2)
# me.send_rc_control(0, -50, 0, 0)
# sleep(2)
# me.send_rc_control(0, 0, 0, 0)
# me.land()
