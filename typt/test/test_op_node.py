"""test_op_node.py - holds AST node for a test operation.

A test operation is one of or_test, and_test, or not_test in Typt.g4.

"""

from typt.test_node import TestNode

from typing import List

from typt.codegen import indent
from typt.environment import Environment
from typt.typt_types import Type, BoolType, log_type_error


class TestOpNode(TestNode):
    """TestOpNode AST node."""

    def __init__(self, operator: str, lhs: TestNode):
        """Create initial operand list as just the lhs operand."""
        self.operator = operator
        self.operands = list([lhs])     # type: List[TestNode]

    def check_type(self, environment: Environment) -> Type:
        """Check the type of the test operation."""
        # RULE must have valid operands
        # RULE 'not', only one operand allowed
        # RULE 'and', all operands must be coercible to bool,
        #       resultant is BoolType
        # RULE 'or', all operands must be coercible to bool,
        #       resultant is BoolType

        # Check RULE 1
        operand_types = [o.check_type(environment) for o in self.operands]

        # Check operands not empty
        if not operand_types:
            return log_type_error(
                f'not enough operands for operator \'{self.operator}\'',
                environment.filename,
                self.meta
            )

        # Check RULE 2 -- 'not' test
        if self.operator == 'not':
            if len(self.operands) != 1:
                return log_type_error(
                    'not operator takes exactly one operand',
                    environment.filename,
                    self.meta
                )

            # NOTE All Types are coercible to bool
            return BoolType()

        # Check RULE 3 -- 'and' test
        if self.operator == 'and':
            # NOTE All Types are coercible to bool
            return BoolType()

        # Check RULE 4 -- 'or' test
        if self.operator == 'or':
            # NOTE All Types are coercible to bool
            return BoolType()

        return log_type_error(
            f'unsupported operator \'{self.operator}\'',
            environment.filename,
            self.meta
        )

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the Python3 code for the expression operation."""
        indentation = indent(indentation_level)

        # Get the code of the test operation
        output = self.operator.join(map(lambda o: o.codegen(), self.operands))
        return f'{indentation}{output}'
