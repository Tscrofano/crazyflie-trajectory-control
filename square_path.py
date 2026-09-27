"""Takeoff, fly a square pattern, and land for one CF in simulation."""

from crazyflie_py import Crazyswarm

TAKEOFF_DURATION = 2.5
HOVER_DURATION = 2.0
FLIGHT_DURATION = 3.0  # Time allowed to fly between each corner
LAND_DURATION = 2.5

def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf = swarm.allcfs.crazyflies[0]

    # 1. Takeoff to 1 meter high
    print("Taking off...")
    cf.takeoff(targetHeight=1.0, duration=TAKEOFF_DURATION)
    timeHelper.sleep(TAKEOFF_DURATION + HOVER_DURATION)

    # 2. Fly the square pattern [X, Y, Z]
    # Corner 1: Move forward 1 meter
    print("Moving to Corner 1...")
    cf.goTo(goal=[0.5, 0.0, 1.0], yaw=0.0, duration=FLIGHT_DURATION)
    timeHelper.sleep(FLIGHT_DURATION + HOVER_DURATION)

    # Corner 2: Move left 1 meter
    print("Moving to Corner 2...")
    cf.goTo(goal=[0.5, 0.5, 1.0], yaw=0.0, duration=FLIGHT_DURATION)
    timeHelper.sleep(FLIGHT_DURATION + HOVER_DURATION)

    # Corner 3: Move back 1 meter
    print("Moving to Corner 3...")
    cf.goTo(goal=[0.0, 0.5, 1.0], yaw=0.0, duration=FLIGHT_DURATION)
    timeHelper.sleep(FLIGHT_DURATION + HOVER_DURATION)

    # Corner 4: Return to the start position above the launch pad
    print("Returning to home position...")
    cf.goTo(goal=[0.0, 0.0, 1.0], yaw=0.0, duration=FLIGHT_DURATION)
    timeHelper.sleep(FLIGHT_DURATION + HOVER_DURATION)

    # 3. Land safely
    print("Landing...")
    cf.land(targetHeight=0.04, duration=LAND_DURATION)
    timeHelper.sleep(LAND_DURATION)
    print("Flight complete!")

if __name__ == '__main__':
    main()
