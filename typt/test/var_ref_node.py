"""var_ref_node.py - holds the variable reference AST node."""

from typt.test.atom_node import AtomNode

from typt.typt_types import Type, log_type_error
from typt.environment import Environment


class VarRefNode(AtomNode):
    """VarRefNode AST node."""

    def __init__(self, var_name: str, *args, **kwargs):
        """Set the variable name (var_name)."""
        self.var_name = var_name

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Return the type of the variable being referenced."""
        # Special case for self
        if self.var_name == 'self':
            # Get class environemnt
            while environment.scope != 'class':
                if not environment.parent:
                    log_type_error(
                        'self outside class', environment.filename, self.meta
                    )
                environment = environment.parent
            # Get class type
            class_name = environment.name[1:]   # HACK remove ':' from name
            return environment.parent[class_name]

        # Standard var reference
        var_type = environment.get(self.var_name)

        if not var_type:
            return log_type_error(
                f'name {self.var_name} does not exist in current scope',
                environment.filename,
                self.meta
            )

        return var_type

    def codegen(self, indentation_level: int = 0) -> str:
        """Return code of the variable refence, in Python3 form."""
        return f'{self.var_name}'
