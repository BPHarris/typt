"""assignment_expr_stmt_node.py -- holds AST node for assignment expr stmt."""

from typt.stmt_node import StmtNode
from typt.test_node import TestNode
from typt.test.expr_op_node import ExprOpNode

from typt.codegen import indent
from typt.environment import Environment

from typt.typt_types import InvalidType, Type, is_invalid_type, log_type_error
from typt.typt_types import NoneType, BoolType, IntType, FloatType, StringType
from typt.typt_types import ListType, TupleType, SetType, DictType
from typt.typt_types import UserDefinedType


class AssignmentExprStmtNode(StmtNode):
    """AssignmentExprStmtNode AST node."""

    def __init__(self, lhs: TestNode, assignment_type: str, rhs: TestNode, *args, **kwargs):
        """Set the lhs, rhs, and the type of assignment (=, +=, etc.)."""
        self.lhs = lhs
        self.assignment_type = assignment_type
        self.rhs = rhs

        self.operator_method = ''

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Return the type of the contained expression."""
        # RULE op='=', lhs=A, rhs=B, where A == B => A
        # RULE Apply ExprOpNode rules
        # RULE Resulting type of ExprOpNode must be sub of lhs

        if self.assignment_type == '=':
            lhs_type = self.lhs.check_type(environment)
            rhs_type = self.rhs.check_type(environment)
        else:
            op = self.assignment_type.replace('=', '')

            as_expr = ExprOpNode(op, self.lhs, self.rhs, meta=self.meta)
            as_expr.check_type(environment)
            self.operator_method = as_expr.operator_method

            lhs_type = self.lhs.check_type(environment)
            rhs_type = as_expr.check_type(environment)

        # User Defined Type support
        if isinstance(rhs_type, UserDefinedType):
            rhs_type = rhs_type.get_object_type(environment)
            if not rhs_type:
                log_type_error(
                    f'the user-defined type {rhs_type} is not in scope',
                    environment.filename,
                    self.meta
                )

        # If rhs is not a subtype of lhs, then invalid
        if not rhs_type == lhs_type:
            return log_type_error(
                f'cannot assign {rhs_type} to variable of type {lhs_type}',
                environment.filename,
                self.meta
            )

        return lhs_type

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the Python3 code of this expression."""
        indentation = indent(indentation_level)

        operator = self.assignment_type
        lhs = self.lhs.codegen()
        rhs = self.rhs.codegen()

        if not self.operator_method:
            return f'{indentation}{lhs} {operator} {rhs}\n'
        return f'{indentation}{lhs} = {lhs}.{self.operator_method}({rhs})'
