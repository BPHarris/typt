"""argument_list_node.py - holds the AST node for the argument_list rule."""

from typt.node import Node


class ArgumentListNode(Node):
    """ArgumentListNode AST node.

    Attributes:
        argument_list   (List[TestNode])    : The functions's parameter list

    """

    def __init__(self):
        """Initialise argument_list."""
        self.argument_list = list()
