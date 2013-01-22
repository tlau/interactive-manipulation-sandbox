#!/bin/bash
source ../ros/setup.bash
export ROS_MASTER_URI=http://dug.willowgarage.com:11311
# export ROS_HOSTNAME=10.1.0.10
python manage.py runserver --noreload --nothreading 0:8100
