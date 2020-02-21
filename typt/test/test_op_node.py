"""test_op_node.py - holds AST node for a test operation.

A test operation is one of or_test, and_test, or not_test in Typt.g4.

"""

from typt.test_node import TestNode

from typing import List

from typt.codegen import indent
from typt.typt_types import Type
from typt.environment import Environment


class TestOpNode(TestNode):
    """TestOpNode AST node."""

    def __init__(self, operator: str, lhs: TestNode):
        """Create initial operand list as just the lhs operand."""
        self.operator = operator
        self.operands = list([lhs])     # type: List[TestNode]

    def check_type(self, environment: Environment) -> Type:
        """Check the type of the test operation."""
        pass

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the Python3 code for the expression operation."""
        indentation = indent(indentation_level)

        # Get the code of the test operation
        output = self.operator.join(map(lambda o: o.codegen(), self.operands))
        return f'{indentation}{output}'
