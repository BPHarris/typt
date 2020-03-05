"""subscript_node.py - holds the AST subscript node."""

from typt.node import Node
from typt.test_node import TestNode

from typt.typt_types import Type, ListType, TupleType, DictType, StringType
from typt.typt_types import log_type_error, is_invalid_type, is_int, IntType
from typt.environment import Environment

from typing import Union


NoneOrTestNode = Union[None, TestNode]
NoneOrTestNode.__doc__ = """Union of (None, TestNode) for subscript args."""


class SubscriptNode(Node):
    """SubscriptNode AST node."""

    def __init__(self, index: NoneOrTestNode, *args, **kwargs):
        """Set default values."""
        self.index = index
        # self.upto = upto
        # self.step = step

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Check the type of the result of the subscript operation.

        Assumes the lowest level of environment is a sub environment of:
            - scope 'subscript'
            - has (only) members 'parent_type'
        """
        # RULE Index must be valid
        # RULE Subscript must occur in the scope that it is expected
        # RULE Parent type must be List, Tuple, Dict, String
        # RULE For parent ListType<T>, Index : IntType, result is T
        # RULE For parent TupleType<T_i for 0..n>, Index: IntType,
        #       0 <= Index <= n, result is T_m where m = Index
        # RULE For parent DictType<K, V>, Index : K, result is V
        # RULE For parent String, Index : Int, result is String

        # Check RULE 1
        index_type = self.index.check_type(environment)
        if is_invalid_type(index_type):
            return log_type_error(
                'index of invalid type', environment.filename, self.meta
            )

        # Check RULE 2
        if environment.scope != 'subscript':
            return log_type_error(
                'illegal scope for subscript operation',
                environment.filename,
                self.meta
            )

        parent_type = environment['parent_type']

        # Check RULE 4 -- ListType<T>, Index : IntType => T
        if isinstance(parent_type, ListType):
            if not isinstance(index_type, IntType):
                return log_type_error(
                    'list index must be int', environment.filename, self.meta
                )
            return parent_type.element_type

        # Check RULE 5 -- TupleType<T_0..T_n>, Index : IntType, 0 <= Index <= n
        #                   => T_m where m = Index
        if isinstance(parent_type, TupleType):
            index_codegen = self.index.codegen()

            # Must know Index value at run-time, but be an int
            if not is_int(index_codegen):
                return log_type_error(
                    'tuple index must be int literal',
                    environment.filename,
                    self.meta
                )

            # Check range of Index
            index = int(index_codegen)
            if index < 0 or index > len(parent_type.element_type_list):
                return log_type_error(
                    f'tuple index {index} out-of-range',
                    environment.filename,
                    self.meta
                )

            return parent_type.element_type_list[index]

        # Check RULE 6 -- DictType<K, V>, Index : K => V
        if isinstance(parent_type, DictType):
            key_type = parent_type.key_type
            if not isinstance(index_type, key_type):
                return log_type_error(
                    f'dict expecting {key_type} index, found {index_type}',
                    environment.filename,
                    self.meta
                )
            return parent_type.value_type

        # Checl RULE 7 -- String, Index : Int => String
        if isinstance(parent_type, StringType):
            if not isinstance(index_type, IntType):
                return log_type_error(
                    'string index must be int', environment.filename, self.meta
                )
            return StringType()

        # Check RULE 3
        return log_type_error(
            f'cannot perform subscript on {parent_type}',
            environment.filename,
            self.meta
        )

    def codegen(self, indentation_level: int = 0) -> str:
        """Return Python3 representation of subscipt."""
        return f'{self.index.codegen()}'
