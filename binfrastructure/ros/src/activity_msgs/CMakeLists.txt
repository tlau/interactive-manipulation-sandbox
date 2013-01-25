cmake_minimum_required(VERSION 2.8.3)
project(activity_msgs)

find_package(catkin REQUIRED COMPONENTS actionlib_msgs)

add_message_files(
  FILES
  ActivityErrorCode.msg
  QueryArg.msg
  Query.msg
  RunningActivityInfo.msg
)
  

add_action_files(
  DIRECTORY action
  FILES 
  EvaluateQuery.action
  Execute.action
  ListRunningActivities.action
  StartActivity.action
  StopActivity.action
)

generate_messages(
  DEPENDENCIES actionlib_msgs
  )

catkin_package(
  DEPENDS actionlib_msgs
  )
