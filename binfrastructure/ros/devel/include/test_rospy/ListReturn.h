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
 * Auto-generated by gensrv_cpp from file /home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/ros_comm/test/test_rospy/srv/ListReturn.srv
 *
 */


#ifndef TEST_ROSPY_MESSAGE_LISTRETURN_H
#define TEST_ROSPY_MESSAGE_LISTRETURN_H

#include <ros/service_traits.h>


#include <test_rospy/ListReturnRequest.h>
#include <test_rospy/ListReturnResponse.h>


namespace test_rospy
{

struct ListReturn
{

typedef ListReturnRequest Request;
typedef ListReturnResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct ListReturn
} // namespace test_rospy


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::test_rospy::ListReturn > {
  static const char* value()
  {
    return "8083abf57e6eb0ff97ebb506984b66b8";
  }

  static const char* value(const ::test_rospy::ListReturn&) { return value(); }
};

template<>
struct DataType< ::test_rospy::ListReturn > {
  static const char* value()
  {
    return "test_rospy/ListReturn";
  }

  static const char* value(const ::test_rospy::ListReturn&) { return value(); }
};


// service_traits::MD5Sum< ::test_rospy::ListReturnRequest> should match 
// service_traits::MD5Sum< ::test_rospy::ListReturn > 
template<>
struct MD5Sum< ::test_rospy::ListReturnRequest>
{
  static const char* value()
  {
    return MD5Sum< ::test_rospy::ListReturn >::value();
  }
  static const char* value(const ::test_rospy::ListReturnRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::test_rospy::ListReturnRequest> should match 
// service_traits::DataType< ::test_rospy::ListReturn > 
template<>
struct DataType< ::test_rospy::ListReturnRequest>
{
  static const char* value()
  {
    return DataType< ::test_rospy::ListReturn >::value();
  }
  static const char* value(const ::test_rospy::ListReturnRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::test_rospy::ListReturnResponse> should match 
// service_traits::MD5Sum< ::test_rospy::ListReturn > 
template<>
struct MD5Sum< ::test_rospy::ListReturnResponse>
{
  static const char* value()
  {
    return MD5Sum< ::test_rospy::ListReturn >::value();
  }
  static const char* value(const ::test_rospy::ListReturnResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::test_rospy::ListReturnResponse> should match 
// service_traits::DataType< ::test_rospy::ListReturn > 
template<>
struct DataType< ::test_rospy::ListReturnResponse>
{
  static const char* value()
  {
    return DataType< ::test_rospy::ListReturn >::value();
  }
  static const char* value(const ::test_rospy::ListReturnResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // TEST_ROSPY_MESSAGE_LISTRETURN_H
