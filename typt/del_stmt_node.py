"""pass_stmt_node.py - holds the AST node for del(ete) statements."""

from typt.stmt_node import StmtNode
from typt.test.expr_op_node import ExprOpNode

from typing import List


class DelStmtNode(StmtNode):
    """Nothing to be implemented."""

    def __init__(self, expr_list: List[ExprOpNode]):
        """Set expression list."""
        self.expr_list = expr_list  # type: List[ExprOpNode]
