"""atom_expr_node.py - holds AST node for atom expressions."""

from typt.test_node import TestNode
from typt.test.atom_node import AtomNode

from typt.argument_list_node import ArgumentListNode
from typt.subscript_node import SubscriptNode

from typing import Union, List


TrailerType = Union[ArgumentListNode, SubscriptNode, str]
TrailerType.__doc__ = """The Union of allowed trailer types."""


class AtomExprNode(TestNode):
    """AtomExprNode AST node.

    A trailer is either an argument_list, a subscript_list, or a (.) name.

    """

    def __init__(self, atom: AtomNode):
        """Set atom and initial (empty) trailer_list."""
        self.atom = atom                # type: AtomNode
        self.trailer_list = list()      # type: List[TrailerType]
