"""literal_node.py -- holds AST node for literals."""

from typt.test.atom_node import AtomNode

from typt.codegen import indent
from typt.typt_types import Type
from typt.environment import Environment


class LiteralNode(AtomNode):
    """LiteralNode AST node."""

    def __init__(self, typt_type: Type, data: str, *args, **kwargs):
        """Store the data as a string literal for EzPz codegen."""
        self.typt_type = typt_type
        self.data = data

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Return the type of the literal."""
        return self.typt_type

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the contents of the literal, in Python3 form."""
        return f'{indent(indentation_level)}{self.data}'
