"""environment.py -- holds the Environment class for Typt."""

from re import compile
from typing import Dict, Union

from typt.typt_types import Type, ObjectBaseType, FunctionType, ListType
from typt.typt_types import NoneType, BoolType, IntType, FloatType, StringType


def get_initial_environment(filename: str):
    """Construct and return an initial environment."""
    environment = Environment(filename=filename, name='__main__')

    # Add ObjectBaseType to initial environment
    environment['Object'] = ObjectBaseType()

    # Add typt stdlib print functions
    environment['print_none'] = FunctionType((NoneType(),), NoneType())
    environment['print_bool'] = FunctionType((BoolType(),), NoneType())
    environment['print_int'] = FunctionType((IntType(),), NoneType())
    environment['print_float'] = FunctionType((FloatType(),), NoneType())
    environment['print_string'] = FunctionType((StringType(),), NoneType())
    environment['print'] = FunctionType((StringType(),), NoneType())

    # Add stdlib cast functions (*_to_bool)
    environment['none_to_bool'] = FunctionType((NoneType(),), BoolType())
    environment['bool_to_bool'] = FunctionType((BoolType(),), BoolType())
    environment['int_to_bool'] = FunctionType((IntType(),), BoolType())
    environment['float_to_bool'] = FunctionType((FloatType(),), BoolType())
    environment['string_to_bool'] = FunctionType((StringType(),), BoolType())

    # Add stdlib cast functions (*_to_int)
    environment['none_to_int'] = FunctionType((NoneType(),), IntType())
    environment['bool_to_int'] = FunctionType((BoolType(),), IntType())
    environment['int_to_int'] = FunctionType((IntType(),), IntType())
    environment['float_to_int'] = FunctionType((FloatType(),), IntType())
    environment['string_to_int'] = FunctionType((StringType(),), IntType())

    # Add stdlib cast functions (*_to_float)
    environment['none_to_float'] = FunctionType((NoneType(),), FloatType())
    environment['bool_to_float'] = FunctionType((BoolType(),), FloatType())
    environment['int_to_float'] = FunctionType((IntType(),), FloatType())
    environment['float_to_float'] = FunctionType((FloatType(),), FloatType())
    environment['string_to_float'] = FunctionType((StringType(),), FloatType())

    # Add stdlib cast functions (*_to_string)
    environment['none_to_string'] = FunctionType((NoneType(),), StringType())
    environment['bool_to_string'] = FunctionType((BoolType(),), StringType())
    environment['int_to_string'] = FunctionType((IntType(),), StringType())
    environment['float_to_string'] = FunctionType((FloatType(),), StringType())
    environment['string_to_string'] = FunctionType((StringType(),), StringType())

    # Add stdlib misc functions
    environment['range'] = FunctionType(
        (IntType(), IntType()), ListType(IntType())
    )

    return environment


class Environment:
    """A Typt environment, stores the the current scope.

    Each named element of the environment is either a sub envionment or a Type.

    Attributes:
        parent      (Environment) : the parent of this environment
        filename    (str)         : the file the environment belongs to
        scope       (str)         : the scope of the environment
            (file/__main__, class, method, function, for, while, if, subscript)
        name        (str)         : the identifier of the environment
            (for classes/functions this is the class/function name, otherwise
            it is generated and unimportant)

    Format:
        dict['name']    = Type of name
        dict['a.b.c']   = Type of c in b in a
        dict[':name']   = The environment local to the identifier 'name'

    """

    def __init__(self, parent=None, filename: str = '', scope: str = '__main__', name: str = ''):
        """Create the empty environment."""
        self.parent = parent        # type: Environment
        self.filename = filename    # type: str
        self.scope = scope          # type: str
        self.name = name            # type: str

        self.environment = dict()   # type: Dict[str, Union[Environment, Type]]

    def __getitem__(self, key: str):
        """Override __getitem__ to implement the behaviour in the docstring."""
        name_pattern = '[a-zA-Z0-9_]*'
        trailer_pattern = fr'(\.{name_pattern})*'
        prime_pattern = '[\']*'

        name = compile(name_pattern + prime_pattern)
        dotted_name = compile(name_pattern + trailer_pattern + prime_pattern)
        environment_name = compile(':' + name_pattern + trailer_pattern + prime_pattern)

        # If it is a simple name, get the name from the wrapped dictionary
        if name.match(key):
            return self.environment.get(key, None)

        # If dotted name, a.b.c, check for b.c in environment ':a'
        if dotted_name.match(key):
            balkanised = key.split('.')
            head, body, tail = balkanised[0], balkanised[1:-1], balkanised[-1]

            # Get the head environment
            # Use a get asthe head can can be in any legal scope
            environment = self.get(':' + head)
            if not environment:
                return None

            # Get each subsequent child environment
            # Use index as each body segment MUST be in previous segment/head
            for segment in body:
                environment = environment[':' + segment]
                if not environment:
                    return None

            # Get the tail inside the final environment
            # Use index as must be directly inside
            target = environment[tail]

            if not target:
                return None
            return target

        if environment_name.match(key):
            # If it is a simple environment, i.e. ':name' not ':name.name'
            # then return the environment
            if name.match(key[1:]):
                return self.environment.get(key, None)

            # Otherwise, it is a dotted environment name, handle as such
            balkanised = key.split('.')[1:]  # HACK Remove the preceeding ':'
            head, body, tail = balkanised[0], balkanised[1:-1], balkanised[-1]

            # Get the head environment, see dotted name handling
            environment = self.get(':' + head)
            if not environment:
                return None

            # Get each subsequent child environment, see dotted name handling
            for segment in body:
                environment = environment[':' + segment]
                if not environment:
                    return None

            # Get the tail environment
            # Use index as must be directly inside
            target_environment = environment[':' + tail]

            if not target_environment:
                return None
            return target_environment

        raise KeyError(f'Invalid format for key {key}')

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

    def in_scope(self, s: str) -> bool:
        """Return a Boolean representing if the environment is in the scope s.

        The environment is in scope if it's scope, or any of it's parents
        scopes are equal to s.

        """
        # BASE CASE: If is root, check scope and stop recursion
        if not self.parent:
            return self.scope == s

        # RECURSIVE CASE: Otherwise, check self; recurse if needed
        if self.scope is s:
            return True

        return self.parent.in_scope(s)

    def add_child(self, *args):
        """Depricated. Use add_child_environment or add_local_environment."""
        raise NotImplementedError(f'add_child: {self.add_child.__doc__}')

    def add_child_environment(self, scope: str, name: str):
        """Add and return a child environment with the given name and scope."""
        accepted_scopes = ('__main__', 'class', 'method', 'function')

        if scope not in accepted_scopes:
            raise ValueError(f'\'{scope}\' is invalid as a child environment.')

        # Name must be unique
        if self[':' + name]:
            raise ValueError(f'name {name} not unique in {self.name}.')

        self[':' + name] = Environment(self, self.filename, scope, name)
        return self[':' + name]

    def add_local_environment(self, scope: str):
        """Add a child environment for the given scope type."""
        accepted_local_scopes = (
            'for', 'while', 'if', 'elif', 'else', 'subscript'
        )

        if scope not in accepted_local_scopes:
            raise ValueError(f'\'{scope}\' is invalid as a local environment.')

        # Get the scopes name (unused later, but needed as unique ID)
        name = scope
        while self[':' + name]:
            name += '\''

        self[':' + name] = Environment(self, self.filename, scope, name)
        return self[':' + name]

    def __repr__(self) -> str:
        """Return string representation of the dictionary."""
        to_show = {
            'name': self.name,
            'scope': self.scope,
            'contents': self.environment
        }

        return f'Environment{{{to_show}}}'


def json_encode_environment(e) -> Dict:
    """Return a JSON-encodable dict representation of the given environment."""
    if isinstance(e, Environment):
        return {
            'name': e.name,
            'scope': e.scope,
            'contents': e.environment
        }
    elif isinstance(e, Type):
        return repr(e)
    else:
        raise TypeError(f'Can\'t encode {e.__class__.__name__}')
