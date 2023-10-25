#!/usr/bin/env:python3

import rospy
from std_msgs.msg import Int16

class subscriber():
    def __init__(self):
        rospy.init_node('SUB')

        self.SUB = rospy.subscriber('motion',Int16,self.callback)
        self.PUB = rospy.publisher('move',Int16,queue_size = 10)

        self.count = 0
        self.move_msg = Int16()

    
    def callback(self,counter):
        self.count = counter.data
        if self.count < 600:
            self.move_msg = 1
        elif (self.count > 600) and (self.count <= 700):
            self.move_msg = 2
        elif (self.count > 700) and (self.count <= 1300):
            self.move_msg = 1
        elif (self.count > 1300) and (self.count <= 1400):
            self.move_msg = 3
        elif (self.count > 1400) and (self.count <= 2000):
            self.move_msg = 4
        else:
            self.move_msg = 0


        self.PUB.publish(self.move_msg)


if __name__ =='__main__':
    try:
        x_motion = subscriber()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
