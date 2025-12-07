import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class AiPublisher(Node):

    def __init__(self):
        super().__init__('ai_publisher_node')
        self.publisher_ = self.create_publisher(String, 'ai_sensor_data', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.object_id = 0

    def timer_callback(self):
        object_name = random.choice(['robot', 'human', 'obstacle', 'target'])
        confidence = round(random.uniform(70.0, 99.9), 2)
        msg_data = f'Detected object: {object_name}, ID: {self.object_id}, Confidence: {confidence}%'
        
        msg = String()
        msg.data = msg_data
        self.publisher_.publish(msg)
        self.get_logger().info(f'AI Publishing: "{msg.data}"')
        self.object_id += 1

def main(args=None):
    rclpy.init(args=args)
    ai_publisher = AiPublisher()
    rclpy.spin(ai_publisher)
    ai_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()