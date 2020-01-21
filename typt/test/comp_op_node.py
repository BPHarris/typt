"""comp_op_node.py - holds the AST node for a comparison operation.

Comparison operations are binary operations.
"""

from typt.test_node import TestNode


class CompOpNode(TestNode):
    """CompOpNode AST node."""

    def __init__(self, operator: str, lhs: TestNode, rhs: TestNode):
        """Set operator and operands."""
        self.operator = operator
        self.lhs = lhs
        self.rhs = rhs
