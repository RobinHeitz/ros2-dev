#! /usr/bin/env python


import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker

from std_msgs.msg import String

class MeshPublisher(Node):
    def __init__(self):
        super().__init__('mesh_publisher')
        self.publisher_ = self.create_publisher(Marker, "base_link", 10)
        self.timer = self.create_timer(5, self.timer_callback)
        self.i = 0
        
        
    
    def timer_callback(self):
        msg = Marker()
        msg.header.frame_id = "base_link"
        msg.type = 10
        msg.id = 0
        msg.action = 0
        msg.mesh_resource = "package://igus_rebel_description/meshes/robolink_rebel/Robolink_RebeL_000.dae"
        msg.mesh_use_embedded_materials = True

        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing counter: {self.i}")
        self.i += 1

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MeshPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()