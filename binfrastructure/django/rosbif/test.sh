#!/bin/bash
source ../../ros/devel/setup.bash
export ROS_MASTER_URI=http://10.0.9.133:11311
# export ROS_HOSTNAME=10.1.0.10
export ROS_HOSTNAME=10.0.10.237
python impl.py $1
