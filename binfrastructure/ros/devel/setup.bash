#!/usr/bin/env bash
# generated from catkin/cmake/templates/setup.bash.in

# Modified by JAC to get it to work on different environments without modification
SCRIPT_PATH="${BASH_SOURCE[0]}";
if([ -h "${SCRIPT_PATH}" ]) then
  while([ -h "${SCRIPT_PATH}" ]) do SCRIPT_PATH=`readlink "${SCRIPT_PATH}"`; done
fi
export OLDPWDBAK=$OLDPWD
pushd . > /dev/null
cd `dirname ${SCRIPT_PATH}` > /dev/null
SCRIPT_PATH=`pwd`;
cd ..
ACTUAL=`pwd`;
popd  > /dev/null
export OLDPWD=$OLDPWDBAK
export SCRIPT_PATH

CATKIN_SHELL=bash
. "${SCRIPT_PATH}/setup.sh"

# Replace hardcoded location of ROS workspace with actual one (calculated above)
HARDCODED=/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros
export ROS_PACKAGE_PATH=${ROS_PACKAGE_PATH//${HARDCODED}/${ACTUAL}}
