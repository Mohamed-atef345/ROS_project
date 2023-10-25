#!/usr/bin/env:python3

import rospy
from std_msgs.msg import Int16

class publisher():
    def __init__(self):
        rospy.init_node('PUB')

        self.PUB = rospy.Publisher('motion',Int16,queue_size = 10)
        self.rate = rospy.rate(10)
        self.counter = 0

    
    def publishing_count(self):
        while not rospy.is_shutdown():
            self.counter +=1
            self.PUB.publish(self.counter)
            self.rate.sleep()

if __name__ =='__main__':
    try:
        counter_publishing = publisher()
        counter_publishing.publishing_count()
    except rospy.ROSInterruptException:
        pass
