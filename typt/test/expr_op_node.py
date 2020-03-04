"""expr_op_node.py - holds the AST node for an expression.

Expressions are binary operations (grammar: or_expr to term, inclusive).
"""

from typt.test_node import TestNode

from typt.codegen import indent
from typt.environment import Environment
from typt.typt_types import Type, BoolType, IntType, FloatType, log_type_error


class ExprOpNode(TestNode):
    """ExprOpNode AST node."""

    def __init__(self, operator: str, lhs: TestNode, rhs: TestNode, *args, **kwargs):
        """Set operator and operands."""
        self.operator = operator
        self.lhs = lhs
        self.rhs = rhs

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Check the type of the expression operation."""
        # RULE lhs and rhs are valid
        lhs_type = self.lhs.check_type(environment)
        rhs_type = self.rhs.check_type(environment)

        # RULE op='|', lhs=Bool, rhs=Bool => Bool
        # RULE op='|', lhs=Int, rhs=Int => Int
        # RULE op='^', lhs=Bool, rhs=Bool => Bool
        # RULE op='^', lhs=Int, rhs=Int => Int
        # RULE op='&', lhs=Bool, rhs=Bool => Bool
        # RULE op='&', lhs=Int, rhs=Int => Int

        # RULE op='<<', lhs=Int, rhs=Int => Int
        # RULE op='>>', lhs=Int, rhs=Int => Int

        # RULE op='+', lhs=A, rhs=A, where A in Numeric => A
        # RULE op='+', lhs=A, rhs=B, where A, B in Numeric and A =/= B => Float
        # RULE op='-', lhs=A, rhs=A, where A in Numeric => A
        # RULE op='-', lhs=A, rhs=B, where A, B in Numeric and A =/= B => Float
        # RULE op='*', lhs=A, rhs=A, where A in Numeric => A
        # RULE op='*', lhs=A, rhs=B, where A, B in Numeric and A =/= B => Float
        # RULE op='%', lhs=A, rhs=A, where A in Numeric => A
        # RULE op='%', lhs=A, rhs=B, where A, B in Numeric and A =/= B => Float

        # RULE op='/',  lhs=A, rhs=B, where A, B in Numeric => Float
        # RULE op='//', lhs=A, rhs=B, where A, B in Numeric => Int

        bitwise_operators = ('|', '^', '&')
        arithmetic_shift_operators = ('<<', '>>')
        safe_arithmetic_operators = ('+', '-', '*', '%')

        numeric = (IntType, FloatType)

        # Check RULEs for bitwise operators
        if self.operator in bitwise_operators:
            # lhs=Bool, rhs=Bool => Bool
            if isinstance(lhs_type, BoolType) \
                    and isinstance(rhs_type, BoolType):
                return BoolType()
            # lhs=Int, rhs=Int => Int
            if isinstance(lhs_type, IntType) and isinstance(rhs_type, IntType):
                return IntType()
            # Otherwise, error
            return log_type_error(
                f'no operator {self.operator} for {lhs_type} and {rhs_type}',
                environment.filename,
                self.meta
            )

        # Check RULEs for arithmetic shift operators
        if self.operator in arithmetic_shift_operators:
            if isinstance(lhs_type, IntType) and isinstance(rhs_type, IntType):
                return IntType()
            return log_type_error(
                f'no operator {self.operator} for {lhs_type} and {rhs_type}',
                environment.filename,
                self.meta
            )

        # Check RULEs for arithmetic operators that are integer safe
        if self.operator in safe_arithmetic_operators:
            if isinstance(lhs_type, numeric) and isinstance(rhs_type, numeric):
                # lhs=A, rhs=A, where A in Numeric => A
                if lhs_type == rhs_type:
                    return lhs_type
                # lhs=A, rhs=B, where A, B in Numeric and A =/= B => Float
                if lhs_type != rhs_type:
                    return FloatType()
            return log_type_error(
                f'no operator {self.operator} for {lhs_type} and {rhs_type}',
                environment.filename,
                self.meta
            )

        # Check RULEs for '/' operator
        # lhs=A, rhs=B, where A, B in Numeric => Float
        if self.operator == '/':
            if isinstance(lhs_type, numeric) and isinstance(rhs_type, numeric):
                return FloatType()
            return log_type_error(
                f'no operator {self.operator} for {lhs_type} and {rhs_type}',
                environment.filename,
                self.meta
            )

        # Check RULES for '//' operator
        # op='//', lhs=A, rhs=A, where A in Numeric => Int
        if self.operator == '//':
            if isinstance(lhs_type, numeric) and isinstance(rhs_type, numeric):
                return IntType()
            return log_type_error(
                f'no operator {self.operator} for {lhs_type} and {rhs_type}',
                environment.filename,
                self.meta
            )

        return log_type_error(
            f'unsupported operator {self.operator}',
            environment.filename,
            self.meta
        )

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the Python3 code for the expression operation."""
        indentation = indent(indentation_level)

        lhs = self.lhs.codegen()
        rhs = self.rhs.codegen()

        return f'{indentation}{lhs} {self.operator} {rhs}'
