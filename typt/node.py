"""node.py - holds the AST node base class and related data structures."""

from typt.typt_types import Type, NameTypePair, TestSuitePair

from typing import Union


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
        meta    (NodeMetadata) : The metadata of the AST node instance.

    """

    def __init__(self, meta: NodeMetadata = NodeMetadata(), depth=0):
        """Define all intrinsic member variables."""
        self.meta = meta

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


Printables = Union[
    Node, Type, NameTypePair, TestSuitePair, list, str, None
]
Printables.__doc__ = """The printable types for NodePrinter::_print."""


class NodePrinter:
    """Pretty print the AST of which 'root' is the root.

    Attributes:
        NodePrinter.depth   (int)   : The tree-depth of the node to print
        root                (Node)  : The root node to print from
        indent              (str)   : The string used to denote indentation

    # TODO Remove all references to depth in *_node.py

    """

    depth = 0
    indent = '-'

    def __init__(self, root: Node, indent_str: str = '    '):
        """Set the initial values."""
        self.root = root
        NodePrinter.indent = indent_str

    @staticmethod
    def puts(string: str) -> None:
        """Print the given string at the current indentation level."""
        # Get indent level
        indent = NodePrinter.depth * NodePrinter.indent

        # Get lines (i.e. split on \n if present)
        lines = str(string).splitlines(keepends=True)

        # Apply indent
        indented_lines = list()
        for line in lines:
            indented_lines += [indent + line]

        # Print each line in the string with the indent in front
        return print(''.join(indented_lines))

    def print(self) -> None:
        """Print the root node."""
        # Store state
        old = (NodePrinter.depth, NodePrinter.indent, )

        # Print the AST from the root node
        self._print(self.root)

        # Restore state
        NodePrinter.depth, NodePrinter.indent = old

    def _print(self, node: Printables, name: str = '') -> None:
        """Print the given node and it's children."""
        # Node print
        if isinstance(node, Node):
            return self._print_node(node)

        # Typt type
        if isinstance(node, Type):
            return NodePrinter.puts(str(node))

        # NameTypePair
        if isinstance(node, NameTypePair):
            NodePrinter.puts('NameTypePair')

            NodePrinter.depth += 1
            NodePrinter.puts('name: ' + str(node.name))
            NodePrinter.puts('type: ' + str(node.type))
            NodePrinter.depth -= 1

            return

        # TestSuitePair
        if isinstance(node, TestSuitePair):
            NodePrinter.puts('TestSuitePair')

            NodePrinter.depth += 1
            self._print(node.test)
            self._print(node.suite)
            NodePrinter.depth -= 1

            return

        # List print
        if type(node) == list:
            # Print each elem
            for element in node:
                self._print(element, name)

            return

        # String
        if type(node) == str:
            # If name is data then keep '' around string, otherwise don't
            node_str = repr(node) if name == 'data' else str(node)

            return NodePrinter.puts(name + ': ' + node_str)

        # None
        if not node:
            name = name if name else '<None>'

            # Print as warning (i.e. red background for text)
            return NodePrinter.puts(
                '\x1b[1;37;41m' + name + ': ' + 'Empty' + '\x1b[0m'
            )

        raise NotImplementedError('Can\'t print type {}.'.format(type(node)))

    def _print_node(self, node: Node) -> None:
        """Print the given node and it's children."""
        # Check type
        if not isinstance(node, Node):
            return

        # Print name
        NodePrinter.puts(str(node))

        # Print children
        NodePrinter.depth += 1
        for name, attribute in vars(node).items():
            # Skippable attributes
            if name == 'meta':
                continue
            if name == 'depth':
                continue

            self._print(attribute, name=name)
        NodePrinter.depth -= 1
