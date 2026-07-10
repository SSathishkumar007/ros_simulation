import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share = get_package_share_directory('minimal_sim')
    urdf_path = os.path.join(pkg_share, 'urdf', 'minimal_bot.urdf')
    world_path = os.path.join(pkg_share, 'worlds', 'simple_maze.world')

    with open(urdf_path, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_desc}]
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
            ),
            # Add this line to load your specific world
            launch_arguments={'world': world_path}.items()
        ),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-file', urdf_path,  # Reads directly from the file instead of the topic
                '-entity', 'minimal_bot', 
                '-x', '1.0', 
                '-y', '1.0', 
                '-z', '0.1'
            ],
            output='screen'
        )
    ])