"""break_stmt_node.py - holds the AST node for break statements."""

from typt.stmt_node import StmtNode

from typt.codegen import indent
from typt.typt_types import Type, log_type_error
from typt.environment import Environment


class BreakStmtNode(StmtNode):
    """Class 'break' statement AST node."""

    def check_type(self, environment: Environment) -> Type:
        """Perform type checking on this break statement."""
        # RULE Break stmt can only occur inside a loop (for/while)
        if environment.in_scope('for') or environment.in_scope('while'):
            return log_type_error(
                'break outside loop', environment.filename, self.meta
            )

        return Type()

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the Python3 equivelent to a break stmt."""
        return '{indent}break'.format(indent=indent(indentation_level))
