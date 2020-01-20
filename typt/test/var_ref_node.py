"""var_ref_node.py - holds the variable reference AST node."""

from typt.test.atom_node import AtomNode


class VarRefNode(AtomNode):
    """VarRefNode AST node."""

    def __init__(self, var_name: str, depth=0):
        """Set the variable name (var_name)."""
        self.var_name = var_name

        super().__init__(depth=0)
