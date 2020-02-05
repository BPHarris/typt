"""if_stmt_node.py -- holds the AST node for if statements."""

from typt.stmt_node import StmtNode
from typt.suite_node import SuiteNode

from typt.codegen import indent
from typt.environment import Environment
from typt.typt_types import TestSuitePair, Type, InvalidType, is_invalid_type

from typing import Iterable


class IfStmtNode(StmtNode):
    """If statement AST node."""

    def __init__(self, if_branch: TestSuitePair, *args, **kwargs):
        """Set initial values."""
        self.if_branch = if_branch      # type: TestSuitePair
        self.elif_branches = list()     # type: Iterable[TestSuitePair]
        self.else_branch = None         # type: SuiteNode

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Perform type checking on if-stmt."""
        # RULE Each test must be valid
        # RULE Each test must be implicitly coercable to a BoolType
        # RULE Each suite must be valid

        # NOTE Each suite occcurs in a sub-environment

        test_types = []
        types_invalid = []

        # Check RULE 1
        for branch in [self.if_branch] + self.elif_branches:
            test_types += [branch.test.check_type(environment)]

        # Check RULE 2
        # All valid types can be coerced to a Boolean
        # NOTE Does not log_type_error as this is handled by RULE 1
        for test_type in test_types:
            types_invalid += [is_invalid_type(test_type)]

        # Check RULE 3
        for branch in [self.if_branch] + self.elif_branches:
            types_invalid += [
                is_invalid_type(branch.suite.check_type(environment))
            ]
        if self.else_branch:
            types_invalid += [
                is_invalid_type(self.else_branch.check_type(environment))
            ]

        return InvalidType() if any(types_invalid) else Type()

    def codegen(self, indentation_level: int = 0) -> str:
        """Return equivalent Python3 code."""
        indentation = indent(indentation_level)

        # If-branch
        if_branch = f'{indentation}if {self.if_branch.test.codegen()}:'
        if_branch += f'{self.if_branch.suite.codegen(indentation_level)}'

        # Elif-branches
        elif_branches = list()
        for branch in self.elif_branches:
            elif_branches = f'{indentation}elif {branch.test.codegen()}:'
            elif_branches += f'{branch.suite.codegen(indentation_level)}'

        # Else codegen
        else_branch = ''
        if self.else_branch:
            else_branch = f'else:{self.else_branch.codegen(indentation_level)}'

        return f'{if_branch}{str().join(elif_branches)}{else_branch}'
