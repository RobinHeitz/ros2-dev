import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os

def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='rebel_test').find('rebel_test')
    default_model_path = os.path.join(pkg_share, 'urdf/rebel.urdf')

    model_arg = launch.actions.DeclareLaunchArgument(name="model", default_value=default_model_path, description="Absolute path to the robot urdf file.")
    launch_foxglove = launch.actions.DeclareLaunchArgument(name="foxglove", default_value=True, description="Launch foxglove node for 3D-View (alternative to RViz2)")

    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': Command(['xacro ', LaunchConfiguration('model')])}]
    )
    
    joint_state_publisher_node = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
    )

    foxglove_node = launch_ros.actions.Node(
        package='foxglove_bridge',
        executable='foxglove_bridge',
        name='foxglove_bridge',
    )

    return launch.LaunchDescription([
        model_arg,
        joint_state_publisher_node,
        robot_state_publisher_node,
        foxglove_node,
    ])