"""while_stmt_node.py - holds the AST node for while statements."""

from typt.stmt_node import StmtNode
from typt.suite_node import SuiteNode

from typt.codegen import indent
from typt.environment import Environment
from typt.typt_types import TestSuitePair, Type, InvalidType, is_invalid_type


class WhileStmtNode(StmtNode):
    """While statement AST node."""

    def __init__(self, while_branch: TestSuitePair, else_branch: SuiteNode, *args, **kwargs):
        """Set initial values."""
        self.while_branch = while_branch
        self.else_branch = else_branch

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Perform type checking for while-stmt."""
        # RULE Each test must be valid
        # RULE Each test must be coercible to a Boolean
        # RULE Each suite must be valid

        # Check RULE 1 and 2
        is_while_test_invalid = is_invalid_type(
            self.while_branch.test.check_type(environment)
        )

        # Check RULE 3 -- while suite
        is_while_suite_invalid = is_invalid_type(
            self.while_branch.suite.check_type(environment)
        )

        # Check RULE 3 -- else suite
        section_invalid = [is_while_test_invalid, is_while_suite_invalid]
        if self.else_branch:
            section_invalid += [
                is_invalid_type(self.else_branch.check_type(environment))
            ]

        return InvalidType() if any(section_invalid) else Type()

    def codegen(self, indentation_level: int = 0) -> str:
        """Return Python3 equivalent code."""
        indentation = indent(indentation_level)

        # Codegen for while-proper
        while_branch = f'{indentation}while {self.while_branch.test.codegen()}:\n'
        while_branch += f'{self.while_branch.suite.codegen(indentation_level)}'

        # Codegen for else branch
        else_branch = ''
        if self.else_branch:
            else_branch = f'{indentation}else:\n'
            else_branch += f'{self.else_branch.codegen(indentation_level)}'

        return f'{while_branch}{else_branch}'
