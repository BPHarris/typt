"""return_stmt_node.py - holds the AST node for return statements."""

from typt.stmt_node import StmtNode
from typt.test_node import TestNode

from typt.codegen import indent
from typt.environment import Environment
from typt.typt_types import Type


class ReturnStmtNode(StmtNode):
    """ReturnStmt AST node."""

    def __init__(self, return_value: TestNode = None, *args, **kwargs):
        """Set return_value."""
        self.return_value = return_value

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Check the type of the return statement."""
        # RULE Must be inside function
        # RULE Return value type must match funtion return value

        # TODO

        return Type()

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the Python3 equivalent for a return statement."""
        indentation = indent(indentation_level)

        if not self.return_value:
            return f'{indentation}return'

        return f'{indentation}return {self.return_value.codegen()}'
