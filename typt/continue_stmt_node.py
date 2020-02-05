"""continue_stmt_node.py -- holds the AST node for continue statements."""

from typt.stmt_node import StmtNode

from typt.codegen import indent
from typt.typt_types import Type, log_type_error
from typt.environment import Environment


class ContinueStmtNode(StmtNode):
    """Class for 'continue' statement AST node."""

    def check_type(self, environment: Environment) -> Type:
        """Perform type checking on this break statement."""
        # RULE Continue stmt can only occur inside a loop (for/while)
        if not any([environment.in_scope(l) for l in ('for', 'while')]):
            return log_type_error(
                'continue not inside loop', environment.filename, self.meta
            )

        return Type()

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the Python3 equivelent to a continue stmt."""
        return f'{indent(indentation_level)}continue\n'
