"""types.py - classes representing typt types."""

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


def compare_types(a: Type, b: Type) -> bool:
    """Compare the given types A and B.

    Return true if the two given types are sematically equivalent int the
    typing rules for the Typt language. Return false otherwise.

    Args:
        a   (Type) : First given type.
        b   (Type) : Second given type.
    """
    pass
