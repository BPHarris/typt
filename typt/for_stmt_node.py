"""for_stmt_node.py - holds the AST node for for statements."""

from typt.stmt_node import StmtNode
from typt.suite_node import SuiteNode
from typt.test.expr_op_node import ExprOpNode
from typt.test_node import TestNode

from typing import List

from typt.codegen import indent
from typt.environment import Environment
from typt.typt_types import Type, InvalidType, is_invalid_type, log_type_error


class ForStmtNode(StmtNode):
    """For statement AST node."""

    def __init__(self, expr_list: List[ExprOpNode], test_list: List[TestNode], for_branch: SuiteNode, else_branch: SuiteNode, *args, **kwargs):
        """Set initial values."""
        self.expr_list = expr_list
        self.test_list = test_list
        self.for_branch = for_branch
        self.else_branch = else_branch

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Perfrom type checking for 'for' statement."""
        # RULE Each expr must be valid
        # RULE Each test must be valid
        # RULE Each test must be coercible to a Boolean
        # RULE Each suite must be valid

        # TODO Allow for test list longer than one
        # RULE Test list length must be exactly one -- for now

        # RULE 1
        exprs_invalid = list()
        for expr in self.expr_list:
            exprs_invalid += [
                is_invalid_type(expr.check_type(environment))
            ]

        # RULE 2 and 3
        tests_invalid = list()
        for test in self.test_list:
            tests_invalid += [
                is_invalid_type(test.check_type(environment))
            ]

        # RULE 4 -- for branch
        for_suite_invalid = is_invalid_type(
            self.for_branch.check_type(environment)
        )

        # RULE 4 -- else branch
        else_suite_invalid = True
        if self.else_branch:
            else_suite_invalid = self.else_branch.check_type(environment)

        # RULE 5
        n_tests = len(self.test_list)
        if n_tests > 1:
            return log_type_error(
                f'too many values to unpack (got {n_tests} expected 1)',
                environment.filename,
                self.meta
            )

        suites_invalid = [for_suite_invalid, else_suite_invalid]
        types_invalid = exprs_invalid + tests_invalid + suites_invalid
        return InvalidType() if any(types_invalid) else Type()

    def codegen(self, indentation_level: int = 0) -> str:
        pass
