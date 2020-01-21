"""if_stmt_node.py - holds the AST node for if statements."""

from typt.stmt_node import StmtNode
from typt.suite_node import SuiteNode

from typt.typt_types import TestSuitePair

from typing import Iterable


class IfStmtNode(StmtNode):
    """If statement AST node."""

    def __init__(self, if_branch: TestSuitePair, depth: int = 0):
        """Set initial values."""
        self.if_branch = if_branch      # type: TestSuitePair
        self.elif_branches = list()     # type: Iterable[TestSuitePair]
        self.else_branch = None         # type: SuiteNode

        super().__init__(depth=depth)
