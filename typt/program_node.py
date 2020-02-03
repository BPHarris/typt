"""program_node.py - holds the AST node for the program rule."""

from typt.node import Node

from typt.typt_types import Environment, Type, InvalidType, is_invalid_type


class ProgramNode(Node):
    """Program AST node.

    Attributes:
        using_list  (List[UsingNode])   : The program's using-declarations
        stmt_list   (List[StmtNode])    : The program's statements
        environment (Environment)       : The program's type environment

    """

    def __init__(self):
        """Initialise using_list and stmt_list."""
        self.using_list = list()
        self.stmt_list = list()

        super().__init__()

    def check_type(self, environment: Environment = None) -> Type:
        """Check the program type, return Type if invalid."""
        # RULE Program invalid if any using or stmt is invalid, valid otherwise

        u_types = map(lambda u: u.check_type(environment), self.using_list)
        s_types = map(lambda s: s.check_type(environment), self.stmt_list)

        is_not_valid = any(map(is_invalid_type, list(u_types) + list(s_types)))

        return InvalidType() if is_not_valid else Type()
