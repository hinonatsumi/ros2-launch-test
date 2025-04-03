from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    node1 = Node(
        package='tutorial_topic',
        executable='subscriber_async'
    )
    node2 = Node(
        package='tutorial_topic',
        executable='publisher',
        name='publisher1'
        remappings=[
            ('/number', '/number1')
            ]
        )
    node3 = Node(
	package='tutorial_topic',
	executable='publisher',
        name='publisher2'
        remappings=[
            ('/number', '/number2')
            ]
        )
    return LaunchDescription([
        node1,
        node2,
        node3
        ])
