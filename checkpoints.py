#!/usr/bin/env python3

import numpy as np
from crazyflie_py import Crazyswarm 


def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cfs = allcfs.crazyflies

    Z = 1.0

    TAKEOFF_TIME = 3.0
    MOVE_TIME = 1.0
    HOVER_TIME = 3.0
    LAND_TIME = 3.0

    # Save each drone's starting position
    starts = [np.array(cf.initialPosition) for cf in cfs]

    # Takeoff
    print("Taking off...")
    allcfs.takeoff(targetHeight=Z, duration=TAKEOFF_TIME)
    timeHelper.sleep(TAKEOFF_TIME + 2.0)

    # Define three checkpoints (relative movement)
    checkpoints = [
        np.array([0.5, 0.0, Z]),
        np.array([0.5, 0.5, Z]),
        np.array([0.0, 0.5, Z]),
    ]

    # Fly through checkpoints
    for i, checkpoint in enumerate(checkpoints):
        print(f"Checkpoint {i+1}")

        for cf, start in zip(cfs, starts):
            target = np.array([
                start[0] + checkpoint[0],
                start[1] + checkpoint[1],
                Z
            ])

            cf.goTo(target, yaw=0.0, duration=MOVE_TIME)

        timeHelper.sleep(MOVE_TIME + HOVER_TIME)

    # Return home
    print("Returning home...")

    for cf, start in zip(cfs, starts):
        target = np.array([
            start[0],
            start[1],
            Z
        ])

        cf.goTo(target, yaw=0.0, duration=MOVE_TIME)

    timeHelper.sleep(MOVE_TIME + HOVER_TIME)

    # Land
    print("Landing...")
    allcfs.land(targetHeight=0.04, duration=LAND_TIME)
    timeHelper.sleep(LAND_TIME)


if __name__ == "__main__":
    main()
