"""class_method_node.py - holds the AST node for a class method."""

from typt.func_def_node import FuncDefNode
from typt.func_signature_node import FuncSignatureNode

from typt.suite_node import SuiteNode


class ClassMethodNode(FuncDefNode):
    """ClassMethodNode AST node."""

    def __init__(self, signature: FuncSignatureNode, suite: SuiteNode):
        """Specialisation of function definition."""
        super().__init__(signature, suite)
