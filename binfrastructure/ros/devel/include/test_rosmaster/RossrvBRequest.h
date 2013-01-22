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
 * Auto-generated by genmsg_cpp from file /home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/ros_comm/test/test_rosmaster/srv/RossrvB.srv
 *
 */


#ifndef TEST_ROSMASTER_MESSAGE_ROSSRVBREQUEST_H
#define TEST_ROSMASTER_MESSAGE_ROSSRVBREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <test_rosmaster/Empty.h>

namespace test_rosmaster
{
template <class ContainerAllocator>
struct RossrvBRequest_
{
  typedef RossrvBRequest_<ContainerAllocator> Type;

  RossrvBRequest_()
    : empty()  {
    }
  RossrvBRequest_(const ContainerAllocator& _alloc)
    : empty(_alloc)  {
    }



   typedef  ::test_rosmaster::Empty_<ContainerAllocator>  _empty_type;
  _empty_type empty;




  typedef boost::shared_ptr< ::test_rosmaster::RossrvBRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::test_rosmaster::RossrvBRequest_<ContainerAllocator> const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;

}; // struct RossrvBRequest_

typedef ::test_rosmaster::RossrvBRequest_<std::allocator<void> > RossrvBRequest;

typedef boost::shared_ptr< ::test_rosmaster::RossrvBRequest > RossrvBRequestPtr;
typedef boost::shared_ptr< ::test_rosmaster::RossrvBRequest const> RossrvBRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::test_rosmaster::RossrvBRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::test_rosmaster::RossrvBRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace test_rosmaster

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'test_rosmaster': ['/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/ros_comm/test/test_rosmaster/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::test_rosmaster::RossrvBRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::test_rosmaster::RossrvBRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test_rosmaster::RossrvBRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test_rosmaster::RossrvBRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test_rosmaster::RossrvBRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test_rosmaster::RossrvBRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::test_rosmaster::RossrvBRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6aac6c697d5414bc0fcede8c33981d0e";
  }

  static const char* value(const ::test_rosmaster::RossrvBRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6aac6c697d5414bcULL;
  static const uint64_t static_value2 = 0x0fcede8c33981d0eULL;
};

template<class ContainerAllocator>
struct DataType< ::test_rosmaster::RossrvBRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "test_rosmaster/RossrvBRequest";
  }

  static const char* value(const ::test_rosmaster::RossrvBRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::test_rosmaster::RossrvBRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Empty empty\n\
\n\
================================================================================\n\
MSG: test_rosmaster/Empty\n\
\n\
";
  }

  static const char* value(const ::test_rosmaster::RossrvBRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::test_rosmaster::RossrvBRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.empty);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct RossrvBRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::test_rosmaster::RossrvBRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::test_rosmaster::RossrvBRequest_<ContainerAllocator>& v)
  {
    s << indent << "empty: ";
    s << std::endl;
    Printer< ::test_rosmaster::Empty_<ContainerAllocator> >::stream(s, indent + "  ", v.empty);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TEST_ROSMASTER_MESSAGE_ROSSRVBREQUEST_H
