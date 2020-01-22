"""subscript_node.py - holds the AST subscript node."""

from typt.node import Node
from typt.test_node import TestNode

from typing import Union


NoneOrTestNode = Union[None, TestNode]
NoneOrTestNode.__doc__ = """Union of (None, TestNode) for subscript args."""


class SubscriptNode(Node):
    """SubscriptNode AST node."""

    def __init__(self, start: NoneOrTestNode, upto: NoneOrTestNode, step: NoneOrTestNode):
        """Set default values."""
        self.start = start
        self.upto = upto
        self.step = step
