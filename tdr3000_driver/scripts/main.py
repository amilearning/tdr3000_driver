#!/usr/bin/env python
# license removed for brevity


import rospy
from std_msgs.msg import String
# from nmea_msgs.msg import nmea_msgs
from NMEAInterpreter import*

if __name__ == '__main__':
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('tdr3000', anonymous=True)
    rate = rospy.Rate(100) # 100hz
    try:
        MyNMEAInterpreter = NMEAInterpreter()            
        while not rospy.is_shutdown():
            MyNMEAInterpreter.convertDataUnit4PX2()            
            # pub.publish(hello_str)
            rate.sleep()
            
    finally:
        MyNMEAInterpreter.MySerialCommunicator.ser.close()
        server_socket.close() 
    
    try:
        talker()
    except rospy.ROSInterruptException:
        pass