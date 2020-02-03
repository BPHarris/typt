"""pass_stmt_node.py - holds the AST node for pass statements."""

from typt.stmt_node import StmtNode

from typt.typt_types import Type
from typt.environment import Environment


class PassStmtNode(StmtNode):
    """Nothing to be implemented."""

    def check_type(self, environment: Environment) -> Type:
        """Check the type of the pass statement."""
        # RULE Pass statement is always well-formed
        return Type()
