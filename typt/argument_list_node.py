"""argument_list_node.py - holds the AST node for the argument_list rule."""

from typt.node import Node

from typt.codegen import indent
from typt.typt_types import Type
from typt.environment import Environment


class ArgumentListNode(Node):
    """ArgumentListNode AST node.

    Attributes:
        argument_list   (List[TestNode])    : The functions's parameter list

    """

    def __init__(self):
        """Initialise argument_list."""
        self.argument_list = list()

    def check_type(self, environment: Environment) -> Type:
        """Delegate to super (raise error)."""
        return super().check_type()

    def codegen(self, indentation_level: int = 0) -> str:
        """Generate code for argument list."""
        return ', '.join([a.codegen() for a in self.argument_list])
