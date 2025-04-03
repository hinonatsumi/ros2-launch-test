from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    node = Node(
        package='tutorial_service',
        executable='service_server'
    )
    return LaunchDescription([
        node
        ])
