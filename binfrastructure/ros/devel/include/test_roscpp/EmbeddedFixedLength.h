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
 * Auto-generated by genmsg_cpp from file /home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/ros_comm/test/test_roscpp/test_serialization/msg/EmbeddedFixedLength.msg
 *
 */


#ifndef TEST_ROSCPP_MESSAGE_EMBEDDEDFIXEDLENGTH_H
#define TEST_ROSCPP_MESSAGE_EMBEDDEDFIXEDLENGTH_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <test_roscpp/FixedLength.h>

namespace test_roscpp
{
template <class ContainerAllocator>
struct EmbeddedFixedLength_
{
  typedef EmbeddedFixedLength_<ContainerAllocator> Type;

  EmbeddedFixedLength_()
    : a()  {
    }
  EmbeddedFixedLength_(const ContainerAllocator& _alloc)
    : a(_alloc)  {
    }



   typedef  ::test_roscpp::FixedLength_<ContainerAllocator>  _a_type;
  _a_type a;




  typedef boost::shared_ptr< ::test_roscpp::EmbeddedFixedLength_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::test_roscpp::EmbeddedFixedLength_<ContainerAllocator> const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;

}; // struct EmbeddedFixedLength_

typedef ::test_roscpp::EmbeddedFixedLength_<std::allocator<void> > EmbeddedFixedLength;

typedef boost::shared_ptr< ::test_roscpp::EmbeddedFixedLength > EmbeddedFixedLengthPtr;
typedef boost::shared_ptr< ::test_roscpp::EmbeddedFixedLength const> EmbeddedFixedLengthConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::test_roscpp::EmbeddedFixedLength_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::test_roscpp::EmbeddedFixedLength_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace test_roscpp

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'rosgraph_msgs': ['/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/ros_comm/messages/rosgraph_msgs/msg'], 'test_roscpp': ['/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/ros_comm/test/test_roscpp/test/msg', '/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/ros_comm/test/test_roscpp/test_serialization/msg', '/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/ros_comm/test/test_roscpp/perf/msg', '/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/ros_comm/test/test_roscpp/perf_serialization/msg'], 'std_msgs': ['/opt/ros/groovy/share/std_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::test_roscpp::EmbeddedFixedLength_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::test_roscpp::EmbeddedFixedLength_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test_roscpp::EmbeddedFixedLength_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test_roscpp::EmbeddedFixedLength_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test_roscpp::EmbeddedFixedLength_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test_roscpp::EmbeddedFixedLength_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::test_roscpp::EmbeddedFixedLength_<ContainerAllocator> >
{
  static const char* value()
  {
    return "770e15962592d1fbea70b6b820ba16d9";
  }

  static const char* value(const ::test_roscpp::EmbeddedFixedLength_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x770e15962592d1fbULL;
  static const uint64_t static_value2 = 0xea70b6b820ba16d9ULL;
};

template<class ContainerAllocator>
struct DataType< ::test_roscpp::EmbeddedFixedLength_<ContainerAllocator> >
{
  static const char* value()
  {
    return "test_roscpp/EmbeddedFixedLength";
  }

  static const char* value(const ::test_roscpp::EmbeddedFixedLength_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::test_roscpp::EmbeddedFixedLength_<ContainerAllocator> >
{
  static const char* value()
  {
    return "FixedLength a\n\
\n\
================================================================================\n\
MSG: test_roscpp/FixedLength\n\
uint32 a\n\
float32 b\n\
\n\
";
  }

  static const char* value(const ::test_roscpp::EmbeddedFixedLength_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::test_roscpp::EmbeddedFixedLength_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.a);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct EmbeddedFixedLength_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::test_roscpp::EmbeddedFixedLength_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::test_roscpp::EmbeddedFixedLength_<ContainerAllocator>& v)
  {
    s << indent << "a: ";
    s << std::endl;
    Printer< ::test_roscpp::FixedLength_<ContainerAllocator> >::stream(s, indent + "  ", v.a);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TEST_ROSCPP_MESSAGE_EMBEDDEDFIXEDLENGTH_H
