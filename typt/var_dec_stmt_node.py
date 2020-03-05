"""var_dec_stmt_node.py -- holds AST node for variable declaration stmt."""

from typt.stmt_node import StmtNode
from typt.test_node import TestNode

from typt.codegen import indent
from typt.typt_types import UserDefinedType
from typt.typt_types import Type, is_invalid_type, log_type_error
from typt.environment import Environment


class VarDecStmtNode(StmtNode):
    """VarDecStmtNode AST node."""

    def __init__(self, lhs: str, var_type: Type, rhs: TestNode, *args, **kwargs):
        """Set the lhs, rhs (default=None), and the type of variable."""
        self.lhs = lhs
        self.var_type = var_type
        self.rhs = rhs

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Return the type of the contained expression."""
        # RULE RHS must be a valid type
        # RULE Name free in environment
        # RULE Given type is valid
        # RULE RHS type matches given type

        rhs_type = self.rhs.check_type(environment)

        # Check RULE 1
        if is_invalid_type(rhs_type):
            log_type_error(
                'invalid assignment type', environment.filename, self.meta
            )

        # Check RULE 2
        if environment.get(self.lhs):
            return log_type_error(
                f'{self.lhs} not free in {environment.scope}',
                environment.filename,
                self.meta
            )

        # Get ObjectType if UDT
        var_type = self.var_type
        if isinstance(self.var_type, UserDefinedType):
            var_type = self.var_type.get_object_type(environment)

        # If UDT invalid, log error
        if not var_type:
            return log_type_error(
                f'the user-defined type {var_type} is not in scope',
                environment.filename,
                self.meta
            )

        # Check RULE 3
        if is_invalid_type(var_type):
            return log_type_error(
                'given variable type invalid', environment.filename, self.meta
            )

        # Check RULE 4
        if not rhs_type == var_type:
            return log_type_error(
                f'mismatch between declared type ({var_type}) '
                f'and assigned type ({rhs_type})',
                environment.filename,
                self.meta
            )

        # Add variable to environment
        environment[self.lhs] = var_type

        return environment[self.lhs]

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the Python3 code of thi given expression."""
        indentation = indent(indentation_level)

        return f'{indentation}{self.lhs} = {self.rhs.codegen()}\n'
