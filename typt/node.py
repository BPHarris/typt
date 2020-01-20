"""node.py - holds the AST node base class and related data structures."""

from typt.typt_types import Type


class NodeMetadata:
    """A NodeMetadata class, representing info on the source code.

    Args:
        line    (int)   : The line number of the metadata being initialised.
        column  (int)   : The column number of the metadata being initialised.

    Attributes:
        line    (int)   : The line number of the metadata.
        column  (int)   : The column (char) number of the metadata.

    """

    def __init__(self, line: int = None, column: int = None):
        """Set position."""
        self.line = line
        self.column = column

    def __repr__(self) -> str:
        """Return the string representation of the metadata."""
        if not self.line or not self.column:
            return 'EmptyMetadata'

        return str(self.line) + ':' + str(self.column)


class Node:
    """AST node base class.

    Args:
        meta    (NodeMetadata) : The metadata of the node being initialised.

    Attributes:
        meta    (NodeMetadata) : The metadata of the AST node -- stores metadata.

    """

    def __init__(self, meta=NodeMetadata(), depth: int = 0):
        """Define all intrinsic member variables."""
        self.meta = meta
        self.depth = depth

    # Return str representing the output Python 3 code for the node
    def codegen(self) -> str:
        """Perform codegen for the given node."""
        raise NotImplementedError('Can not generate code for base AST node.')

    # Return the type of the node, derived from typing rules
    def check_type() -> Type:
        """Peform type checking for given node."""
        raise NotImplementedError('Can not check type for base AST node.')

    def __repr__(self) -> str:
        """Return the string representation of node."""
        return self.__class__.__name__
