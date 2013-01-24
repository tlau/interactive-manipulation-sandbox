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
 * Auto-generated by genmsg_cpp from file /home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/ros_comm/test/test_rospy/srv/StringString.srv
 *
 */


#ifndef TEST_ROSPY_MESSAGE_STRINGSTRINGREQUEST_H
#define TEST_ROSPY_MESSAGE_STRINGSTRINGREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/String.h>
#include <test_rospy/Val.h>

namespace test_rospy
{
template <class ContainerAllocator>
struct StringStringRequest_
{
  typedef StringStringRequest_<ContainerAllocator> Type;

  StringStringRequest_()
    : str()
    , str2()  {
    }
  StringStringRequest_(const ContainerAllocator& _alloc)
    : str(_alloc)
    , str2(_alloc)  {
    }



   typedef  ::std_msgs::String_<ContainerAllocator>  _str_type;
  _str_type str;

   typedef  ::test_rospy::Val_<ContainerAllocator>  _str2_type;
  _str2_type str2;




  typedef boost::shared_ptr< ::test_rospy::StringStringRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::test_rospy::StringStringRequest_<ContainerAllocator> const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;

}; // struct StringStringRequest_

typedef ::test_rospy::StringStringRequest_<std::allocator<void> > StringStringRequest;

typedef boost::shared_ptr< ::test_rospy::StringStringRequest > StringStringRequestPtr;
typedef boost::shared_ptr< ::test_rospy::StringStringRequest const> StringStringRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::test_rospy::StringStringRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::test_rospy::StringStringRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace test_rospy

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'test_rospy': ['/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/ros_comm/test/test_rospy/msg'], 'std_msgs': ['/opt/ros/groovy/share/std_msgs/msg'], 'test_rosmaster': ['/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/ros_comm/test/test_rosmaster/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::test_rospy::StringStringRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::test_rospy::StringStringRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test_rospy::StringStringRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test_rospy::StringStringRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test_rospy::StringStringRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test_rospy::StringStringRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::test_rospy::StringStringRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "1546156fedebbd48201e9764f27ae3e2";
  }

  static const char* value(const ::test_rospy::StringStringRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x1546156fedebbd48ULL;
  static const uint64_t static_value2 = 0x201e9764f27ae3e2ULL;
};

template<class ContainerAllocator>
struct DataType< ::test_rospy::StringStringRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "test_rospy/StringStringRequest";
  }

  static const char* value(const ::test_rospy::StringStringRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::test_rospy::StringStringRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "std_msgs/String str\n\
Val str2\n\
\n\
================================================================================\n\
MSG: std_msgs/String\n\
string data\n\
\n\
================================================================================\n\
MSG: test_rospy/Val\n\
string val\n\
";
  }

  static const char* value(const ::test_rospy::StringStringRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::test_rospy::StringStringRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.str);
      stream.next(m.str2);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct StringStringRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::test_rospy::StringStringRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::test_rospy::StringStringRequest_<ContainerAllocator>& v)
  {
    s << indent << "str: ";
    s << std::endl;
    Printer< ::std_msgs::String_<ContainerAllocator> >::stream(s, indent + "  ", v.str);
    s << indent << "str2: ";
    s << std::endl;
    Printer< ::test_rospy::Val_<ContainerAllocator> >::stream(s, indent + "  ", v.str2);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TEST_ROSPY_MESSAGE_STRINGSTRINGREQUEST_H