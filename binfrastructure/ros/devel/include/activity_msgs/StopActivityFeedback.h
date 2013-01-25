/* Software License Agreement (BSD License)
 *
 * Copyright (c) 2011, Willow Garage, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *  * Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *  * Redistributions in binary form must reproduce the above
 *    copyright notice, this list of conditions and the following
 *    disclaimer in the documentation and/or other materials provided
 *    with the distribution.
 *  * Neither the name of Willow Garage, Inc. nor the names of its
 *    contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 * FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 * ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 *
 * Auto-generated by genmsg_cpp from file /home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/devel/share/activity_msgs/msg/StopActivityFeedback.msg
 *
 */


#ifndef ACTIVITY_MSGS_MESSAGE_STOPACTIVITYFEEDBACK_H
#define ACTIVITY_MSGS_MESSAGE_STOPACTIVITYFEEDBACK_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace activity_msgs
{
template <class ContainerAllocator>
struct StopActivityFeedback_
{
  typedef StopActivityFeedback_<ContainerAllocator> Type;

  StopActivityFeedback_()
    {
    }
  StopActivityFeedback_(const ContainerAllocator& _alloc)
    {
    }






  typedef boost::shared_ptr< ::activity_msgs::StopActivityFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::activity_msgs::StopActivityFeedback_<ContainerAllocator> const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;

}; // struct StopActivityFeedback_

typedef ::activity_msgs::StopActivityFeedback_<std::allocator<void> > StopActivityFeedback;

typedef boost::shared_ptr< ::activity_msgs::StopActivityFeedback > StopActivityFeedbackPtr;
typedef boost::shared_ptr< ::activity_msgs::StopActivityFeedback const> StopActivityFeedbackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::activity_msgs::StopActivityFeedback_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::activity_msgs::StopActivityFeedback_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace activity_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'actionlib_msgs': ['/opt/ros/groovy/share/actionlib_msgs/msg'], 'std_msgs': ['/opt/ros/groovy/share/std_msgs/msg'], 'activity_msgs': ['/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/activity_msgs/msg', '/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/devel/share/activity_msgs/msg', '/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/devel/share/activity_msgs/msg', '/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/devel/share/activity_msgs/msg', '/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/devel/share/activity_msgs/msg', '/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/devel/share/activity_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::activity_msgs::StopActivityFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::activity_msgs::StopActivityFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::activity_msgs::StopActivityFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::activity_msgs::StopActivityFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::activity_msgs::StopActivityFeedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::activity_msgs::StopActivityFeedback_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::activity_msgs::StopActivityFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::activity_msgs::StopActivityFeedback_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::activity_msgs::StopActivityFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "activity_msgs/StopActivityFeedback";
  }

  static const char* value(const ::activity_msgs::StopActivityFeedback_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::activity_msgs::StopActivityFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
# no feedback\n\
\n\
\n\
";
  }

  static const char* value(const ::activity_msgs::StopActivityFeedback_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::activity_msgs::StopActivityFeedback_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct StopActivityFeedback_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::activity_msgs::StopActivityFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::activity_msgs::StopActivityFeedback_<ContainerAllocator>& v)
  {
  }
};

} // namespace message_operations
} // namespace ros

#endif // ACTIVITY_MSGS_MESSAGE_STOPACTIVITYFEEDBACK_H
