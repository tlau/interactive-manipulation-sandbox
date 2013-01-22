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
 * Auto-generated by gensrv_cpp from file /home/julian/aaad/interactive-manipulation-sandbox/binfrastructure/ros/src/ros_comm/test/test_roscpp/test/srv/TestStringString.srv
 *
 */


#ifndef TEST_ROSCPP_MESSAGE_TESTSTRINGSTRING_H
#define TEST_ROSCPP_MESSAGE_TESTSTRINGSTRING_H

#include <ros/service_traits.h>


#include <test_roscpp/TestStringStringRequest.h>
#include <test_roscpp/TestStringStringResponse.h>


namespace test_roscpp
{

struct TestStringString
{

typedef TestStringStringRequest Request;
typedef TestStringStringResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct TestStringString
} // namespace test_roscpp


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::test_roscpp::TestStringString > {
  static const char* value()
  {
    return "671f8e4998eaec79f1c47e339dfd527b";
  }

  static const char* value(const ::test_roscpp::TestStringString&) { return value(); }
};

template<>
struct DataType< ::test_roscpp::TestStringString > {
  static const char* value()
  {
    return "test_roscpp/TestStringString";
  }

  static const char* value(const ::test_roscpp::TestStringString&) { return value(); }
};


// service_traits::MD5Sum< ::test_roscpp::TestStringStringRequest> should match 
// service_traits::MD5Sum< ::test_roscpp::TestStringString > 
template<>
struct MD5Sum< ::test_roscpp::TestStringStringRequest>
{
  static const char* value()
  {
    return MD5Sum< ::test_roscpp::TestStringString >::value();
  }
  static const char* value(const ::test_roscpp::TestStringStringRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::test_roscpp::TestStringStringRequest> should match 
// service_traits::DataType< ::test_roscpp::TestStringString > 
template<>
struct DataType< ::test_roscpp::TestStringStringRequest>
{
  static const char* value()
  {
    return DataType< ::test_roscpp::TestStringString >::value();
  }
  static const char* value(const ::test_roscpp::TestStringStringRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::test_roscpp::TestStringStringResponse> should match 
// service_traits::MD5Sum< ::test_roscpp::TestStringString > 
template<>
struct MD5Sum< ::test_roscpp::TestStringStringResponse>
{
  static const char* value()
  {
    return MD5Sum< ::test_roscpp::TestStringString >::value();
  }
  static const char* value(const ::test_roscpp::TestStringStringResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::test_roscpp::TestStringStringResponse> should match 
// service_traits::DataType< ::test_roscpp::TestStringString > 
template<>
struct DataType< ::test_roscpp::TestStringStringResponse>
{
  static const char* value()
  {
    return DataType< ::test_roscpp::TestStringString >::value();
  }
  static const char* value(const ::test_roscpp::TestStringStringResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // TEST_ROSCPP_MESSAGE_TESTSTRINGSTRING_H
