"""suite_node.py - holds the AST node for a suite (a.k.a. a block)."""

from typt.node import Node

from typt.environment import Environment
from typt.typt_types import Type, InvalidType, is_invalid_type


class SuiteNode(Node):
    """SuiteNode AST node."""

    def __init__(self, *args, **kwargs):
        """Initialise statement list."""
        self.stmt_list = list()

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Perfrom type checking for this suite."""
        # RULE All stmts are valid

        # RULE 1
        stmts_invalid = list()
        for stmt in self.stmt_list:
            stmts_invalid += [is_invalid_type(stmt.check_type(environment))]

        return InvalidType() if any(stmts_invalid) else Type()

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the Python3 equivalent for a suite."""
        stmts_code = '\n'
        for stmt in self.stmt_list:
            stmts_code += f'{stmt.codegen(indentation_level + 1)}'

        return f'{stmts_code}'
