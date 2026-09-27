#!/usr/bin/env python3

import numpy as np
from crazyflie_py import Crazyswarm

def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf = swarm.allcfs.crazyflies[0]

    #Parameters
    Z = 1.0
    R = 0.5
    CIRCLE_TIME = 5.0

    TAKEOFF_TIME = 3.0
    LAND_TIME = 3.0

    #Take off
    cf.takeoff(targetHeight=Z, duration=TAKEOFF_TIME )
    timeHelper.sleep(TAKEOFF_TIME + 1.0) #tells the clock to give the sim time to run the take off then wait a second

    #start
    start = np.array(cf.initialPosition)


    #circle centers
    center1 = [0.5, 0]

    #circle1
    t = 0.0
    dt = 0.05
    while t < CIRCLE_TIME:
        theta = 2 * np.pi * (t/CIRCLE_TIME)
        x = center1[0] + R * np.cos(theta)
        y = center1[1] + R * np.sin(theta)

        cf.goTo(
            np.array([x, y, Z]),
            yaw = 0.0,
            duration = 5.0,
        )

        timeHelper.sleep(dt)  #this spaces out each iteration of the loop so it dosent give the sim too many inputs at once. 
         #without this it will send hundreds of outputs per second
        t += dt

    # Hover before land
    timeHelper.sleep(1.0)

    #Land
    cf.land(targetHeight=0.0, duration=LAND_TIME)
    timeHelper.sleep(LAND_TIME) #lets the drone land before giving it any more outputs.

if __name__ == "__main__":
    main()

