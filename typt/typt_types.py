"""types.py - classes representing typt types."""

from typing import Iterable
from collections import namedtuple

from copy import deepcopy


NameSuperPair = namedtuple('NameNamePair', ('name', 'super'))
NameSuperPair.__doc__ = """Store a pair of strings (name and super)."""


NameTypePair = namedtuple('NameTypePair', ('name', 'type'))
NameTypePair.__doc__ = """Store a (name: str, type: Type) pair."""


TestSuitePair = namedtuple('TestSuitePair', ('test', 'suite'))
TestSuitePair.__doc__ = """Store a (test: TestNode, suite: SuiteNode) pair."""


def log_type_error(msg: str, filename: str, metadata):
    """Log a type error for the given class."""
    # Format the source code
    source_lines = metadata.source.splitlines(keepends=True)
    line_ctr = metadata.line
    source_with_lines_and_indent = ''
    for line in source_lines:
        source_with_lines_and_indent += '\t{} | {}'.format(line_ctr, line)
        line_ctr += 1

    # Print source code that triggered error
    print('Error encountered:', source_with_lines_and_indent, sep='\n')

    # Print error message
    print(
        '\x1b[31mtypt\x1b[0m: {}: {}:{}: \x1b[1;37;41m{}\x1b[0m\n'.format(
            filename, metadata.line, metadata.column, msg
        )
    )


class Type:
    """A base class for Typt types."""

    def __init__(self):
        """Set base variables."""
        pass

    def __repr__(self) -> str:
        """Return a string representation of the Type."""
        return 'Typt::' + self.__class__.__name__


class InvalidType(Type):
    """Class representing an ill-formed type."""

    def __eq__(self, other) -> bool:
        """Return False for all others (cannot equal an invalid type)."""
        return False

    def __repr__(self) -> str:
        """Return the repr of an invalid type."""
        '\x1b[1;37;41m' + 'Typt::InvalidType' + '\x1b[0m'


class NoneType(Type):
    """Class for Typt::None type."""

    def __eq__(self, other) -> bool:
        """Compare a NoneType to another type."""
        if isinstance(other, NoneType):
            return True
        return False


class BoolType(Type):
    """Class for Typt::Bool type."""

    def __eq__(self, other) -> bool:
        """Compare a BoolType to another type."""
        if isinstance(other, BoolType):
            return True
        return False


class IntType(Type):
    """Class for Typt::Int type."""

    def __eq__(self, other) -> bool:
        """Compare a IntType to another type."""
        if isinstance(other, IntType):
            return True
        return False


class FloatType(Type):
    """Class for Typt::Float type."""

    def __eq__(self, other) -> bool:
        """Compare a FloatType to another type."""
        if isinstance(other, FloatType):
            return True
        return False


class StringType(Type):
    """Class for Typt::String type."""

    def __eq__(self, other) -> bool:
        """Compare a StringType to another type."""
        if isinstance(other, StringType):
            return True
        return False


class ObjectBaseType(Type):
    """Class for Typt::ObjectBaseType type."""

    def __eq__(self, other) -> bool:
        """Compare a ObjectBaseType to another type."""
        # Type equality
        if isinstance(other, ObjectBaseType):
            return True

        return False


class ListType(Type):
    """Class for Typt::ListType type."""

    def __init__(self, element_type: Type):
        """Set the element type."""
        self.element_type = element_type

        super().__init__()

    def __eq__(self, other) -> bool:
        """Check if the other is an equivalent list."""
        if isinstance(other, ListType):
            if isinstance(other.element_type, type(self.element_type)):
                return True
        return False

    def __repr__(self) -> str:
        """Return a string representation of a ListType."""
        return super().__repr__() + '[' + repr(self.element_type) + ']'


class TupleType(Type):
    """Class for Typt::TupleType type."""

    def __init__(self, element_type_list: list):
        """Set the element types."""
        self.element_type_list = element_type_list

        super().__init__()

    def __eq__(self, other) -> bool:
        """Check if the other is an equivalent tuple."""
        if isinstance(other, TupleType):
            # If they have a different number of args, no equal!
            if len(self.element_type_list) != len(other.element_type_list):
                return False

            # For each argument pair, if the arguements aren't the same type,
            # => bye bye
            arg_pairs = zip(self.element_type_list, other.element_type_list)
            for (s, o) in arg_pairs:
                if not isinstance(s, type(o)):
                    return False
            return True

        return False

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

    def __eq__(self, other) -> bool:
        """Check if the other is an equivalent set."""
        if isinstance(other, SetType):
            if isinstance(self.element_type, type(other.element_type)):
                return True
        return False

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

    def __eq__(self, other) -> bool:
        """Check if the other is an equivalent dict."""
        if isinstance(other, DictType):
            if isinstance(self.key_type, type(other.key_type)) \
                    and isinstance(self.value_type, type(other.value_type)):
                return True
        return False

    def __repr__(self) -> str:
        """Return a string representation of a DictType."""
        kv_types_str = [repr(self.key_type), repr(self.value_type)]

        return super().__repr__() + '{' + ' => '.join(kv_types_str) + '}'


class FunctionType(Type):
    """Class for Typt::FunctionType type.

    Attributes:
        parameters      (Iterable[Type]) : The function parameter types.
        return_type     (Type)           : The function return type.

    """

    def __init__(self, parmeters: Iterable[Type], return_type: Type):
        """Set parameters and return type."""
        self.parameters = parmeters
        self.return_type = return_type

        super().__init__()

    def __eq__(self, other) -> bool:
        """Check if the other is an equivalent function."""
        if isinstance(other, FunctionType):
            # Check return types
            if not isinstance(other.return_type, type(self.return_type)):
                return False

            # Check parameter lengths
            if len(self.parameters) != len(other.parameters):
                return False

            # Check parameter types
            pairs = zip(self.parameters, other.parameters)
            for (s, o) in pairs:
                if not isinstance(s, type(o)):
                    return False
            return True
        return False

    def __repr__(self) -> str:
        """Return string representation of a FunctionType."""
        p_types = [repr(param) for param in self.parameters]
        type = '<' + ', '.join(p_types) + ' -> ' + repr(self.return_type) + '>'

        return super().__repr__() + type


class ObjectType(Type):
    """Class for Typt::ObjectType type.

    Attributes:
        members     (Iterable[NameTypePair]) : The object's members.

    """

    def __init__(self, members: Iterable[NameTypePair]):
        """Set member types."""
        self.members = members

        super().__init__()

    def __eq__(self, other) -> bool:
        """Check if the two are equivalent or if lhs (self) is a sub of rhs.

        NOTE If self (i.e. left-hand side) is a subclass of other than also
        return true.
        RULES (Sub Base Object) & (Sub Object)
        """
        # Type subsumption
        # RULE (Sub Base Object)
        if isinstance(other, ObjectBaseType):
            return True

        # Type Equivalence or Subsuption
        # RULE (Sub Object)
        if isinstance(other, ObjectType):
            self_m = sorted(deepcopy(self.members), key=lambda ntp: ntp.name)
            other_m = sorted(deepcopy(other.members), key=lambda ntp: ntp.name)

            for o_m in other_m:
                has_current_m = False

                # Does self have this member?
                for s_m in self_m:
                    if o_m.name == s_m.name \
                            and isinstance(o_m.type, type(s_m.type)):
                        has_current_m = True

                # If it doesn't, then self <: other doesn't hold
                if not has_current_m:
                    return False

            # For every member of other, self has an equivalent
            return True

        return False

    def __repr__(self) -> str:
        """Return string representation of an ObjectType."""
        m_types = [m.name + ': ' + repr(m.type) for m in self.members]

        return super().__repr__() + '{' + ', '.join(m_types) + '}'


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


def is_invalid_type(t: Type) -> bool:
    """Return a boolean indicating if t is of the class InvalidType."""
    return isinstance(t, InvalidType)
