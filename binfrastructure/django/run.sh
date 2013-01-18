#!/bin/bash
source ../ros/setup.bash
export ROS_MASTER_URI=http://10.0.2.178:11311
export ROS_HOSTNAME=babylon1.willowgarage.com
python manage.py runserver 0:8100
