; Auto-generated. Do not edit!


(cl:in-package activity_msgs-msg)


;//! \htmlinclude RunningActivityInfo.msg.html

(cl:defclass <RunningActivityInfo> (roslisp-msg-protocol:ros-message)
  ((activity_type
    :reader activity_type
    :initarg :activity_type
    :type cl:string
    :initform "")
   (activity_id
    :reader activity_id
    :initarg :activity_id
    :type cl:integer
    :initform 0))
)

(cl:defclass RunningActivityInfo (<RunningActivityInfo>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RunningActivityInfo>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RunningActivityInfo)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name activity_msgs-msg:<RunningActivityInfo> is deprecated: use activity_msgs-msg:RunningActivityInfo instead.")))

(cl:ensure-generic-function 'activity_type-val :lambda-list '(m))
(cl:defmethod activity_type-val ((m <RunningActivityInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader activity_msgs-msg:activity_type-val is deprecated.  Use activity_msgs-msg:activity_type instead.")
  (activity_type m))

(cl:ensure-generic-function 'activity_id-val :lambda-list '(m))
(cl:defmethod activity_id-val ((m <RunningActivityInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader activity_msgs-msg:activity_id-val is deprecated.  Use activity_msgs-msg:activity_id instead.")
  (activity_id m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RunningActivityInfo>) ostream)
  "Serializes a message object of type '<RunningActivityInfo>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'activity_type))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'activity_type))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'activity_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'activity_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'activity_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'activity_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 32) (cl:slot-value msg 'activity_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 40) (cl:slot-value msg 'activity_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 48) (cl:slot-value msg 'activity_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 56) (cl:slot-value msg 'activity_id)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RunningActivityInfo>) istream)
  "Deserializes a message object of type '<RunningActivityInfo>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'activity_type) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'activity_type) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'activity_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'activity_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'activity_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'activity_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 32) (cl:slot-value msg 'activity_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 40) (cl:slot-value msg 'activity_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 48) (cl:slot-value msg 'activity_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 56) (cl:slot-value msg 'activity_id)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RunningActivityInfo>)))
  "Returns string type for a message object of type '<RunningActivityInfo>"
  "activity_msgs/RunningActivityInfo")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RunningActivityInfo)))
  "Returns string type for a message object of type 'RunningActivityInfo"
  "activity_msgs/RunningActivityInfo")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RunningActivityInfo>)))
  "Returns md5sum for a message object of type '<RunningActivityInfo>"
  "fd300eb773b52d357e662b58a7cd5c0a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RunningActivityInfo)))
  "Returns md5sum for a message object of type 'RunningActivityInfo"
  "fd300eb773b52d357e662b58a7cd5c0a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RunningActivityInfo>)))
  "Returns full string definition for message of type '<RunningActivityInfo>"
  (cl:format cl:nil "string activity_type~%uint64 activity_id~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RunningActivityInfo)))
  "Returns full string definition for message of type 'RunningActivityInfo"
  (cl:format cl:nil "string activity_type~%uint64 activity_id~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RunningActivityInfo>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'activity_type))
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RunningActivityInfo>))
  "Converts a ROS message object to a list"
  (cl:list 'RunningActivityInfo
    (cl:cons ':activity_type (activity_type msg))
    (cl:cons ':activity_id (activity_id msg))
))
