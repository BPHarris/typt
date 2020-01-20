"""var_dec_stmt_node.py - holds the AST node for a variable declaration statement."""

from typt.stmt_node import StmtNode
from typt.test_node import TestNode

from typt.typt_types import Type


class VarDecStmtNode(StmtNode):
    """VarDecStmtNode AST node."""

    def __init__(self, lhs: TestNode, var_type: Type, rhs: TestNode = None, depth: int = 0):
        """Set the lhs, rhs (default=None), and the type of variable."""
        self.lhs = lhs
        self.var_type = var_type
        self.rhs = rhs

        super().__init__(depth=0)
