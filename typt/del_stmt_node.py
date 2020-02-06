"""pass_stmt_node.py - holds the AST node for del(ete) statements."""

from typt.stmt_node import StmtNode
from typt.test.expr_op_node import ExprOpNode

from typt.codegen import indent
from typt.typt_types import Type
from typt.environment import Environment

from typing import List


class DelStmtNode(StmtNode):
    """Nothing to be implemented."""

    def __init__(self, expr_list: List[ExprOpNode]):
        """Set expression list."""
        self.expr_list = expr_list  # type: List[ExprOpNode]

    def check_type(self, environment: Environment) -> Type:
        """Check the validity of the del stmt's type."""
        pass

    def codegen(self, indentation_level: int = 0) -> str:
        """Return Python3 equivalent code."""
        indentation = indent(indentation_level)

        expr_list_code = ', '.join([e.codegen() for e in self.expr_list])

        return f'{indentation}del {expr_list_code}\n'
