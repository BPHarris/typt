"""unary_expr_op_node.py - holds the AST node for a unary expression."""

from typt.test_node import TestNode

from typt.codegen import indent
from typt.typt_types import Type
from typt.environment import Environment


class UnaryExprOpNode(TestNode):
    """UnaryExprOpNode AST node."""

    def __init__(self, operator: str, lhs: TestNode):
        """Set operator and operands."""
        self.operator = operator
        self.lhs = lhs

    def check_type(self, environment: Environment) -> Type:
        """Check the type of the unary expression."""
        pass

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the Python3 code for the expression operation."""
        indentation = indent(indentation_level)

        return f'{indentation}{self.operator}{self.lhs.codegen()}'
