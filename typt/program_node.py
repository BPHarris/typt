"""program_node.py - holds the AST node for the program rule."""

from typt.node import Node

from typt.typt_types import Type, InvalidType, is_invalid_type


class ProgramNode(Node):
    """Program AST node.

    Attributes:
        using_list  (list[UsingNode])   : The program's using-declarations
        stmt_list   (list[StmtNode])    : The program's statements

    """

    def __init__(self):
        """Initialise using_list and stmt_list."""
        self.using_list = list()
        self.stmt_list = list()

        super().__init__()

    def check_type(self) -> Type:
        """Check the program type, return Type if invalid."""
        # RULE Program valid if all using and all stmt are valid
        is_valid = True

        for u in self.using_list:
            is_valid = False if is_invalid_type(u.check_type()) else is_valid

        for s in self.stmt_list:
            is_valid = False if is_invalid_type(s.check_type()) else is_valid

        return Type() if is_valid else InvalidType()
