"""test_op_node.py - holds AST node for a test operation.

A test operation is one of or_test, and_test, or not_test in Typt.g4.

"""

from typt.test_node import TestNode


class TestOpNode(TestNode):
    """TestOpNode AST node."""

    def __init__(self, operator: str, lhs: TestNode):
        """Create initial operand list as just the lhs operand."""
        self.operator = operator
        self.operands = list([lhs])
