"""suite_node.py - holds the AST node for a suite (a.k.a. a block)."""

from typt.node import Node


class SuiteNode(Node):
    """SuiteNode AST node."""

    def __init__(self, depth: int = 0):
        """Initialise statement list."""
        self.stmt_list = list()

        super().__init__(depth=depth)
