/* Auto-generated by genmsg_cpp for file /home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/executer_actions/msg/ExecuteAction.msg */
#ifndef EXECUTER_ACTIONS_MESSAGE_EXECUTEACTION_H
#define EXECUTER_ACTIONS_MESSAGE_EXECUTEACTION_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "executer_actions/ExecuteActionGoal.h"
#include "executer_actions/ExecuteActionResult.h"
#include "executer_actions/ExecuteActionFeedback.h"

namespace executer_actions
{
template <class ContainerAllocator>
struct ExecuteAction_ {
  typedef ExecuteAction_<ContainerAllocator> Type;

  ExecuteAction_()
  : action_goal()
  , action_result()
  , action_feedback()
  {
  }

  ExecuteAction_(const ContainerAllocator& _alloc)
  : action_goal(_alloc)
  , action_result(_alloc)
  , action_feedback(_alloc)
  {
  }

  typedef  ::executer_actions::ExecuteActionGoal_<ContainerAllocator>  _action_goal_type;
   ::executer_actions::ExecuteActionGoal_<ContainerAllocator>  action_goal;

  typedef  ::executer_actions::ExecuteActionResult_<ContainerAllocator>  _action_result_type;
   ::executer_actions::ExecuteActionResult_<ContainerAllocator>  action_result;

  typedef  ::executer_actions::ExecuteActionFeedback_<ContainerAllocator>  _action_feedback_type;
   ::executer_actions::ExecuteActionFeedback_<ContainerAllocator>  action_feedback;


  typedef boost::shared_ptr< ::executer_actions::ExecuteAction_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::executer_actions::ExecuteAction_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct ExecuteAction
typedef  ::executer_actions::ExecuteAction_<std::allocator<void> > ExecuteAction;

typedef boost::shared_ptr< ::executer_actions::ExecuteAction> ExecuteActionPtr;
typedef boost::shared_ptr< ::executer_actions::ExecuteAction const> ExecuteActionConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::executer_actions::ExecuteAction_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::executer_actions::ExecuteAction_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace executer_actions

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::executer_actions::ExecuteAction_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::executer_actions::ExecuteAction_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::executer_actions::ExecuteAction_<ContainerAllocator> > {
  static const char* value() 
  {
    return "66f9a3e2b949236a70f2a804af9b59d5";
  }

  static const char* value(const  ::executer_actions::ExecuteAction_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x66f9a3e2b949236aULL;
  static const uint64_t static_value2 = 0x70f2a804af9b59d5ULL;
};

template<class ContainerAllocator>
struct DataType< ::executer_actions::ExecuteAction_<ContainerAllocator> > {
  static const char* value() 
  {
    return "executer_actions/ExecuteAction";
  }

  static const char* value(const  ::executer_actions::ExecuteAction_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::executer_actions::ExecuteAction_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
ExecuteActionGoal action_goal\n\
ExecuteActionResult action_result\n\
ExecuteActionFeedback action_feedback\n\
\n\
================================================================================\n\
MSG: executer_actions/ExecuteActionGoal\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalID goal_id\n\
ExecuteGoal goal\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: actionlib_msgs/GoalID\n\
# The stamp should store the time at which this goal was requested.\n\
# It is used by an action server when it tries to preempt all\n\
# goals that were requested before a certain time\n\
time stamp\n\
\n\
# The id provides a way to associate feedback and\n\
# result message with specific goal requests. The id\n\
# specified must be unique.\n\
string id\n\
\n\
\n\
================================================================================\n\
MSG: executer_actions/ExecuteGoal\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# JSON encoded action to execute\n\
string action\n\
\n\
\n\
================================================================================\n\
MSG: executer_actions/ExecuteActionResult\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalStatus status\n\
ExecuteResult result\n\
\n\
================================================================================\n\
MSG: actionlib_msgs/GoalStatus\n\
GoalID goal_id\n\
uint8 status\n\
uint8 PENDING         = 0   # The goal has yet to be processed by the action server\n\
uint8 ACTIVE          = 1   # The goal is currently being processed by the action server\n\
uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing\n\
                            #   and has since completed its execution (Terminal State)\n\
uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)\n\
uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due\n\
                            #    to some failure (Terminal State)\n\
uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,\n\
                            #    because the goal was unattainable or invalid (Terminal State)\n\
uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing\n\
                            #    and has not yet completed execution\n\
uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,\n\
                            #    but the action server has not yet confirmed that the goal is canceled\n\
uint8 RECALLED        = 8   # The goal received a cancel request before it started executing\n\
                            #    and was successfully cancelled (Terminal State)\n\
uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be\n\
                            #    sent over the wire by an action server\n\
\n\
#Allow for the user to associate a string with GoalStatus for debugging\n\
string text\n\
\n\
\n\
================================================================================\n\
MSG: executer_actions/ExecuteResult\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
# outcome of the state machine. if retval is RETVAL_SUCCESS, this will\n\
# correspond to one of the outcomes in the state machine defined in the goal's json_str.\n\
string outcome\n\
\n\
# JSON encoded output values\n\
string outputs\n\
\n\
# return value\n\
uint8 retval\n\
uint8 RETVAL_SUCCESS = 0\n\
uint8 RETVAL_PARSE_ERROR = 1\n\
uint8 RETVAL_RUNTIME_ERROR = 2\n\
uint8 RETVAL_OTHER_ERROR = 3\n\
\n\
# human readable error string, if something went wrong\n\
string error_string\n\
\n\
\n\
================================================================================\n\
MSG: executer_actions/ExecuteActionFeedback\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalStatus status\n\
ExecuteFeedback feedback\n\
\n\
================================================================================\n\
MSG: executer_actions/ExecuteFeedback\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
\n\
";
  }

  static const char* value(const  ::executer_actions::ExecuteAction_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::executer_actions::ExecuteAction_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.action_goal);
    stream.next(m.action_result);
    stream.next(m.action_feedback);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ExecuteAction_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::executer_actions::ExecuteAction_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::executer_actions::ExecuteAction_<ContainerAllocator> & v) 
  {
    s << indent << "action_goal: ";
s << std::endl;
    Printer< ::executer_actions::ExecuteActionGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.action_goal);
    s << indent << "action_result: ";
s << std::endl;
    Printer< ::executer_actions::ExecuteActionResult_<ContainerAllocator> >::stream(s, indent + "  ", v.action_result);
    s << indent << "action_feedback: ";
s << std::endl;
    Printer< ::executer_actions::ExecuteActionFeedback_<ContainerAllocator> >::stream(s, indent + "  ", v.action_feedback);
  }
};


} // namespace message_operations
} // namespace ros

#endif // EXECUTER_ACTIONS_MESSAGE_EXECUTEACTION_H
