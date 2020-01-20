"""pass_stmt_node.py - holds the AST node for del(ete) statements."""

from typt.stmt_node import StmtNode


class DelStmtNode(StmtNode):
    """Nothing to be implemented."""

    # TODO Type annotation for expr_list
    def __init__(self, expr_list: None, depth=0):
        """Set expression list."""
        self.expr_list = expr_list

        super().__init__(depth=0)
