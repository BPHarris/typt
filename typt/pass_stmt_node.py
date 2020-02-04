"""pass_stmt_node.py - holds the AST node for pass statements."""

from typt.stmt_node import StmtNode

from typt.codegen import indent
from typt.typt_types import Type
from typt.environment import Environment


class PassStmtNode(StmtNode):
    """Class for 'pass' statement AST node."""

    def check_type(self, environment: Environment) -> Type:
        """Check the type of the pass statement."""
        # RULE Pass statement is always well-formed
        return Type()

    def codegen(self, indentation_level: int = 0) -> str:
        """Return Python3 equivalent to 'pass' statement."""
        return f'{indent(indentation_level)}pass'
