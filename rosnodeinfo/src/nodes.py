#!/usr/bin/env python

import roslib
import rospy
import rosnode

from std_msgs.msg import String

def pubNodeInfos():
  pub = rospy.Publisher('runningNodes', String, queue_size=1)
  rospy.init_node('nodeInfoPublisher', anonymous=False)
  
  while not rospy.is_shutdown():
    nodeString = ""
    nodes = rosnode.get_node_names()

    for node in nodes:
      nodeString += node + " "
    rospy.loginfo(nodeString)

    pub.publish(nodeString)
    rospy.sleep(2)


if __name__ == '__main__':
  try:  
    pubNodeInfos()
  except rospy.ROSInterruptException:
    print "node interrupted"
