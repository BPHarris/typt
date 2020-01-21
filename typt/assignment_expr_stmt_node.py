"""assignment_expr_stmt_node.py.

Holds the AST node for an assignment expression statement.
"""

from typt.stmt_node import StmtNode
from typt.test_node import TestNode


class AssignmentExprStmtNode(StmtNode):
    """AssignmentExprStmtNode AST node."""

    def __init__(self, lhs: TestNode, assignment_type: str, rhs: TestNode, depth: int = 0):
        """Set the lhs, rhs, and the type of assignment (=, +=, etc.)."""
        self.lhs = lhs
        self.assignment_type = assignment_type
        self.rhs = rhs

        super().__init__(depth=depth)
