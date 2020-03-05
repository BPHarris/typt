"""atom_expr_node.py - holds AST node for atom expressions."""

from typt.test_node import TestNode
from typt.test.atom_node import AtomNode

from typt.argument_list_node import ArgumentListNode
from typt.subscript_node import SubscriptNode

from typt.codegen import indent
from typt.environment import Environment
from typt.typt_types import ObjectBaseType, ObjectType, FunctionType
from typt.typt_types import Type, InvalidType, is_invalid_type, log_type_error

from typing import Union, List


TrailerType = Union[ArgumentListNode, SubscriptNode, str]
TrailerType.__doc__ = """The Union of allowed trailer types."""


class AtomExprNode(TestNode):
    """AtomExprNode AST node.

    A trailer is either an argument_list, a subscript_list, or a (.) name.

    """

    def __init__(self, atom: AtomNode, *args, **kwargs):
        """Set atom and initial (empty) trailer_list."""
        self.atom = atom                # type: AtomNode
        self.trailer_list = list()      # type: List[TrailerType]

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Check the type of an atom expression."""
        atom_type = self.atom.check_type(environment)
        if is_invalid_type(atom_type):
            return InvalidType()

        if not self.trailer_list:
            return atom_type

        # RULE lhs.trailer, lhs has member trailer s.t. member : T => T
        # RULE lhs[trailer], delegate to Subscript node
        # RULE lhs(trailer), lhs : Object => Object.__init__(trailer)
        # RULE lhs(trailer), lhs : Function => lhs(trailer)

        lhs_type = atom_type
        for trailer in self.trailer_list:
            # lhs.trailer
            if isinstance(trailer, str):
                if not lhs_type == ObjectType():
                    return log_type_error(
                        f'{lhs_type} has no member {trailer}',
                        environment.filename,
                        self.meta
                    )

                # Get member
                member_type = lhs_type.get(trailer)
                if not member_type:
                    return log_type_error(
                        f'{lhs_type} has no member {trailer}',
                        environment.filename,
                        self.meta
                    )

                # Set new lhs to member
                lhs_type = member_type

            # lhs[trailer]
            if isinstance(trailer, SubscriptNode):
                _environment = environment.add_local_environment('subscript')
                _environment['parent_type'] = lhs_type

                # Delegate to SubscriptNode
                element_type = trailer.check_type(_environment)

                if is_invalid_type(element_type):
                    return InvalidType()

                # Set new lhs to the element type
                lhs_type = element_type

            # lhs(trailer)
            if isinstance(trailer, ArgumentListNode):
                # lhs is object => type check with init => lhs_type' = lhs_type
                if lhs_type == ObjectType():
                    initialiser = lhs_type.get('__init__')

                    if not initialiser:
                        return log_type_error(
                            f'object has no initialiser',
                            environment.filename,
                            self.meta
                        )

                    # Check arguments against initialiser
                    if len(trailer.argument_list) != len(initialiser.parameters):
                        return log_type_error(
                            f'incorrect number of arguments for initialiser',
                            environment.filename,
                            self.meta
                        )

                    # Check argument types
                    arguments = zip(trailer.argument_list, initialiser.parameters)
                    for i, (received, expected_type) in enumerate(arguments):
                        received_type = received.check_type(environment)

                        if not received_type == expected_type:
                            return log_type_error(
                                f'argument {i} expected value of type '
                                f'{expected_type}, received {received_type}',
                                environment.filename,
                                self.meta
                            )

                    # lhs remains the same
                    lhs_type = lhs_type

                # lhs is function => type check => lhs_type' = return_type
                if isinstance(lhs_type, FunctionType):
                    if len(trailer.argument_list) != len(lhs_type.parameters):
                        return log_type_error(
                            f'incorrect number of arguments for function {lhs_type}',
                            environment.filename,
                            self.meta
                        )

                    # Check argument types
                    arguments = zip(trailer.argument_list, lhs_type.parameters)
                    for i, (received, expected_type) in enumerate(arguments):
                        received_type = received.check_type(environment)

                        if not received_type == expected_type:
                            return log_type_error(
                                f'argument {i} expected value of type '
                                f'{expected_type}, received {received_type}',
                                environment.filename,
                                self.meta
                            )

                    # All argument types are correct, lhs_type' = return_type
                    lhs_type = lhs_type.return_type

        # Return the final value of of lhs_type
        return lhs_type

    def codegen(self, indentation_level: int = 0) -> str:
        """Codegen for the atom expression."""
        indentation = indent(indentation_level)

        output = f'{indentation}{self.atom.codegen()}'

        for trailer in self.trailer_list:
            # atom.trailer
            if isinstance(trailer, str):
                output += f'.{trailer}'

            # atom[trailer]
            if isinstance(trailer, SubscriptNode):
                output += f'[{trailer.codegen()}]'

            # atom(trailer)
            if isinstance(trailer, ArgumentListNode):
                output += f'({trailer.codegen()})'

        return output
