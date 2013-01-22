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
 * Auto-generated by genmsg_cpp from file /home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/ros_comm/test/test_roslib_comm/msg/HeaderTest.msg
 *
 */


#ifndef TEST_ROSLIB_COMM_MESSAGE_HEADERTEST_H
#define TEST_ROSLIB_COMM_MESSAGE_HEADERTEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace test_roslib_comm
{
template <class ContainerAllocator>
struct HeaderTest_
{
  typedef HeaderTest_<ContainerAllocator> Type;

  HeaderTest_()
    : header()
    , i32(0)  {
    }
  HeaderTest_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , i32(0)  {
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef int32_t _i32_type;
  _i32_type i32;




  typedef boost::shared_ptr< ::test_roslib_comm::HeaderTest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::test_roslib_comm::HeaderTest_<ContainerAllocator> const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;

}; // struct HeaderTest_

typedef ::test_roslib_comm::HeaderTest_<std::allocator<void> > HeaderTest;

typedef boost::shared_ptr< ::test_roslib_comm::HeaderTest > HeaderTestPtr;
typedef boost::shared_ptr< ::test_roslib_comm::HeaderTest const> HeaderTestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::test_roslib_comm::HeaderTest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::test_roslib_comm::HeaderTest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace test_roslib_comm

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'rosgraph_msgs': ['/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/ros_comm/messages/rosgraph_msgs/msg'], 'test_roslib_comm': ['/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/ros_comm/test/test_roslib_comm/msg'], 'std_msgs': ['/opt/ros/groovy/share/std_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::test_roslib_comm::HeaderTest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::test_roslib_comm::HeaderTest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test_roslib_comm::HeaderTest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test_roslib_comm::HeaderTest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test_roslib_comm::HeaderTest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test_roslib_comm::HeaderTest_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::test_roslib_comm::HeaderTest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4426b8931bec8509041d64c6a89b54a2";
  }

  static const char* value(const ::test_roslib_comm::HeaderTest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4426b8931bec8509ULL;
  static const uint64_t static_value2 = 0x041d64c6a89b54a2ULL;
};

template<class ContainerAllocator>
struct DataType< ::test_roslib_comm::HeaderTest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "test_roslib_comm/HeaderTest";
  }

  static const char* value(const ::test_roslib_comm::HeaderTest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::test_roslib_comm::HeaderTest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n\
int32 i32\n\
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
";
  }

  static const char* value(const ::test_roslib_comm::HeaderTest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::test_roslib_comm::HeaderTest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.i32);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct HeaderTest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::test_roslib_comm::HeaderTest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::test_roslib_comm::HeaderTest_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "i32: ";
    Printer<int32_t>::stream(s, indent + "  ", v.i32);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TEST_ROSLIB_COMM_MESSAGE_HEADERTEST_H
