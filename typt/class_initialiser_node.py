"""class_initialiser_node.py - holds the AST node for a class initialiser."""

from typt.func_def_node import FuncDefNode
from typt.func_signature_node import FuncSignatureNode

from typt.suite_node import SuiteNode

from typt_types import NoneType, NameTypePair

from typing import List


class ClassInitialiserNode(FuncDefNode):
    """ClassInitialiserNode AST node."""

    def __init__(self, parameters: List[NameTypePair], suite: SuiteNode):
        """Create as FunDefNode with fixed name."""
        # Create signature with return type and add parameters
        func_signnature = FuncSignatureNode('self', NoneType)
        func_signnature.parameter_list = parameters

        super().__init__(func_signnature, suite)
