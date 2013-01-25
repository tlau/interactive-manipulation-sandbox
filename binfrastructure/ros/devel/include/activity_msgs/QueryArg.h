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
 * Auto-generated by genmsg_cpp from file /home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/activity_msgs/msg/QueryArg.msg
 *
 */


#ifndef ACTIVITY_MSGS_MESSAGE_QUERYARG_H
#define ACTIVITY_MSGS_MESSAGE_QUERYARG_H


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
struct QueryArg_
{
  typedef QueryArg_<ContainerAllocator> Type;

  QueryArg_()
    : name()
    , value()  {
    }
  QueryArg_(const ContainerAllocator& _alloc)
    : name(_alloc)
    , value(_alloc)  {
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _name_type;
  _name_type name;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _value_type;
  _value_type value;




  typedef boost::shared_ptr< ::activity_msgs::QueryArg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::activity_msgs::QueryArg_<ContainerAllocator> const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;

}; // struct QueryArg_

typedef ::activity_msgs::QueryArg_<std::allocator<void> > QueryArg;

typedef boost::shared_ptr< ::activity_msgs::QueryArg > QueryArgPtr;
typedef boost::shared_ptr< ::activity_msgs::QueryArg const> QueryArgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::activity_msgs::QueryArg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::activity_msgs::QueryArg_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace activity_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'actionlib_msgs': ['/opt/ros/groovy/share/actionlib_msgs/msg'], 'std_msgs': ['/opt/ros/groovy/share/std_msgs/msg'], 'activity_msgs': ['/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/activity_msgs/msg', '/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/devel/share/activity_msgs/msg', '/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/devel/share/activity_msgs/msg', '/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/devel/share/activity_msgs/msg', '/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/devel/share/activity_msgs/msg', '/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/devel/share/activity_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::activity_msgs::QueryArg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::activity_msgs::QueryArg_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::activity_msgs::QueryArg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::activity_msgs::QueryArg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::activity_msgs::QueryArg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::activity_msgs::QueryArg_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::activity_msgs::QueryArg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bc6ccc4a57f61779c8eaae61e9f422e0";
  }

  static const char* value(const ::activity_msgs::QueryArg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbc6ccc4a57f61779ULL;
  static const uint64_t static_value2 = 0xc8eaae61e9f422e0ULL;
};

template<class ContainerAllocator>
struct DataType< ::activity_msgs::QueryArg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "activity_msgs/QueryArg";
  }

  static const char* value(const ::activity_msgs::QueryArg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::activity_msgs::QueryArg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string name\n\
\n\
# JSON encoded value\n\
string value\n\
";
  }

  static const char* value(const ::activity_msgs::QueryArg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::activity_msgs::QueryArg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.name);
      stream.next(m.value);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct QueryArg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::activity_msgs::QueryArg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::activity_msgs::QueryArg_<ContainerAllocator>& v)
  {
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.name);
    s << indent << "value: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.value);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ACTIVITY_MSGS_MESSAGE_QUERYARG_H
