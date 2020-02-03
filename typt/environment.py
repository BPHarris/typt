"""environment.py -- holds the Environment class for Typt."""

from re import compile
from typing import Dict, Union

from typt.typt_types import Type


class Environment:
    """A Typt environment, stores the the current scope.

    Each named element of the environment is either a sub envionment or a Type.

    Format:
        dict['name']    = Type of name
        dict['a.b.c']   = Type of c in b in a
        dict[':name']   = The environment local to the identifier 'name'

    """

    def __init__(self, parent=None, filename: str = ''):
        """Create the empty environment."""
        self.parent = parent        # type: Environment
        self.filename = filename
        self.environment = dict()   # type: Dict[str, Union[Environment, Type]]

    def __getitem__(self, key: str):
        """Override __getitem__ to implement the behaviour in the docstring."""
        name = compile('[a-zA-Z]')
        dotted_name = compile('[a-zA-Z.][a-zA-Z]')
        environment_name = compile(':[a-zA-Z]')

        if name.match(key):
            return self.environment.get(key, None)

        # If dotted name, a.b.c, check for b.c in environment ':a'
        if dotted_name.match(key):
            head, tail = key.split('.')[0], key.split('.')[1:]
            return self.environment.get(':' + head, None)[tail]

        if environment_name.match(key):
            return self.environment.get(key, None)

        raise KeyError('Invalid format for key {}.'.format(key))

    def __setitem__(self, key: str, value):
        """Set item delegates to self.environment."""
        self.environment[key] = value

    def get(self, key: str, default=None):
        """Get the value belonging to the given key."""
        result = self[key]

        # If there is a local instance, return it
        if result:
            return result

        # Otherwise, travel up the tree until one is located or hits root

        # If root, and key not local -- then key is free in Environment
        if not self.parent:
            return None

        return self.parent.get(key, default)

    def __repr__(self) -> str:
        """Return string representation of the dictionary."""
        contents_str = '\n'.join(
            ['\t' + repr(k) + ' : ' + repr(v) for k, v in self.environment.items()]
        )
        return self.filename + '\n' + contents_str
