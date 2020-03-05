"""unary_expr_op_node.py - holds the AST node for a unary expression."""

from typt.test_node import TestNode

from typt.codegen import indent
from typt.environment import Environment
from typt.typt_types import Type, IntType, FloatType, log_type_error


class UnaryExprOpNode(TestNode):
    """UnaryExprOpNode AST node."""

    def __init__(self, operator: str, rhs: TestNode, *args, **kwargs):
        """Set operator and operands."""
        self.operator = operator
        self.rhs = rhs

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Check the type of the unary expression."""
        # RULE op='+', rhs : T => T. For all T in {Int, Float}
        # RULE op='-', rhs : T => T. For all T in {Int, Float}
        # RULE op='~', rhs : Int => Int

        rhs_type = self.rhs.check_type(environment)

        # Check RULE 1 & 2 -- '+' & '-' operators
        if self.operator == '+' or self.operator == '-':
            if not isinstance(rhs_type, (IntType, FloatType)):
                return log_type_error(
                    f'unsuppported operator \'{self.operator}\' on {rhs_type}',
                    environment.filename,
                    self.meta
                )
            return rhs_type

        # Check RULE 3 -- '~'
        if self.operator == '~':
            if not isinstance(rhs_type, IntType):
                return log_type_error(
                    f'unsupported operator \'~\' on {rhs_type}',
                    environment.filename,
                    self.meta
                )
            return rhs_type

        return log_type_error(
            f'unsupported operator \'{self.operator}\'',
            environment.filename,
            self.meta
        )

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the Python3 code for the expression operation."""
        indentation = indent(indentation_level)

        return f'{indentation}{self.operator}{self.rhs.codegen()}'
