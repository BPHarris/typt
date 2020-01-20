"""while_stmt_node.py - holds the AST node for while statements."""

from typt.stmt_node import StmtNode
from typt.suite_node import SuiteNode

from typt.typt_types import TestSuitePair


class WhileStmtNode(StmtNode):
    """While statement AST node."""

    def __init__(self, while_branch: TestSuitePair, else_branch: SuiteNode, depth=0):
        """Set initial values."""
        self.while_branch = while_branch
        self.else_branch = else_branch

        super().__init__(depth=depth)
