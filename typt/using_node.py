"""using_node.py - holds the AST node for the using rule."""

from typt.node import Node

from typt.typt_types import log_type_error
from typt.typt_types import Environment, Type, InvalidType

from importlib.util import find_spec


class UsingNode(Node):
    """Using AST node.

    Attributes:
        function_signature_list (List[FuncSignatureNode])   : Signatures list
        library_name            (str)                       : The library name
        library_alias           (str)                       : The library alias

    """

    def __init__(self, library_name: str = '', library_alias: str = ''):
        """Initialise using_list and stmt_list."""
        self.function_signature_list = list()
        self.library_name = library_name
        self.library_alias = library_alias

        super().__init__()

    def check_type(self, environment: Environment) -> Type:
        """Check type for this using statement (and add to the environment)."""
        # RULE Using statement invalid if library does not exist
        # RULE Using statement invalid if the function does not exist
        # RULE Using statement invalid if the arguments or return functions
        #       are not base types

        # Check RULE 1
        if not find_spec(self.library_name):
            log_type_error(
                'library {} does not exist'.format(self.library_name),
                environment.filename,
                self.meta
            )
            return InvalidType()

        # Check RULE 2
        any_invalid = False
        for f in self.function_signature_list:
            if not find_spec(f.name, package=self.library_name):
                log_type_error(
                    'function {} does not exist in library {}'.format(
                        f.name,
                        self.library_name
                    ),
                    environment.filename,
                    self.meta
                )
                any_invalid = True

        if any_invalid:
            return InvalidType()

        # TODO Check RULE 3

        # All rules passed
        return Type()
