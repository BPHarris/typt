"""using_node.py - holds the AST node for the using rule."""

from typt.node import Node


class UsingNode(Node):
    """Using AST node.

    Attributes:
        function_signature_list (list[UsingNode])   : The function signatures
        library_name            (str)               : The library name
        library_alias           (str)               : The library alias

    """

    def __init__(self, library_name: str = '', library_alias: str = '', depth: int = 0):
        """Initialise using_list and stmt_list."""
        self.function_signature_list = list()
        self.library_name = library_name
        self.library_alias = library_alias

        super().__init__()
