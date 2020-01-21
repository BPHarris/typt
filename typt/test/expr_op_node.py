"""expr_op_node.py - holds the AST node for an expression.

Expressions are binary operations (grammar: or_expr to term, inclusive).
"""

from typt.test_node import TestNode


class ExprOpNode(TestNode):
    """ExprOpNode AST node."""

    def __init__(self, operator: str, lhs: TestNode, rhs: TestNode):
        """Set operator and operands."""
        self.operator = operator
        self.lhs = lhs
        self.rhs = rhs
