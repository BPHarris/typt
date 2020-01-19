"""node.py - holds the AST node base class and related data structures."""

from typt.typt_types import Type


class Token:
    """A token class, representing info on the source code.

    Args:
        line    (int)   : The line number of the token being initialised.
        column  (int)   : The column number of the token being initialised.

    Attributes:
        line    (int)   : The line number of the token.
        column  (int)   : The column (char) number of the token.

    """

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
    """AST node base class.

    Args:
        token   (Token) : The token of the node being initialised.

    Attributes:
        token   (Token) : The token of the AST node -- stores metadata.

    """

    def __init__(self, token=Token()):
        """Define all intrinsic member variables."""
        self.token = token

    # TODO: Should return ???
    def codegen(self) -> None:
        """Perform codegen for the given node."""
        raise NotImplementedError('Can not generate code for base AST node.')

    # TODO: Should return the type of the expression represented by the node.
    def check_type() -> Type:
        """Peform type checking for given node."""
        raise NotImplementedError('Can not check type for base AST node.')

    def __repr__(self) -> str:
        """Return the string representation of node."""
        return 'Node'
