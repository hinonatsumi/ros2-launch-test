from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    parameter = Node(
        package='tutorial_parameter',
        executable='parameter',
        parameters=[
            {'int_val':100},
            {'double_val':100.0},
            {'str_val':'goodbye'}
        ]
    )
    return LaunchDescription([
        parameter
        ])
