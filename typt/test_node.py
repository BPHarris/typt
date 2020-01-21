"""test_node.py - holds the AST node for a test statement."""

from typt.node import Node


class TestNode(Node):
    """TestNode AST node."""

    def __init__(self, depth: int = 0):
        """Call super initialiser."""
        super().__init__(depth=depth)
