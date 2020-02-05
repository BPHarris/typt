"""func_def_node.py - holds the AST node for the func_def rule."""

from typt.node import Node

from typt.codegen import indent
from typt.environment import Environment
from typt.typt_types import Type, InvalidType, is_invalid_type

from typt.suite_node import SuiteNode
from typt.func_signature_node import FuncSignatureNode


class FuncDefNode(Node):
    """FuncDefNode AST node."""

    def __init__(self, func_signature: FuncSignatureNode, suite: SuiteNode, *args, **kwargs):
        """Initialise statement list."""
        self.func_signature = func_signature
        self.suite = suite

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Check type for the function body."""
        # RULE Function signature is valid
        # RULE Suite is valid

        # RULE 1
        func = is_invalid_type(self.func_signature.check_type(environment))

        # RULE 2
        suite = is_invalid_type(self.suite.check_type(environment))

        return InvalidType() if any([func, suite]) else Type()

    def codegen(self, indentation_level: int = 0) -> str:
        """Return Python3 equivalent."""
        pass
