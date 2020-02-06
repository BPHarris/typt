"""assignment_expr_stmt_node.py -- holds AST node for assignment expr stmt."""

from typt.stmt_node import StmtNode
from typt.test_node import TestNode

from typt.codegen import indent
from typt.environment import Environment

from typt.typt_types import InvalidType, Type, is_invalid_type, log_type_error
from typt.typt_types import NoneType, BoolType, IntType, FloatType, StringType
from typt.typt_types import ListType, TupleType, SetType, DictType


class AssignmentExprStmtNode(StmtNode):
    """AssignmentExprStmtNode AST node."""

    def __init__(self, lhs: TestNode, assignment_type: str, rhs: TestNode, *args, **kwargs):
        """Set the lhs, rhs, and the type of assignment (=, +=, etc.)."""
        self.lhs = lhs
        self.assignment_type = assignment_type
        self.rhs = rhs

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Return the type of the contained expression."""
        # RULE LHS and RHS must be valid
        # RULE a = b valid for b <: a
        # RULE a O= b, for O in (+, -), valid when both are same base type
        # RULE a O= b, for O in (*, /), valid if both Int or Float
        # RULE a *= b, valid for a=(Str|List|...) and b=Int
        # RULE a %= b, valid both Str or both Int
        # RULE a B= b, for B in (&, |, ^), valid for both Bool or both Int
        # RULE <<= and >>= only valid if both Int
        # RULE **= valid for both Int OR LHS Float and RHS Number
        # RULE //= valid for LHS Int and RHS Number
        lhs_type = self.lhs.check_type(environment)
        rhs_type = self.rhs.check_type(environment)

        lhs_int, lhs_float = lhs_type == IntType(), lhs_type == FloatType()
        rhs_int, rhs_float = rhs_type == IntType(), rhs_type == FloatType()
        lhs_str, rhs_str = lhs_type == StringType(), rhs_type == StringType()
        lhs_bool, rhs_bool = lhs_type == BoolType(), rhs_type == BoolType()

        non_none_base_types = (
            BoolType(), IntType(), FloatType(), StringType(),
            ListType(), TupleType(), SetType(), DictType()
        )

        repeatable_types = (
            StringType(), ListType(), TupleType(), SetType(), DictType()
        )

        expr_stmt_type = InvalidType()

        # Check RULE 1
        if is_invalid_type(lhs_type) or is_invalid_type(rhs_type):
            return InvalidType()

        # Check RULE 2
        if self.assignment_type == '=' and rhs_type == lhs_type:
            expr_stmt_type = lhs_type

        # Check RULE 3
        if self.assignment_type in ('+=', '-='):
            if rhs_type == lhs_type and lhs_type in non_none_base_types:
                expr_stmt_type = lhs_type

        # Check RULE 4
        if self.assignment_type in ('*=', '/='):
            if lhs_int and rhs_int:
                expr_stmt_type = lhs_type
            if lhs_float and rhs_float:
                expr_stmt_type = lhs_type

        # Check RULE 5
        if self.assignment_type == '*=':
            if lhs_type in repeatable_types and rhs_int:
                expr_stmt_type = lhs_type

        # Check RULE 5
        if self.assignment_type == '%=':
            if lhs_int and rhs_int:
                expr_stmt_type = lhs_type
            if lhs_str and rhs_str:
                # TODO Extra check needed? For %c in lhs?
                expr_stmt_type = lhs_type

        # Check RULE 6
        if self.assignment_type in ('&=', '|=', '^='):
            if lhs_bool and rhs_bool:
                expr_stmt_type = lhs_type
            if lhs_int and rhs_int:
                expr_stmt_type = lhs_type

        # Check RULE 7
        if self.assignment_type in ('<<=', '>>='):
            if lhs_bool and rhs_bool:
                expr_stmt_type = lhs_type

        # Check RULE 8
        if self.assignment_type == '**=':
            if lhs_int and rhs_int:
                expr_stmt_type = lhs_type
            if lhs_float and (rhs_int or rhs_float):
                expr_stmt_type = lhs_type

        # Check RULE 9
        if self.assignment_type == '//=':
            if lhs_int and (rhs_int or rhs_float):
                expr_stmt_type = lhs_type

        # If the final type is invalid, inform the user
        if is_invalid_type(expr_stmt_type):
            operator = self.assignment_type
            return log_type_error(
                f'unsuported types for {operator}: {lhs_type} and {rhs_type}',
                environment.filename,
                self.meta
            )

        return expr_stmt_type

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the Python3 code of this expression."""
        operator = self.assignment_type
        return f'{indent(indentation_level)}{self.lhs} {operator} {self.rhs}\n'
