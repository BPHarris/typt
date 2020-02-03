"""environment.py -- holds the Environment class for Typt."""

from typing import Dict, Union

from typt.typt_types import Type


class Environment:
    """A Typt environment, stores the the current scope.

    Each named element of the environment is either a sub envionment or a Type.

    Format:
        dict['name']     = Type of name
        dict['a.b.c']    = Type of c in b in a
        dict['env:name'] = The environment local to the identifier 'name'

    """

    def __init__(self, parent=None, filename: str = ''):
        """Create the empty environment."""
        self.parent = parent
        self.filename = filename
        self.environment = dict()   # type: Dict[str, Union[Environment, Type]]
