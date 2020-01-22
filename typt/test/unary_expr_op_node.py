"""unary_expr_op_node.py - holds the AST node for a unary expression."""

from typt.test_node import TestNode


class UnaryExprOpNode(TestNode):
    """UnaryExprOpNode AST node."""

    def __init__(self, operator: str, lhs: TestNode):
        """Set operator and operands."""
        self.operator = operator
        self.lhs = lhs
