"""expr_stmt_node.py - holds the AST node for an expression statement."""

from typt.stmt_node import StmtNode
from typt.test_node import TestNode

from typt.codegen import indent
from typt.typt_types import Type
from typt.environment import Environment


class ExprStmtNode(StmtNode):
    """ExprStmtNode AST node."""

    def __init__(self, test_node: TestNode, *args, **kwargs):
        """Set the test node (expression body)."""
        self.test_node = test_node

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Return the type of the contained expression."""
        return self.test_node.check_type(environment)

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the Python3 code of thi given expression."""
        return f'{indent(indentation_level)}{self.test_node.codegen()}'
