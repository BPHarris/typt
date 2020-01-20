"""return_stmt_node.py - holds the AST node for return statements."""

from typt.stmt_node import StmtNode


class ReturnStmtNode(StmtNode):
    """ReturnStmt AST node."""

    def __init__(self, return_value: TestNode, depth=0):
        """Set return_value."""
        self.return_value = return_value

        super().__init__(depth=depth)
