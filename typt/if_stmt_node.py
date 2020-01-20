"""if_stmt_node.py - holds the AST node for if statements."""

from typt.stmt_node import StmtNode
from typt.suite_node import SuiteNode

from typing import Iterable

from collections import namedtuple


TestSuitePair = namedtuple('TestSuitePair', ('test', 'suite'))
TestSuitePair.__doc__ = """Store a (test: TestNode, suite: SuiteNode) pair."""


class IfStmtNode(StmtNode):
    """If statement AST node."""

    def __init__(self, if_branch: TestSuitePair, depth=0):
        """Set initial values."""
        self.if_branch = if_branch      # type: TestSuitePair
        self.elif_branches = list()     # type: Iterable[TestSuitePair]
        self.else_branch = None         # type: SuiteNode

        super().__init__(depth=depth)
