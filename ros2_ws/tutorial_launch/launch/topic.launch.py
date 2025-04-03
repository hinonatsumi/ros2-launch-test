from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    node1 = Node(
        package='tutorial_topic',
        executable='publisher'
        output={
            'stdout': 'log',
            'stderr': 'log'
    )
    node2 = Node(
        package='tutorial_topic',
        executable='subscriber'
        )
    return LaunchDescription([
        node1,
        node2
        ])
