"""for_stmt_node.py - holds the AST node for for statements."""

from typt.stmt_node import StmtNode
from typt.suite_node import SuiteNode
from typt.test.expr_op_node import ExprOpNode
from typt.test_node import TestNode

from typing import List


class ForStmtNode(StmtNode):
    """For statement AST node."""

    def __init__(self, expr_list: List[ExprOpNode], test_list: List[TestNode], for_branch: SuiteNode, else_branch: SuiteNode, *args, **kwargs):
        """Set initial values."""
        self.expr_list = expr_list      # type: List[ExprOpNode]
        self.test_list = test_list      # type: List[TestNode]
        self.for_branch = for_branch
        self.else_branch = else_branch

        super().__init__(*args, **kwargs)
