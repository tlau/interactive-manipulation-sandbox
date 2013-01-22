"""autogenerated by genpy from test_rosmaster/Arrays.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy

class Arrays(genpy.Message):
  _md5sum = "c5a1f18379b10bdd4df210944f6007a4"
  _type = "test_rosmaster/Arrays"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """#for rostopic tests
int8[] int8_arr
uint8[] uint8_arr
int32[] int32_arr
uint32[] uint32_arr
string[] string_arr
time[] time_arr

"""
  __slots__ = ['int8_arr','uint8_arr','int32_arr','uint32_arr','string_arr','time_arr']
  _slot_types = ['int8[]','uint8[]','int32[]','uint32[]','string[]','time[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       int8_arr,uint8_arr,int32_arr,uint32_arr,string_arr,time_arr

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Arrays, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.int8_arr is None:
        self.int8_arr = []
      if self.uint8_arr is None:
        self.uint8_arr = ''
      if self.int32_arr is None:
        self.int32_arr = []
      if self.uint32_arr is None:
        self.uint32_arr = []
      if self.string_arr is None:
        self.string_arr = []
      if self.time_arr is None:
        self.time_arr = []
    else:
      self.int8_arr = []
      self.uint8_arr = ''
      self.int32_arr = []
      self.uint32_arr = []
      self.string_arr = []
      self.time_arr = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.int8_arr)
      buff.write(_struct_I.pack(length))
      pattern = '<%sb'%length
      buff.write(struct.pack(pattern, *self.int8_arr))
      _x = self.uint8_arr
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.int32_arr)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.int32_arr))
      length = len(self.uint32_arr)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.pack(pattern, *self.uint32_arr))
      length = len(self.string_arr)
      buff.write(_struct_I.pack(length))
      for val1 in self.string_arr:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.time_arr)
      buff.write(_struct_I.pack(length))
      for val1 in self.time_arr:
        _x = val1
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.time_arr is None:
        self.time_arr = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sb'%length
      start = end
      end += struct.calcsize(pattern)
      self.int8_arr = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.uint8_arr = str[start:end].decode('utf-8')
      else:
        self.uint8_arr = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.int32_arr = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.uint32_arr = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.string_arr = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.string_arr.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.time_arr = []
      for i in range(0, length):
        val1 = genpy.Time()
        _x = val1
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        self.time_arr.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.int8_arr)
      buff.write(_struct_I.pack(length))
      pattern = '<%sb'%length
      buff.write(self.int8_arr.tostring())
      _x = self.uint8_arr
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.int32_arr)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.int32_arr.tostring())
      length = len(self.uint32_arr)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.uint32_arr.tostring())
      length = len(self.string_arr)
      buff.write(_struct_I.pack(length))
      for val1 in self.string_arr:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.time_arr)
      buff.write(_struct_I.pack(length))
      for val1 in self.time_arr:
        _x = val1
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.time_arr is None:
        self.time_arr = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sb'%length
      start = end
      end += struct.calcsize(pattern)
      self.int8_arr = numpy.frombuffer(str[start:end], dtype=numpy.int8, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.uint8_arr = str[start:end].decode('utf-8')
      else:
        self.uint8_arr = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.int32_arr = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.uint32_arr = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.string_arr = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.string_arr.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.time_arr = []
      for i in range(0, length):
        val1 = genpy.Time()
        _x = val1
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        self.time_arr.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2I = struct.Struct("<2I")
