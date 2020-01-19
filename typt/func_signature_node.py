"""func_signature_node.py - holds the AST node for the func_signature rule."""

from typt.node import Node


class FuncSignature(Node):
    """FuncSignature AST node.

    Attributes:
        name            (str)                : The function name
        parameter_list  (list[(name, type)]) : The functions's parameter list
        return_type     (str)                : The functions's return type

    """

    def __init__(self, name: str, return_type: str, depth: int = 0):
        """Initialise using_list and stmt_list."""
        self.name = name
        self.parameter_list = list()
        self.return_type = return_type

        super().__init__()