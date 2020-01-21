"""for_stmt_node.py - holds the AST node for for statements."""

from typt.stmt_node import StmtNode
from typt.suite_node import SuiteNode


class ForStmtNode(StmtNode):
    """For statement AST node."""

    # TODO type annotations for expr_list/test_list
    def __init__(self, expr_list, test_list, for_branch: SuiteNode, else_branch: SuiteNode, depth: int = 0):
        """Set initial values."""
        self.expr_list = expr_list
        self.test_list = test_list
        self.for_branch = for_branch
        self.else_branch = else_branch

        super().__init__(depth=depth)
