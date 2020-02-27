"""subscript_node.py - holds the AST subscript node."""

from typt.node import Node
from typt.test_node import TestNode

from typt.codegen import indent
from typt.typt_types import Type
from typt.environment import Environment

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

    def check_type(self, environment: Environment) -> Type:
        """Delegate (raise error)."""
        return super().check_type(environment)

    def codegen(self, indentation_level: int = 0) -> str:
        """Return Python3 representation of subscipt."""
        start = '' if not self.start else self.start.codegen()
        upto = '' if not self.upto else self.upto.codegen()
        step = '' if not self.step else self.step.codegen()

        return f'[{start}:{upto}:{step}]'
