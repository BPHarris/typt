"""expr_op_node.py - holds the AST node for an expression.

Expressions are binary operations (grammar: or_expr to term, inclusive).
"""

from typt.test_node import TestNode

from typt.codegen import indent
from typt.typt_types import Type
from typt.environment import Environment


class ExprOpNode(TestNode):
    """ExprOpNode AST node."""

    def __init__(self, operator: str, lhs: TestNode, rhs: TestNode):
        """Set operator and operands."""
        self.operator = operator
        self.lhs = lhs
        self.rhs = rhs

    def check_type(self, environment: Environment) -> Type:
        """Check the type of the expression operation."""
        pass

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the Python3 code for the expression operation."""
        indentation = indent(indentation_level)

        lhs = self.lhs.codegen()
        rhs = self.rhs.codegen()

        return f'{indentation}{lhs} {self.operator} {rhs}'
