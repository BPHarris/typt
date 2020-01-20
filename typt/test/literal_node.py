"""literal_node.py - holds AST node for literals."""

from typt.test.atom_node import AtomNode

from typt.typt_types import Type


class LiteralNode(AtomNode):
    """LiteralNode AST node."""

    def __init__(self, typt_type: Type, data: str, depth=0):
        """Store the data as a string literal for EzPz codegen."""
        self.typt_type = typt_type
        self.data = data

        super().__init__(depth=0)
