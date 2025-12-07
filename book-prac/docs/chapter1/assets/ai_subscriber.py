import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class AiSubscriber(Node):

    def __init__(self):
        super().__init__('ai_subscriber_node')
        self.subscription = self.create_subscription(
            String,
            'ai_sensor_data',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.get_logger().info('AI Subscriber Node started. Listening for sensor data...')

    def listener_callback(self, msg):
        # Simulate AI processing of the received data
        sensor_data = msg.data
        self.get_logger().info(f'AI Received: "{sensor_data}"')
        
        # Example processing: parse object and confidence
        try:
            parts = sensor_data.split(', ')
            obj_part = parts[0] # "Detected object: robot"
            conf_part = parts[2] # "Confidence: 95.23%"
            
            detected_object = obj_part.split(': ')[1]
            confidence_str = conf_part.split(': ')[1].replace('%', '')
            confidence = float(confidence_str)

            if confidence > 90:
                self.get_logger().info(f'High confidence detection of {detected_object}. Initiating further action...')
            else:
                self.get_logger().info(f'Detection of {detected_object} with moderate confidence. Awaiting more data.')

        except IndexError:
            self.get_logger().warn(f'Could not parse sensor data: "{sensor_data}"')
        except ValueError:
            self.get_logger().warn(f'Could not convert confidence to float: "{sensor_data}"')


def main(args=None):
    rclpy.init(args=args)

    ai_subscriber = AiSubscriber()

    rclpy.spin(ai_subscriber)

    # Destroy the node explicitly
    ai_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()