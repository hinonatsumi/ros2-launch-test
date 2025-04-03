from os.path import join
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription

def generate_launch_description():
    pkg_prefix = get_package_share_directory('tutorial_launch')
    launch_path1 = join(pkg_prefix, 'launch/server.launch.py')
    launch_path2 = join(pkg_prefix, 'launch/client.launch.py')
    node1 = IncludeLaunchDescription(PythonLaunchDescriptionSource(launch_path1))
    node2 = IncludeLaunchDescription(PythonLaunchDescriptionSource(launch_path2))
    return LaunchDescription([
        node1,
        node2
        ])
