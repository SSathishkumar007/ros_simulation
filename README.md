# 🤖 Minimal ROS 2 Robot Simulation

A beginner-friendly ROS 2 Humble project that demonstrates how to build a differential-drive robot from scratch, simulate it in Gazebo, perform SLAM mapping using a LiDAR sensor, visualize the robot in RViz2, and control it using the keyboard.

---

# Project Structure

```text
minimal_sim/
│
├── launch/
│   └── bringup.launch.py      # Launches Gazebo and spawns the robot
│
├── urdf/
│   └── minimal_bot.urdf       # Robot model and sensor description
│
├── worlds/
│   └── simple_maze.world      # Custom Gazebo environment
│
├── CMakeLists.txt             # Build configuration
├── package.xml                # ROS package information
├── README.md                  # Project documentation
└── LICENSE                    # Open-source license
```

---

# Folder Description

### 📁 launch/

Contains the ROS 2 launch files.

**bringup.launch.py**

* Starts Gazebo
* Loads the custom world
* Starts Robot State Publisher
* Spawns the robot into Gazebo

---

### 📁 urdf/

Contains the robot description.

**minimal_bot.urdf**

Defines

* Robot chassis
* Left wheel
* Right wheel
* Wheel joints
* LiDAR sensor
* Robot dimensions
* Gazebo Differential Drive Plugin
* Gazebo LiDAR Plugin

---

### 📁 worlds/

Contains Gazebo simulation environments.

**simple_maze.world**

Creates

* Ground plane
* Sun
* Four surrounding walls
* Center obstacle
* Maze environment

---

### 📄 CMakeLists.txt

Specifies how the package is built and installs the **launch**, **urdf**, and **worlds** folders.

---

### 📄 package.xml

Contains

* Package name
* Dependencies
* Version
* Author
* License

---

# Software Requirements

* Ubuntu 22.04
* ROS 2 Humble
* Gazebo
* RViz2
* SLAM Toolbox
* Teleop Twist Keyboard

---

# Step 1 : Create the Workspace

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```

---

# Step 2 : Create the ROS 2 Package

```bash
ros2 pkg create --build-type ament_cmake minimal_sim --dependencies rclcpp robot_state_publisher gazebo_ros nav2_bringup
```

---

# Step 3 : Create Required Folders

```bash
cd minimal_sim
mkdir launch urdf worlds
```

---

# Step 4 : Create the Robot Model

Create the file

```text
urdf/minimal_bot.urdf
```

Paste the URDF robot model provided in this repository.

This file defines

* Robot body
* Wheels
* LiDAR sensor
* Gazebo plugins
* Robot physics

---

# Step 5 : Create the Gazebo World

Create

```text
worlds/simple_maze.world
```

Paste the world file available in this repository.

This creates

* Closed room
* Four walls
* Center obstacle
* Ground plane

---

# Step 6 : Create the Launch File

Create

```text
launch/bringup.launch.py
```

Paste the launch file provided in this repository.

The launch file

* Starts Gazebo
* Loads the world
* Publishes robot state
* Spawns the robot

---

# Step 7 : Update CMakeLists.txt

Before

```cmake
ament_package()
```

add

```cmake
install(DIRECTORY
  launch
  urdf
  worlds
  DESTINATION share/${PROJECT_NAME}
)
```

---

# Step 8 : Build the Package

Go to the workspace.

```bash
cd ~/ros2_ws
```

Build.

```bash
colcon build --symlink-install
```

Source the workspace.

```bash
source install/setup.bash
```

---

# Step 9 : Run the Simulation

## Terminal 1

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch minimal_sim bringup.launch.py
```

This starts Gazebo and spawns the robot.

---

## Terminal 2

```bash
source /opt/ros/humble/setup.bash
ros2 launch slam_toolbox online_async_launch.py use_sim_time:=true
```

Starts SLAM mapping.

---

## Terminal 3

```bash
source /opt/ros/humble/setup.bash
rviz2
```

Configure RViz

* Fixed Frame → `map`
* Add **Map**
* Add **RobotModel**
* Add **LaserScan**
* Set LaserScan Topic → `/scan`

---

## Terminal 4

```bash
source /opt/ros/humble/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Use the keyboard to move the robot around the maze while RViz builds the map in real time.

---

# Features

* Differential Drive Robot
* URDF Robot Model
* Gazebo Simulation
* Custom Maze
* LiDAR Sensor
* SLAM Mapping
* RViz Visualization
* Keyboard Teleoperation

---

# Future Improvements

* Navigation2 (Nav2)
* Autonomous Navigation
* AMCL Localization
* Obstacle Avoidance
* Camera Integration
* Path Planning

---

# Author

**S Sathish Kumar**

Robotics and Automation Engineering

Sahyadri College of Engineering and Management
