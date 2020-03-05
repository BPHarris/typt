"""return_stmt_node.py - holds the AST node for return statements."""

from typt.stmt_node import StmtNode
from typt.test_node import TestNode

from typt.test.literal_node import LiteralNode

from typt.codegen import indent
from typt.environment import Environment
from typt.typt_types import Type, NoneType, log_type_error


class ReturnStmtNode(StmtNode):
    """ReturnStmt AST node."""

    def __init__(self, return_value: TestNode = None, *args, **kwargs):
        """Set return_value."""
        self.return_value = return_value

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Check the type of the return statement."""
        # RULE Must be inside function
        # RULE Return value type must match funtion return value

        # Get the function environment
        function_environment = environment
        while function_environment.scope != 'function':
            # Check RULE -- inside function scope
            if not function_environment.parent:
                log_type_error(
                    'return outside class',
                    function_environment.filename,
                    self.meta
                )

            function_environment = function_environment.parent

        # Get the function type
        function_name = function_environment.name
        function_type = function_environment.parent[function_name]

        # Check RULE -- no return value
        if function_type.return_type == NoneType():
            if not self.return_value or self.return_value.codegen() == 'None':
                return NoneType()
            return log_type_error(
                f'cannot return a value from a {NoneType()} function',
                environment.filename,
                self.meta
            )

        # If no return value provided, then implcit None
        if not self.return_value:
            self.return_value = LiteralNode(NoneType(), 'None', meta=self.meta)

        # Check RULE -- return value type must match expected return type
        return_type = self.return_value.check_type(environment)
        if not return_type == function_type.return_type:
            return log_type_error(
                f'return statement expected {function_type.return_type}, '
                f'received {return_type}',
                environment.filename,
                self.meta
            )

        return return_type

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the Python3 equivalent for a return statement."""
        indentation = indent(indentation_level)

        if not self.return_value:
            return f'{indentation}return'

        return f'{indentation}return {self.return_value.codegen()}'
