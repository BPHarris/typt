"""node.py - holds the AST node base class and related data structures."""


class Token:
    """A token class, representing info on the source code."""

    def __init__(self, line: None, column: None):
        """Set token position."""
        self.line = line
        self.column = column

    def __repr__(self) -> str:
        """Return the string representation of the token."""
        if not self.line or not self.column:
            return 'EmptyToken'

        return str(self.line) + ':' + str(self.column)


class Node:
    """AST node base class."""

    def __init__(self, token=Token()):
        """Define all intrinsic member variables."""
        self.token = token

    # TODO: Should return ???
    def codegen(self) -> None:
        """Perform codegen for the given node."""
        raise NotImplementedError('Can not generate code for base AST node.')

    # TODO: Should return the type of the expression represented by the node.
    def check_type() -> None:
        """Peform type checking for given node."""
        raise NotImplementedError('Can not check type for base AST node.')

    def __repr__(self) -> str:
        """Return the string representation of node."""
        return 'Node'
