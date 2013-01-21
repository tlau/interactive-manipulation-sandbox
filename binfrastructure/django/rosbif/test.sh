#!/bin/bash
source ../../ros/setup.bash
export ROS_MASTER_URI=http://10.0.2.178:11311
export ROS_HOSTNAME=10.1.0.10
python impl.py $1
