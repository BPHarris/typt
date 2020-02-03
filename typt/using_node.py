"""using_node.py - holds the AST node for the using rule."""

from typt.node import Node

from typt.environment import Environment
from typt.typt_types import Type, InvalidType, FunctionType, log_type_error

from importlib import import_module
from importlib.util import find_spec


class UsingNode(Node):
    """Using AST node.

    Attributes:
        function_signature_list (List[FuncSignatureNode])   : Signatures list
        library_name            (str)                       : The library name
        library_alias           (str)                       : The library alias

    """

    def __init__(self, name: str = '', alias: str = '', *args, **kwargs):
        """Initialise using_list and stmt_list."""
        self.function_signature_list = list()
        self.library_name = name
        self.library_alias = alias

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Check type for this using statement (and add to the environment)."""
        # RULE Using statement invalid if library does not exist
        # RULE Using statement invalid if the function does not exist
        # RULE Using alias must be free in the environment

        # Check RULE 1
        if not find_spec(self.library_name):
            return log_type_error(
                'library {} does not exist'.format(self.library_name),
                environment.filename,
                self.meta
            )

        # Check RULE 2
        any_invalid = False
        loaded_module = import_module(self.library_name)
        for f in self.function_signature_list:
            if not hasattr(loaded_module, f.name):
                # Log error if function not in library
                log_type_error(
                    'no member {} in {}'.format(f.name, self.library_name),
                    environment.filename,
                    f.meta
                )

                any_invalid = True
        if any_invalid:
            return InvalidType()

        # Check RULE 3
        if environment[self.library_alias]:
            return log_type_error(
                'alias {} is not free in {}'.format(
                    self.library_alias, environment.filename
                )
            )

        # All rules passed, add types to environment and return (Valid)Type
        for f in self.function_signature_list:
            environment[f.name] = FunctionType(
                [p.type for p in f.parameter_list],
                f.return_type
            )

        return Type()

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the Python3 equivalent to using decl."""
        imported = ', '.join([f.name for f in self.function_signature_list])

        return 'from {} import {}'.format(self.library_name, imported)
