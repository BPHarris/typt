"""suite_node.py - holds the AST node for a suite (a.k.a. a block)."""

from typt.node import Node

from typt.codegen import indent
from typt.environment import Environment
from typt.typt_types import Type, InvalidType, is_invalid_type, log_type_error


class SuiteNode(Node):
    """SuiteNode AST node."""

    def __init__(self, *args, **kwargs):
        """Initialise statement list."""
        self.stmt_list = list()

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Perfrom type checking for this suite."""
        # RULE All stmts are valid

        suite_env = environment.add_child('suite')

        # RULE 1
        stmts_invalid = list()
        for stmt in self.stmt_list:
            stmts_invalid += [is_invalid_type(stmt.check_type(suite_env))]

        return InvalidType() if any(stmts_invalid) else Type()

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the Python3 equivalent for a suite."""
        pass
