"""func_signature_node.py - holds the AST node for the func_signature rule."""

from typt.node import Node

from typt.codegen import indent
from typt.environment import Environment
from typt.typt_types import UserDefinedType
from typt.typt_types import is_invalid_type, log_type_error
from typt.typt_types import NameTypePair, Type, InvalidType, FunctionType

from typing import List


class FuncSignatureNode(Node):
    """FuncSignatureNode AST node."""

    def __init__(self, name: str, return_type: Type, *args, **kwargs):
        """Initialise using_list and stmt_list."""
        self.name = name
        self.parameter_list = list()    # type: List[NameTypePair]
        self.return_type = return_type

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Check the type of a function signature."""
        # RULE All parameter types must be valid
        # RULE All return types must be valid

        # RULE 1
        params_invalid = list()
        parameter_list = list()
        for param in self.parameter_list:
            # Get ObjectType if UDT
            param_type = param.type
            if isinstance(param.type, UserDefinedType):
                param_type = param.type.get_object_type(environment)

            # If UDT invalid, log error
            if not param_type:
                return log_type_error(
                    f'the user-defined type {param_type} is not in scope',
                    environment.filename,
                    self.meta
                )

            params_invalid += [is_invalid_type(param_type)]
            parameter_list.append(NameTypePair(param.name, param_type))

        # RULE 2
        return_invalid = is_invalid_type(self.return_type)

        # Get ObjectType if UDT
        return_type = self.return_type
        if isinstance(self.return_type, UserDefinedType):
            return_type = self.return_type.get_object_type(environment)

        # If UDT invalid, log error
        if not return_type:
            return log_type_error(
                f'the user-defined type {return_type} is not in scope',
                environment.filename,
                self.meta
            )

        # Add function to environment
        environment[self.name] = FunctionType(
            [p.type for p in parameter_list],
            return_type
        )

        # (Valid)Type iff all children are valid
        types_invalid = params_invalid + [return_invalid]
        return InvalidType() if any(types_invalid) else Type()

    def codegen(self, indentation_level: int = 0) -> str:
        """Return Python3 function signature."""
        indentation = indent(indentation_level)

        # Get parameters code
        params = ', '.join([p.name for p in self.parameter_list])

        return f'{indentation}def {self.name}({params})'
