#! /usr/bin/env python3
# Copyright (c) 2018 Robert Bosch GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from time import sleep

import rclpy

from geometry_msgs.msg import TransformStamped
from tf2_msgs.msg import TFMessage


def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node("tf2_example_pub")

    pub = node.create_publisher(TFMessage, "/tf")

    t1 = TransformStamped()
    t1.header.frame_id = "base_link"
    t1.child_frame_id = "arm1"
    t2 = TransformStamped()
    t2.header.frame_id = "base_link"
    t2.child_frame_id = "arm2"

    msg = TFMessage()
    msg.transforms = [t1, t2]

    while rclpy.ok():
        pub.publish(msg)
        sleep(0.9)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
