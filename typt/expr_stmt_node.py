"""expr_stmt_node.py - holds the AST node for an expression statement."""

from typt.stmt_node import StmtNode
from typt.test_node import TestNode


class ExprStmtNode(StmtNode):
    """ExprStmtNode AST node."""

    def __init__(self, test_node: TestNode, depth: int = 0):
        """Set the test node (expression body)."""
        self.test_node = test_node

        super().__init__()