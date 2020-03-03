"""test_node.py - holds the AST node for a test statement."""

from typt.node import Node


class TestNode(Node):
    """TestNode AST node."""

    def __init__(self, *args, **kwargs):
        """Call super initialiser."""
        super().__init__(*args, **kwargs)
