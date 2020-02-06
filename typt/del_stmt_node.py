"""pass_stmt_node.py - holds the AST node for del(ete) statements."""

from typt.stmt_node import StmtNode

from typt.codegen import indent
from typt.typt_types import Type, InvalidType, is_invalid_type, log_type_error
from typt.environment import Environment


class DelStmtNode(StmtNode):
    """Nothing to be implemented."""

    def __init__(self, target: str):
        """Set expression list."""
        self.target = target

    def check_type(self, environment: Environment) -> Type:
        """Check the validity of the del stmt's type."""
        # RULE Target must exist in environment

        if not environment.get(self.target):
            return log_type_error(
                f'{self.target} does not exist in {environment.scope}',
                environment.filename,
                self.meta
            )

        # Remove expr from environment
        del environment[self.target]

        return Type()

    def codegen(self, indentation_level: int = 0) -> str:
        """Return Python3 equivalent code."""
        indentation = indent(indentation_level)

        return f'{indentation}del {self.target}\n'
