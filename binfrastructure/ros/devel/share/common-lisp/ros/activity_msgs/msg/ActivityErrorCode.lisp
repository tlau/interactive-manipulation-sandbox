; Auto-generated. Do not edit!


(cl:in-package activity_msgs-msg)


;//! \htmlinclude ActivityErrorCode.msg.html

(cl:defclass <ActivityErrorCode> (roslisp-msg-protocol:ros-message)
  ((val
    :reader val
    :initarg :val
    :type cl:fixnum
    :initform 0))
)

(cl:defclass ActivityErrorCode (<ActivityErrorCode>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ActivityErrorCode>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ActivityErrorCode)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name activity_msgs-msg:<ActivityErrorCode> is deprecated: use activity_msgs-msg:ActivityErrorCode instead.")))

(cl:ensure-generic-function 'val-val :lambda-list '(m))
(cl:defmethod val-val ((m <ActivityErrorCode>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader activity_msgs-msg:val-val is deprecated.  Use activity_msgs-msg:val instead.")
  (val m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<ActivityErrorCode>)))
    "Constants for message type '<ActivityErrorCode>"
  '((:SUCCESS . 0)
    (:OTHER_ERROR . 1))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'ActivityErrorCode)))
    "Constants for message type 'ActivityErrorCode"
  '((:SUCCESS . 0)
    (:OTHER_ERROR . 1))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ActivityErrorCode>) ostream)
  "Serializes a message object of type '<ActivityErrorCode>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'val)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ActivityErrorCode>) istream)
  "Deserializes a message object of type '<ActivityErrorCode>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'val)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ActivityErrorCode>)))
  "Returns string type for a message object of type '<ActivityErrorCode>"
  "activity_msgs/ActivityErrorCode")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ActivityErrorCode)))
  "Returns string type for a message object of type 'ActivityErrorCode"
  "activity_msgs/ActivityErrorCode")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ActivityErrorCode>)))
  "Returns md5sum for a message object of type '<ActivityErrorCode>"
  "5f3a5874e440a9ca821e65c840de46da")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ActivityErrorCode)))
  "Returns md5sum for a message object of type 'ActivityErrorCode"
  "5f3a5874e440a9ca821e65c840de46da")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ActivityErrorCode>)))
  "Returns full string definition for message of type '<ActivityErrorCode>"
  (cl:format cl:nil "uint8 val~%~%uint8 SUCCESS=0~%uint8 OTHER_ERROR=1~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ActivityErrorCode)))
  "Returns full string definition for message of type 'ActivityErrorCode"
  (cl:format cl:nil "uint8 val~%~%uint8 SUCCESS=0~%uint8 OTHER_ERROR=1~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ActivityErrorCode>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ActivityErrorCode>))
  "Converts a ROS message object to a list"
  (cl:list 'ActivityErrorCode
    (cl:cons ':val (val msg))
))
