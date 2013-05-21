"""autogenerated by genpy from phidgets/servo_referenceRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class servo_referenceRequest(genpy.Message):
  _md5sum = "10aec6261d178a540f640abc7e85af3d"
  _type = "phidgets/servo_referenceRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 index
bool engage
float32 position
float32 speed
float32 acceleration

"""
  __slots__ = ['index','engage','position','speed','acceleration']
  _slot_types = ['int32','bool','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       index,engage,position,speed,acceleration

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(servo_referenceRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.index is None:
        self.index = 0
      if self.engage is None:
        self.engage = False
      if self.position is None:
        self.position = 0.
      if self.speed is None:
        self.speed = 0.
      if self.acceleration is None:
        self.acceleration = 0.
    else:
      self.index = 0
      self.engage = False
      self.position = 0.
      self.speed = 0.
      self.acceleration = 0.

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
      _x = self
      buff.write(_struct_iB3f.pack(_x.index, _x.engage, _x.position, _x.speed, _x.acceleration))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 17
      (_x.index, _x.engage, _x.position, _x.speed, _x.acceleration,) = _struct_iB3f.unpack(str[start:end])
      self.engage = bool(self.engage)
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
      _x = self
      buff.write(_struct_iB3f.pack(_x.index, _x.engage, _x.position, _x.speed, _x.acceleration))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 17
      (_x.index, _x.engage, _x.position, _x.speed, _x.acceleration,) = _struct_iB3f.unpack(str[start:end])
      self.engage = bool(self.engage)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_iB3f = struct.Struct("<iB3f")
"""autogenerated by genpy from phidgets/servo_referenceResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class servo_referenceResponse(genpy.Message):
  _md5sum = "35e806e08fe8e25fde5b4c88fa52f05b"
  _type = "phidgets/servo_referenceResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 ack


"""
  __slots__ = ['ack']
  _slot_types = ['int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ack

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(servo_referenceResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.ack is None:
        self.ack = 0
    else:
      self.ack = 0

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
      buff.write(_struct_i.pack(self.ack))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (self.ack,) = _struct_i.unpack(str[start:end])
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
      buff.write(_struct_i.pack(self.ack))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (self.ack,) = _struct_i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_i = struct.Struct("<i")
class servo_reference(object):
  _type          = 'phidgets/servo_reference'
  _md5sum = 'e147971107721d067998f603de281d62'
  _request_class  = servo_referenceRequest
  _response_class = servo_referenceResponse
