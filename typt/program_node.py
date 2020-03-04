"""program_node.py - holds the AST node for the program rule."""

from typt.node import Node

from typt.environment import Environment
from typt.typt_types import Type, InvalidType, is_invalid_type


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

        def map_check_type(node):
            return node.check_type(environment)

        u_types = list(map(map_check_type, self.using_list))
        s_types = list(map(map_check_type, self.stmt_list))

        is_not_valid = any(map(is_invalid_type, u_types + s_types))

        return InvalidType() if is_not_valid else Type()

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the generated code for the ProgramNode."""
        output_code = 'from typt_stdlib import *\n\n'

        for using in self.using_list:
            output_code += using.codegen(indentation_level=0) + '\n'

        for stmt in self.stmt_list:
            output_code += stmt.codegen(indentation_level=0) + '\n'

        return output_code
