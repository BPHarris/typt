"""func_signature_node.py - holds the AST node for the func_signature rule."""

from typt.node import Node

from typt.codegen import indent
from typt.environment import Environment
from typt.typt_types import is_invalid_type
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
        for param in self.parameter_list:
            params_invalid += [is_invalid_type(param.type)]

        # RULE 2
        return_invalid = is_invalid_type(self.return_type)

        # Add function to environment
        environment[f.name] = FunctionType(
            [p.type for p in self.parameter_list],
            self.return_type
        )

        # (Valid)Type iff all children are valid
        types_invalid = params_invalid + [return_invalid]
        return InvalidType() if any(types_invalid) else Type()

    def codegen(self, indentation_level: int = 0) -> str:
        """Return Python3 function signature."""
        pass
