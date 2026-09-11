from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        

        Node(
            package='mia_competition',
            executable='auto_node',
            name='autonomous_controller',
            output='screen'
        ),

        # Computer Vision Node 
        # Node(
        #     package='mia_competition',
        #     executable='vision_node', 
        #     name='yolo_scroll_detector',
        #     output='screen'
        # ),

    ])
