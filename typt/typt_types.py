"""types.py - classes representing typt types."""

from typing import Iterable
from collections import namedtuple

# Todo list
#   TODO: compare_types: add typing rules


NameTypePair = namedtuple('NameTypePair', ('name', 'type'))
NameTypePair.__doc__ = """Store a (str, Type) pair."""

TestSuitePair = namedtuple('TestSuitePair', ('test', 'suite'))
TestSuitePair.__doc__ = """Store a (test: TestNode, suite: SuiteNode) pair."""


class Type:
    """A base class for Typt types."""

    def __init__(self):
        """Set base variables."""
        pass

    def __eq__(self, other) -> bool:
        """Compare self to the given type."""
        return compare_types(self, other)

    def __repr__(self) -> str:
        """Return a string representation of the Type."""
        return 'Typt::' + self.__class__.__name__


class NoneType(Type):
    """Class for Typt::None type."""

    pass


class BoolType(Type):
    """Class for Typt::Bool type."""

    pass


class IntType(Type):
    """Class for Typt::Int type."""

    pass


class FloatType(Type):
    """Class for Typt::Float type."""

    pass


class StringType(Type):
    """Class for Typt::String type."""

    pass


class ObjectBaseType(Type):
    """Class for Typt::ObjectBaseType type."""

    pass


class ListType(Type):
    """Class for Typt::ListType type."""

    def __init__(self, element_type: Type):
        """Set the element type."""
        self.element_type = element_type

        super().__init__()

    def __repr__(self) -> str:
        """Return a string representation of a ListType."""
        return super().__repr__() + '[' + repr(self.element_type) + ']'


class TupleType(Type):
    """Class for Typt::TupleType type."""

    def __init__(self, element_type_list: list):
        """Set the element types."""
        self.element_type_list = element_type_list

        super().__init__()

    def __repr__(self) -> str:
        """Return a string representation of a TupleType."""
        element_types = [repr(e_type) for e_type in self.element_type_list]

        return super().__repr__() + '(' + ', '.join(element_types) + ')'


class SetType(Type):
    """Class for Typt::SetType type."""

    def __init__(self, element_type: Type):
        """Set the element type."""
        self.element_type = element_type

        super().__init__()

    def __repr__(self) -> str:
        """Return a string representation of a SetType."""
        return super().__repr__() + '(' + repr(self.element_type) + ')'


class DictType(Type):
    """Class for Typt::DictType type."""

    def __init__(self, key_type: Type, value_type: Type):
        """Set the element type."""
        self.key_type = key_type
        self.value_type = value_type

        super().__init__()

    def __repr__(self) -> str:
        """Return a string representation of a SetType."""
        kv_types_str = [repr(self.key_type), repr(self.value_type)]

        return super().__repr__() + '{' + ' => '.join(kv_types_str) + '}'


class FunctionType(Type):
    """Class for Typt::FunctionType type.

    Attributes:
        parameters      (Iterable[Type])    ...
        return_type     (Type)              ...

    """

    def __init__(self, parmeters: Iterable[Type], return_type: Type):
        """Set parameters and return type."""
        self.parameters = parmeters
        self.return_type = return_type

        super().__init__()

    def __repr__(self) -> str:
        """Return string representation of a FunctionType."""
        p_types = [repr(param) for param in self.parameters]
        type = '<' + ', '.join(p_types) + ' -> ' + repr(self.return_type) + '>'

        return super().__repr__() + type


class ObjectType(Type):
    """Class for Typt::ObjectType type.

    Attributes:
        members     (Iterable[NameTypePair])    ...

    """

    def __init__(self, members: Iterable[NameTypePair]):
        """Set member types."""
        self.members = members

        super().__init__()

    def __repr__(self) -> str:
        """Return string representation of an ObjectType."""
        m_types = [m.name + ': ' + repr(m.type) for m in self.members]

        return super().__repr__() + '{' + ', '.join(m_types) + '}'


def compare_types(a: Type, b: Type) -> bool:
    """Compare the given types A and B.

    Return true if the two given types are sematically equivalent int the
    typing rules for the Typt language. Return false otherwise.

    Args:
        a   (Type) : First given type.
        b   (Type) : Second given type.
    """
    pass


def is_int(s: str) -> bool:
    """Given a string representing a literal, return true if it is an int."""
    try:
        int(s)
    except ValueError:
        return False

    return True


def is_float(s: str) -> bool:
    """Given a string representing a literal, return true if it is an float."""
    try:
        float(s)
    except ValueError:
        return False

    return True
