import rclpy
from rclpy.node import Node
from service_msg.srv import RandomService
from std_msgs.msg import Int32

class Math_Service(Node):
    def __init__(self):
        super().__init__("math_service")
        self.num_data = []

        self.sub = self.create_subscription(
            Int32, 'random', self.topic_callback, 10
        )

        self.service = self.create_service(
            RandomService, 'random_service', self.service_callback
        )

    def topic_callback(self, msg):
        self.num_data.append(msg.data)

    def service_callback(self, request, response):
        req = request.command
        print(f"{req}が要求されました。")
        try:

            if req=="合計":
                response.answer = float(sum(self.num_data))
                return response

            elif req=="平均":
                response.answer = float(sum(self.num_data) / len(self.num_data))
                return response

            elif req=="最大値":
                response.answer = float(max(self.num_data))
                return response

            elif req=="最小値":
                response.answer = float(min(self.num_data))
                return response

            else:
                rseponse.answer = 0.0
                return response
            
        except Exception as e:
            response.answer = 0.0
            return response

def main():
    print("プログラム開始")
    rclpy.init()
    node = Math_Service()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    print("プログラム終了しました")