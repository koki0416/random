import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random
import time

class RandomPublisher(Node):
    def __init__(self):
        super().__init__("random_number")
        self.pub = self.create_publisher(Int32, 'random', 10)
        self.timer = self.create_timer(1, self.callback)

    def callback(self):
        msg = Int32()
        msg.data = random.randint(0, 500)
        self.pub.publish(msg)
        self.get_logger().info(f"データを送信しました。：{msg.data}")

def main():
    print("プログラム開始")


    rclpy.init()
    node = RandomPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    print("プログラム終了しました")