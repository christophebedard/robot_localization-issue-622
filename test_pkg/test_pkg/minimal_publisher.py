import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.pub_imu = self.create_publisher(Imu, 'imu', 10)
        self.pub_odo = self.create_publisher(Odometry, 'odo', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.imu_msg = Imu()
        self.odo_msg = Odometry()

        self.imu_msg.header.frame_id = 'base_link'

        self.odo_msg.header.frame_id = 'odom'
        self.odo_msg.child_frame_id = 'base_link'

    def timer_callback(self):
        synced_time = self.get_clock().now().to_msg()

        self.imu_msg.header.stamp = synced_time
        self.odo_msg.header.stamp = synced_time

        self.pub_imu.publish(self.imu_msg)
        self.pub_odo.publish(self.odo_msg)
        self.get_logger().info('Published IMU and Odometry')

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

