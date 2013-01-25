; Auto-generated. Do not edit!


(cl:in-package activity_msgs-msg)


;//! \htmlinclude StartActivityGoal.msg.html

(cl:defclass <StartActivityGoal> (roslisp-msg-protocol:ros-message)
  ((desired_activity_id
    :reader desired_activity_id
    :initarg :desired_activity_id
    :type cl:integer
    :initform 0)
   (activity_type
    :reader activity_type
    :initarg :activity_type
    :type cl:string
    :initform "")
   (goal
    :reader goal
    :initarg :goal
    :type cl:string
    :initform ""))
)

(cl:defclass StartActivityGoal (<StartActivityGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StartActivityGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StartActivityGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name activity_msgs-msg:<StartActivityGoal> is deprecated: use activity_msgs-msg:StartActivityGoal instead.")))

(cl:ensure-generic-function 'desired_activity_id-val :lambda-list '(m))
(cl:defmethod desired_activity_id-val ((m <StartActivityGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader activity_msgs-msg:desired_activity_id-val is deprecated.  Use activity_msgs-msg:desired_activity_id instead.")
  (desired_activity_id m))

(cl:ensure-generic-function 'activity_type-val :lambda-list '(m))
(cl:defmethod activity_type-val ((m <StartActivityGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader activity_msgs-msg:activity_type-val is deprecated.  Use activity_msgs-msg:activity_type instead.")
  (activity_type m))

(cl:ensure-generic-function 'goal-val :lambda-list '(m))
(cl:defmethod goal-val ((m <StartActivityGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader activity_msgs-msg:goal-val is deprecated.  Use activity_msgs-msg:goal instead.")
  (goal m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StartActivityGoal>) ostream)
  "Serializes a message object of type '<StartActivityGoal>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'desired_activity_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'desired_activity_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'desired_activity_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'desired_activity_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 32) (cl:slot-value msg 'desired_activity_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 40) (cl:slot-value msg 'desired_activity_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 48) (cl:slot-value msg 'desired_activity_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 56) (cl:slot-value msg 'desired_activity_id)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'activity_type))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'activity_type))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'goal))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'goal))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StartActivityGoal>) istream)
  "Deserializes a message object of type '<StartActivityGoal>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'desired_activity_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'desired_activity_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'desired_activity_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'desired_activity_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 32) (cl:slot-value msg 'desired_activity_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 40) (cl:slot-value msg 'desired_activity_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 48) (cl:slot-value msg 'desired_activity_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 56) (cl:slot-value msg 'desired_activity_id)) (cl:read-byte istream))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'activity_type) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'activity_type) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'goal) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'goal) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StartActivityGoal>)))
  "Returns string type for a message object of type '<StartActivityGoal>"
  "activity_msgs/StartActivityGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StartActivityGoal)))
  "Returns string type for a message object of type 'StartActivityGoal"
  "activity_msgs/StartActivityGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StartActivityGoal>)))
  "Returns md5sum for a message object of type '<StartActivityGoal>"
  "21f1a763fcdb8129f867ea969ee06f32")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StartActivityGoal)))
  "Returns md5sum for a message object of type 'StartActivityGoal"
  "21f1a763fcdb8129f867ea969ee06f32")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StartActivityGoal>)))
  "Returns full string definition for message of type '<StartActivityGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%uint64 desired_activity_id~%~%string activity_type~%~%# JSON encoded goal message~%string goal~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StartActivityGoal)))
  "Returns full string definition for message of type 'StartActivityGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%uint64 desired_activity_id~%~%string activity_type~%~%# JSON encoded goal message~%string goal~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StartActivityGoal>))
  (cl:+ 0
     8
     4 (cl:length (cl:slot-value msg 'activity_type))
     4 (cl:length (cl:slot-value msg 'goal))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StartActivityGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'StartActivityGoal
    (cl:cons ':desired_activity_id (desired_activity_id msg))
    (cl:cons ':activity_type (activity_type msg))
    (cl:cons ':goal (goal msg))
))
