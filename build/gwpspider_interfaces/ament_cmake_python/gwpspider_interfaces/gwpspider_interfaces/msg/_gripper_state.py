# generated from rosidl_generator_py/resource/_idl.py.em
# with input from gwpspider_interfaces:msg/GripperState.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_GripperState(type):
    """Metaclass of message 'GripperState'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('gwpspider_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'gwpspider_interfaces.msg.GripperState')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__gripper_state
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__gripper_state
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__gripper_state
            cls._TYPE_SUPPORT = module.type_support_msg__msg__gripper_state
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__gripper_state

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class GripperState(metaclass=Metaclass_GripperState):
    """Message class 'GripperState'."""

    __slots__ = [
        '_switch_state',
        '_fingers_state',
        '_is_attached',
    ]

    _fields_and_field_types = {
        'switch_state': 'string',
        'fingers_state': 'string',
        'is_attached': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.switch_state = kwargs.get('switch_state', str())
        self.fingers_state = kwargs.get('fingers_state', str())
        self.is_attached = kwargs.get('is_attached', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.switch_state != other.switch_state:
            return False
        if self.fingers_state != other.fingers_state:
            return False
        if self.is_attached != other.is_attached:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def switch_state(self):
        """Message field 'switch_state'."""
        return self._switch_state

    @switch_state.setter
    def switch_state(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'switch_state' field must be of type 'str'"
        self._switch_state = value

    @builtins.property
    def fingers_state(self):
        """Message field 'fingers_state'."""
        return self._fingers_state

    @fingers_state.setter
    def fingers_state(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'fingers_state' field must be of type 'str'"
        self._fingers_state = value

    @builtins.property
    def is_attached(self):
        """Message field 'is_attached'."""
        return self._is_attached

    @is_attached.setter
    def is_attached(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'is_attached' field must be of type 'bool'"
        self._is_attached = value