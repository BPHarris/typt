"""class_initialiser_node.py - holds the AST node for a class initialiser."""

from typt.suite_node import SuiteNode
from typt.func_def_node import FuncDefNode
from typt.func_signature_node import FuncSignatureNode

from typt.environment import Environment
from typt.typt_types import NameTypePair, Type, NoneType

from typing import List


class ClassInitialiserNode(FuncDefNode):
    """ClassInitialiserNode AST node."""

    def __init__(self, parameters: List[NameTypePair], suite: SuiteNode, *args, **kwargs):
        """Create as FunDefNode with fixed name."""
        # Create signature with return type and add parameters
        func_signnature = FuncSignatureNode('__init__', NoneType())
        func_signnature.parameter_list = parameters

        super().__init__(func_signnature, suite, *args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Check initialiser type is valid."""
        return super().check_type(environment)

    def codegen(self, indentation_level: int = 0) -> str:
        """Return Python3 equivalent code."""
        return super().codegen(indentation_level)
