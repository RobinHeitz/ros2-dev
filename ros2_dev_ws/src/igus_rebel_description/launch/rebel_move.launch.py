import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
# from launch_ros.actions import Node

def generate_launch_description():

    # use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    pkg_share = launch_ros.substitutions.FindPackageShare(package='igus_rebel_description').find('igus_rebel_description')
    default_model_path = os.path.join(pkg_share, 'urdf/igus_rebel.urdf')

    with open(default_model_path, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([
               
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}],
            arguments=[urdf]),
        
        Node(
            package='igus_rebel_description',
            executable='state_publisher',
            name='state_publisher',
            output='screen'),
    ])