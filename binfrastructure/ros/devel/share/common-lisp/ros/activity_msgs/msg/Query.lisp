; Auto-generated. Do not edit!


(cl:in-package activity_msgs-msg)


;//! \htmlinclude Query.msg.html

(cl:defclass <Query> (roslisp-msg-protocol:ros-message)
  ((query
    :reader query
    :initarg :query
    :type cl:string
    :initform "")
   (args
    :reader args
    :initarg :args
    :type (cl:vector activity_msgs-msg:QueryArg)
   :initform (cl:make-array 0 :element-type 'activity_msgs-msg:QueryArg :initial-element (cl:make-instance 'activity_msgs-msg:QueryArg))))
)

(cl:defclass Query (<Query>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Query>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Query)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name activity_msgs-msg:<Query> is deprecated: use activity_msgs-msg:Query instead.")))

(cl:ensure-generic-function 'query-val :lambda-list '(m))
(cl:defmethod query-val ((m <Query>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader activity_msgs-msg:query-val is deprecated.  Use activity_msgs-msg:query instead.")
  (query m))

(cl:ensure-generic-function 'args-val :lambda-list '(m))
(cl:defmethod args-val ((m <Query>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader activity_msgs-msg:args-val is deprecated.  Use activity_msgs-msg:args instead.")
  (args m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Query>) ostream)
  "Serializes a message object of type '<Query>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'query))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'query))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'args))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'args))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Query>) istream)
  "Deserializes a message object of type '<Query>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'query) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'query) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'args) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'args)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'activity_msgs-msg:QueryArg))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Query>)))
  "Returns string type for a message object of type '<Query>"
  "activity_msgs/Query")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Query)))
  "Returns string type for a message object of type 'Query"
  "activity_msgs/Query")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Query>)))
  "Returns md5sum for a message object of type '<Query>"
  "da5ce4f3c58052ab69b4d66fd34bddf2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Query)))
  "Returns md5sum for a message object of type 'Query"
  "da5ce4f3c58052ab69b4d66fd34bddf2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Query>)))
  "Returns full string definition for message of type '<Query>"
  (cl:format cl:nil "string query~%QueryArg[] args~%~%================================================================================~%MSG: activity_msgs/QueryArg~%string name~%~%# JSON encoded value~%string value~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Query)))
  "Returns full string definition for message of type 'Query"
  (cl:format cl:nil "string query~%QueryArg[] args~%~%================================================================================~%MSG: activity_msgs/QueryArg~%string name~%~%# JSON encoded value~%string value~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Query>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'query))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'args) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Query>))
  "Converts a ROS message object to a list"
  (cl:list 'Query
    (cl:cons ':query (query msg))
    (cl:cons ':args (args msg))
))
