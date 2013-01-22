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
 * Auto-generated by genmsg_cpp from file /home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/ros_comm/test/test_rosmaster/msg/Simple.msg
 *
 */


#ifndef TEST_ROSMASTER_MESSAGE_SIMPLE_H
#define TEST_ROSMASTER_MESSAGE_SIMPLE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace test_rosmaster
{
template <class ContainerAllocator>
struct Simple_
{
  typedef Simple_<ContainerAllocator> Type;

  Simple_()
    : b(0)
    , int16(0)
    , int32(0)
    , int64(0)
    , c(0)
    , uint16(0)
    , uint32(0)
    , uint64(0)
    , str()  {
    }
  Simple_(const ContainerAllocator& _alloc)
    : b(0)
    , int16(0)
    , int32(0)
    , int64(0)
    , c(0)
    , uint16(0)
    , uint32(0)
    , uint64(0)
    , str(_alloc)  {
    }



   typedef int8_t _b_type;
  _b_type b;

   typedef int16_t _int16_type;
  _int16_type int16;

   typedef int32_t _int32_type;
  _int32_type int32;

   typedef int64_t _int64_type;
  _int64_type int64;

   typedef uint8_t _c_type;
  _c_type c;

   typedef uint16_t _uint16_type;
  _uint16_type uint16;

   typedef uint32_t _uint32_type;
  _uint32_type uint32;

   typedef uint64_t _uint64_type;
  _uint64_type uint64;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _str_type;
  _str_type str;




  typedef boost::shared_ptr< ::test_rosmaster::Simple_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::test_rosmaster::Simple_<ContainerAllocator> const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;

}; // struct Simple_

typedef ::test_rosmaster::Simple_<std::allocator<void> > Simple;

typedef boost::shared_ptr< ::test_rosmaster::Simple > SimplePtr;
typedef boost::shared_ptr< ::test_rosmaster::Simple const> SimpleConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::test_rosmaster::Simple_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::test_rosmaster::Simple_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace test_rosmaster

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'test_rosmaster': ['/home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/ros_comm/test/test_rosmaster/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::test_rosmaster::Simple_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::test_rosmaster::Simple_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test_rosmaster::Simple_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test_rosmaster::Simple_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test_rosmaster::Simple_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test_rosmaster::Simple_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::test_rosmaster::Simple_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c9940b1313e61fed87cd22c50742578f";
  }

  static const char* value(const ::test_rosmaster::Simple_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc9940b1313e61fedULL;
  static const uint64_t static_value2 = 0x87cd22c50742578fULL;
};

template<class ContainerAllocator>
struct DataType< ::test_rosmaster::Simple_<ContainerAllocator> >
{
  static const char* value()
  {
    return "test_rosmaster/Simple";
  }

  static const char* value(const ::test_rosmaster::Simple_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::test_rosmaster::Simple_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# for rostopic tests\n\
byte b\n\
int16 int16\n\
int32 int32\n\
int64 int64\n\
char c\n\
uint16 uint16\n\
uint32 uint32\n\
uint64 uint64\n\
string str\n\
\n\
";
  }

  static const char* value(const ::test_rosmaster::Simple_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::test_rosmaster::Simple_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.b);
      stream.next(m.int16);
      stream.next(m.int32);
      stream.next(m.int64);
      stream.next(m.c);
      stream.next(m.uint16);
      stream.next(m.uint32);
      stream.next(m.uint64);
      stream.next(m.str);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct Simple_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::test_rosmaster::Simple_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::test_rosmaster::Simple_<ContainerAllocator>& v)
  {
    s << indent << "b: ";
    Printer<int8_t>::stream(s, indent + "  ", v.b);
    s << indent << "int16: ";
    Printer<int16_t>::stream(s, indent + "  ", v.int16);
    s << indent << "int32: ";
    Printer<int32_t>::stream(s, indent + "  ", v.int32);
    s << indent << "int64: ";
    Printer<int64_t>::stream(s, indent + "  ", v.int64);
    s << indent << "c: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.c);
    s << indent << "uint16: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.uint16);
    s << indent << "uint32: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.uint32);
    s << indent << "uint64: ";
    Printer<uint64_t>::stream(s, indent + "  ", v.uint64);
    s << indent << "str: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.str);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TEST_ROSMASTER_MESSAGE_SIMPLE_H
