"""atom_expr_node.py - holds AST node for atom expressions."""

from typt.test_node import TestNode
from typt.test.atom_node import AtomNode

from typt.argument_list_node import ArgumentListNode
from typt.subscript_node import SubscriptNode

from typt.codegen import indent
from typt.environment import Environment
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
        # TODO this
        # RULE Check atom type
        atom_type = self.atom.check_type(environment)
        if is_invalid_type(atom_type):
            return InvalidType()

        # RULE When no trailers, resultant type is the type of atom
        if not self.trailer_list:
            return atom_type

        # A) lhs.trailer
        # RULE lhs must have an environment
        # RULE trailer must exist in lhs
        # RULE resultant type is the type of trailer in environment(lhs)

        # B) lhs[trailer]
        # RULE lhs must be list/tuple/dict
        # RULE if lhs is list/tuple, trailer must be int
        # RULE if atim is dict[A -> B], trailer must be of type A

        # C) lhs(trailer)
        # RULE lhs must be function or method of class
        # RULE trailer must match the function signature
        # RULE resultant type is the return type of lhs in environment

        # Check the above rules for each trailer
        lhs = atom_type
        # TODO How to do this, ONLY know the type of lhs in each iter
        # for trailer in self.trailer_list:
        #     # A) lhs.trailer
        #     if isinstance(trailer, str):
        #         lhs_source = lhs.codegen()
        #         lhs_environment = environment.get(':' + lhs_source)

        #         # RULE A.1
        #         if not lhs_environment:
        #             return log_type_error(
        #                 f'lhs is not defined in current scope',
        #                 environment.filename,
        #                 self.meta
        #             )

        #         # RULE A.2
        #         if not environment.get(lhs_source + '.' + trailer):
        #             return log_type_error(
        #                 f'lhs has no member {trailer}',
        #                 environment.filename,
        #                 self.meta
        #             )

        #         # RULE A.3

        #     # B) lhs[trailer]
        #     if isinstance(trailer, SubscriptNode):
        #         pass

        #     # C) lhs(trailer)
        #     if isinstance(trailer, ArgumentListNode):
        #         pass

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
