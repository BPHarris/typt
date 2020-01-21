"""program_node.py - holds the AST node for the program rule."""

from typt.node import Node


class ProgramNode(Node):
    """Program AST node.

    Attributes:
        using_list  (list[UsingNode])   : The program's using-declarations
        stmt_list   (list[StmtNode])    : The program's statements

    """

    def __init__(self, depth: int = 0):
        """Initialise using_list and stmt_list."""
        self.using_list = list()
        self.stmt_list = list()

        super().__init__(depth=depth)
