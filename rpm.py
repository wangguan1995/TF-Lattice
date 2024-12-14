import numpy as np


def cal_rpm(velocity, radius):
    angle_velocity = velocity / radius
    rpm = 60 * angle_velocity / 2 * np.pi
    print(rpm)

# DrivAer ml
velocity = 38.889
radius = 0.318668
cal_rpm(velocity, radius)


# Rivian 
velocity = 30
radius = 0.4234265
cal_rpm(velocity, radius)
