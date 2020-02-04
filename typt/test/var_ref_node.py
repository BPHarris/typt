"""var_ref_node.py - holds the variable reference AST node."""

from typt.test.atom_node import AtomNode

from typt.codegen import indent
from typt.typt_types import Type
from typt.environment import Environment


class VarRefNode(AtomNode):
    """VarRefNode AST node."""

    def __init__(self, var_name: str, *args, **kwargs):
        """Set the variable name (var_name)."""
        self.var_name = var_name

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Return the type of the variable being referenced."""
        return environment.get(self.var_name)

    def codegen(self, indentation_level: int = 0) -> str:
        """Return code of the variable refence, in Python3 form."""
        return f'{indent(indentation_level)}{self.var_name}'
