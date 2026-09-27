# Crazyflie Trajectory Control

Velocity/position-based flight controllers for Crazyflie drones in simulation, built with `crazyflie_py` (Crazyswarm2). Includes three trajectory types: a multi-drone swarm checkpoint route, a single-drone circular path, and a single-drone square pattern.

## Requirements

- ROS2
- [Crazyswarm2](https://imrclab.github.io/crazyswarm2/)
- Python 3
- numpy

Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

crazyflie-trajectory-control/
├── multi_waypoint/ # Swarm flies through 3 checkpoints, then returns home
├── circular/ # Single drone flies a circular path
├── square/ # Single drone flies a square pattern
└── requirements.txt


## Running

Each script assumes a running Crazyswarm2 simulation backend. Launch your sim environment first, then run the desired script:

```bash
cd ~/path/to/crazyflie-trajectory-control/multi_waypoint
python3 multi_waypoint.py
```

```bash
cd ~/path/to/crazyflie-trajectory-control/circular
python3 circular.py
```

```bash
cd ~/path/to/crazyflie-trajectory-control/square
python3 square.py
```

### Multi-Waypoint (Swarm)
Takes off the full swarm, flies each drone through the same three relative checkpoints (preserving each drone's individual starting offset), then returns every drone to its own start position and lands.

### Circular
Takes off a single drone and flies a circular path of radius 0.5m around a fixed center point, using a stepped `goTo` loop to approximate continuous motion.

### Square
Takes off a single drone and flies a 0.5m square pattern through four corners before returning home and landing.

## Notes

- All scripts use `goTo` for position-based waypoint tracking rather than raw velocity commands.
- Hover pauses are inserted between waypoints to let the sim settle before issuing the next command.
