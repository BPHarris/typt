"""class_method_node.py -- holds the AST node for a class method."""

from typt.func_def_node import FuncDefNode

from typt.typt_types import Type
from typt.environment import Environment


class ClassMethodNode(FuncDefNode):
    """ClassMethodNode AST node."""

    def __init__(self, *args, **kwargs):
        """Specialisation of function definition."""
        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Check method type is valid."""
        return super().check_type(environment)

    def codegen(self, indentation_level: int = 0) -> str:
        """Return Python3 equivalent code."""
        return super().codegen(indentation_level)
