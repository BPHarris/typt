"""stmt_node.py - holds the base stmt AST node."""

from typt.node import Node


class StmtNode(Node):
    """StmtNode AST node."""

    def __init__(self, depth: int = 0):
        """Call super initialiser."""
        super().__init__()