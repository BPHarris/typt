"""func_def_node.py - holds the AST node for the func_def rule."""

from typt.node import Node

from typt.suite_node import SuiteNode
from typt.func_signature_node import FuncSignatureNode


class FuncDefNode(Node):
    """FuncDefNode AST node."""

    def __init__(self, func_signature: FuncSignatureNode, suite: SuiteNode, depth=0):
        """Initialise statement list."""
        self.func_signature = func_signature
        self.suite = suite

        super().__init__(depth=depth)
