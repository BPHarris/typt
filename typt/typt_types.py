"""types.py - classes representing typt types."""

from typing import Iterable
from collections import namedtuple

# Todo list
#   TODO: Object base type
#   TODO: Object type
#   TODO: Function type
#   TODO: List type
#   TODO: Tuple type
#   TODO: Set type
#   TODO: Dict type
#
#   TODO: compare_types: add typing rules


NameTypePair = namedtuple('NameTypePair', ('name', 'type'))
NameTypePair.__doc__ = """Store a (str, Type) pair."""


class Type:
    """A base class for Typt types."""

    def __init__(self):
        """Set base variables."""
        pass

    def __eq__(self, other) -> bool:
        """Compare self to the given type."""
        return compare_types(self, other)


class NoneType(Type):
    """Class for Typt::None type."""

    def __init__(self):
        super().__init__()


class BoolType(Type):
    """Class for Typt::Bool type."""

    def __init__(self):
        super().__init__()


class IntType(Type):
    """Class for Typt::Int type."""

    def __init__(self):
        super().__init__()


class FloatType(Type):
    """Class for Typt::Float type."""

    def __init__(self):
        super().__init__()


class StringType(Type):
    """Class for Typt::String type."""

    def __init__(self):
        super().__init__()


class ObjectBaseType(Type):
    """Class for Typt::ObjectBaseType type."""

    def __init__(self):
        super().__init__()


class ListType(Type):
    """Class for Typt::ListType type."""

    def __init__(self, element_type: Type):
        """Set the element type."""
        self.element_type = element_type

        super().__init__()


class TupleType(Type):
    """Class for Typt::TupleType type."""

    def __init__(self, element_type_list: list):
        """Set the element types."""
        self.element_type_list = element_type_list

        super().__init__()


class SetType(Type):
    """Class for Typt::SetType type."""

    def __init__(self, element_type: Type):
        """Set the element type."""
        self.element_type = element_type

        super().__init__()


class DictType(Type):
    """Class for Typt::DictType type."""

    def __init__(self, key_type: Type, value_type: Type):
        """Set the element type."""
        self.key_type = key_type
        self.value_type = value_type

        super().__init__()


class FunctionType(Type):
    """Class for Typt::FunctionType type.

    Attributes:
        parameters      (Iterator[Type])    ...
        return_type     (Type)              ...

    """

    def __init__(self, parmeters: Iterable[Type], return_type: Type):
        """Set parameters and return type."""
        self.parameters = parmeters
        self.return_type = return_type

        super().__init__()


class ObjectType(Type):
    """Class for Typt::ObjectType type.

    Attributes:
        members     (Iterable[NameTypePair])    ...

    """

    def __init__(self, members: Iterable[NameTypePair]):
        """Set parameters and return type."""
        self.members = members

        super().__init__()


def compare_types(a: Type, b: Type) -> bool:
    """Compare the given types A and B.

    Return true if the two given types are sematically equivalent int the
    typing rules for the Typt language. Return false otherwise.

    Args:
        a   (Type) : First given type.
        b   (Type) : Second given type.
    """
    pass
