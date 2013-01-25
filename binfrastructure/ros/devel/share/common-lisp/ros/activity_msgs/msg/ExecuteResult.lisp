; Auto-generated. Do not edit!


(cl:in-package activity_msgs-msg)


;//! \htmlinclude ExecuteResult.msg.html

(cl:defclass <ExecuteResult> (roslisp-msg-protocol:ros-message)
  ((outcome
    :reader outcome
    :initarg :outcome
    :type cl:string
    :initform "")
   (outputs
    :reader outputs
    :initarg :outputs
    :type cl:string
    :initform "")
   (retval
    :reader retval
    :initarg :retval
    :type cl:fixnum
    :initform 0)
   (error_string
    :reader error_string
    :initarg :error_string
    :type cl:string
    :initform ""))
)

(cl:defclass ExecuteResult (<ExecuteResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ExecuteResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ExecuteResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name activity_msgs-msg:<ExecuteResult> is deprecated: use activity_msgs-msg:ExecuteResult instead.")))

(cl:ensure-generic-function 'outcome-val :lambda-list '(m))
(cl:defmethod outcome-val ((m <ExecuteResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader activity_msgs-msg:outcome-val is deprecated.  Use activity_msgs-msg:outcome instead.")
  (outcome m))

(cl:ensure-generic-function 'outputs-val :lambda-list '(m))
(cl:defmethod outputs-val ((m <ExecuteResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader activity_msgs-msg:outputs-val is deprecated.  Use activity_msgs-msg:outputs instead.")
  (outputs m))

(cl:ensure-generic-function 'retval-val :lambda-list '(m))
(cl:defmethod retval-val ((m <ExecuteResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader activity_msgs-msg:retval-val is deprecated.  Use activity_msgs-msg:retval instead.")
  (retval m))

(cl:ensure-generic-function 'error_string-val :lambda-list '(m))
(cl:defmethod error_string-val ((m <ExecuteResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader activity_msgs-msg:error_string-val is deprecated.  Use activity_msgs-msg:error_string instead.")
  (error_string m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<ExecuteResult>)))
    "Constants for message type '<ExecuteResult>"
  '((:RETVAL_SUCCESS . 0)
    (:RETVAL_PARSE_ERROR . 1)
    (:RETVAL_RUNTIME_ERROR . 2)
    (:RETVAL_OTHER_ERROR . 3))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'ExecuteResult)))
    "Constants for message type 'ExecuteResult"
  '((:RETVAL_SUCCESS . 0)
    (:RETVAL_PARSE_ERROR . 1)
    (:RETVAL_RUNTIME_ERROR . 2)
    (:RETVAL_OTHER_ERROR . 3))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ExecuteResult>) ostream)
  "Serializes a message object of type '<ExecuteResult>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'outcome))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'outcome))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'outputs))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'outputs))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'retval)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'error_string))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'error_string))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ExecuteResult>) istream)
  "Deserializes a message object of type '<ExecuteResult>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'outcome) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'outcome) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'outputs) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'outputs) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'retval)) (cl:read-byte istream))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'error_string) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'error_string) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ExecuteResult>)))
  "Returns string type for a message object of type '<ExecuteResult>"
  "activity_msgs/ExecuteResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ExecuteResult)))
  "Returns string type for a message object of type 'ExecuteResult"
  "activity_msgs/ExecuteResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ExecuteResult>)))
  "Returns md5sum for a message object of type '<ExecuteResult>"
  "c00cb5148e9da7247b9783f7dab67f11")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ExecuteResult)))
  "Returns md5sum for a message object of type 'ExecuteResult"
  "c00cb5148e9da7247b9783f7dab67f11")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ExecuteResult>)))
  "Returns full string definition for message of type '<ExecuteResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%# outcome of the state machine. if retval is RETVAL_SUCCESS, this will~%# correspond to one of the outcomes in the state machine defined in the goal's json_str.~%string outcome~%~%# JSON encoded output values~%string outputs~%~%# return value~%uint8 retval~%uint8 RETVAL_SUCCESS = 0~%uint8 RETVAL_PARSE_ERROR = 1~%uint8 RETVAL_RUNTIME_ERROR = 2~%uint8 RETVAL_OTHER_ERROR = 3~%~%# human readable error string, if something went wrong~%string error_string~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ExecuteResult)))
  "Returns full string definition for message of type 'ExecuteResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%# outcome of the state machine. if retval is RETVAL_SUCCESS, this will~%# correspond to one of the outcomes in the state machine defined in the goal's json_str.~%string outcome~%~%# JSON encoded output values~%string outputs~%~%# return value~%uint8 retval~%uint8 RETVAL_SUCCESS = 0~%uint8 RETVAL_PARSE_ERROR = 1~%uint8 RETVAL_RUNTIME_ERROR = 2~%uint8 RETVAL_OTHER_ERROR = 3~%~%# human readable error string, if something went wrong~%string error_string~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ExecuteResult>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'outcome))
     4 (cl:length (cl:slot-value msg 'outputs))
     1
     4 (cl:length (cl:slot-value msg 'error_string))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ExecuteResult>))
  "Converts a ROS message object to a list"
  (cl:list 'ExecuteResult
    (cl:cons ':outcome (outcome msg))
    (cl:cons ':outputs (outputs msg))
    (cl:cons ':retval (retval msg))
    (cl:cons ':error_string (error_string msg))
))
