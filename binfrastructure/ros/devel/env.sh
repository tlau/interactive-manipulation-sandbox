#!/usr/bin/env sh
# generated from catkin/cmake/templates/env.sh.in

if [ $# -eq 0 ] ; then
  /bin/echo "Entering environment at '/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/devel', type 'exit' to leave"
  . "/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/devel/setup.sh"
  "$SHELL" -i
  /bin/echo "Exiting environment at '/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/devel'"
else
  . "/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/devel/setup.sh"
  exec "$@"
fi
