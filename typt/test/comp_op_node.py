"""comp_op_node.py - holds the AST node for a comparison operation.

Comparison operations are binary operations.
"""

from typt.test_node import TestNode

from typt.codegen import indent
from typt.typt_types import NoneType, BoolType, IntType, FloatType, StringType
from typt.typt_types import ListType, TupleType, SetType, DictType
from typt.typt_types import FunctionType, ObjectType
from typt.typt_types import Type, InvalidType, is_invalid_type, log_type_error
from typt.environment import Environment


class CompOpNode(TestNode):
    """CompOpNode AST node."""

    def __init__(self, operator: str, lhs: TestNode, rhs: TestNode, *args, **kwargs):
        """Set operator and operands."""
        self.operator = operator
        self.lhs = lhs
        self.rhs = rhs

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Check the type of the comparison."""
        # TODO Operator polymorphism
        # RULE lhs and rhs are valid

        # RULE '==', equality operator valid for any two comparable types
        # RULE '==', TODO OPERATOR POLYMORPHISM
        # RULE '!=', equality operator valid for any two comparable types
        # RULE '!=', TODO OPERATOR POLYMORPHISM

        # RULE '<', lhs : (Int|Float), rhs : (Int|Float) => Bool
        # RULE '>', lhs : (Int|Float), rhs : (Int|Float) => Bool
        # RULE '<=', lhs : (Int|Float), rhs : (Int|Float) => Bool
        # RULE '>=', lhs : (Int|Float), rhs : (Int|Float) => Bool

        # TODO 'in', 'not in'   (add with operator polymorphism)
        # TODO 'is', 'is not'    (add with operator polymorphism)

        numeric = (IntType, FloatType)
        comparable = (
            NoneType, BoolType, IntType, FloatType, StringType,
            ListType, TupleType, SetType, DictType, FunctionType
        )

        # Check RULE 1
        lhs_type = self.lhs.check_type(environment)
        rhs_type = self.rhs.check_type(environment)
        if is_invalid_type(lhs_type) or is_invalid_type(rhs_type):
            return InvalidType()

        # Check RULE 2-4 -- '==', '!='
        if self.operator == '==' or self.operator == '!=':
            if isinstance(lhs_type, comparable) \
                    and isinstance(rhs_type, comparable):
                return BoolType()
            if isinstance(lhs_type, ObjectType) \
                    or isinstance(rhs_type, ObjectType):
                raise NotImplementedError('Todo: Add operator polymorphism')
            return log_type_error(
                f'no equality operator provided for {lhs_type} and {rhs_type}',
                environment.filename,
                self.meta
            )

        # Check RULE 5-8 -- '<', '>', '<=', '>='
        if self.operator in ('<', '>', '<=', '>='):
            if isinstance(lhs_type, numeric) and isinstance(rhs_type, numeric):
                return BoolType()
            return log_type_error(
                f'no operator \'<\' for {lhs_type} and {rhs_type}',
                environment.filename,
                self.meta
            )

        return log_type_error(
            f'no operator \'{self.operator}\' for {lhs_type} and {rhs_type}',
            environment.filename,
            self.meta
        )

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the Python3 code for the comparison operation."""
        indentation = indent(indentation_level)

        lhs = self.lhs.codegen()
        rhs = self.rhs.codegen()

        return f'{indentation}{lhs} {self.operator} {rhs}'
