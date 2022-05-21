#!/usr/bin/env python3
# license removed for brevity
from pip import main
import rospy
from geometry_msgs.msg import Twist
import keyboard
import sys
import tty
import termios

def getKey(settings):
    if sys.platform == 'win32':
        # getwch() returns a string on Windows
        key = msvcrt.getwch()
    else:
        tty.setraw(sys.stdin.fileno())
        # sys.stdin.read() returns a string on Linux
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def main():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('custom_keyop_node', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    command = Twist()
    print("left arrow key - stop and spin anticlockwise")
    print("Move straight otherwise")
    print("right arrow key - stop and spin clockwise")
    print("x - stop instantly")

    while not rospy.is_shutdown():
         #input string
        #if left arrow key is placed
        
        if(keyboard.is_pressed("left_arrow")):
            command.linear.x = 0.0
            command.linear.y = 0.0
            command.linear.z = 0.0

            command.angular.x = 1.0
            command.angular.y = 0.0
            command.angular.z = 0.0

        elif(keyboard.is_pressed("left_arrow")):
            command.linear.x = 0.0
            command.linear.y = 0.0
            command.linear.z = 0.0

            command.angular.x = -1.0
            command.angular.y = 0.0
            command.angular.z = 0.0

        
        elif(keyboard.is_pressed("x")):
            command.linear.x = 0.0
            command.linear.y = 0.0
            command.linear.z = 0.0

            command.angular.x = 0.0
            command.angular.y = 0.0
            command.angular.z = 0.0

        else:
            command.linear.x = 10.0
            command.linear.y = 0.0
            command.linear.z = 0.0

            command.angular.x = 0.0
            command.angular.y = 0.0
            command.angular.z = 0.0


        rospy.loginfo("Message Published")
        pub.publish(command)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass