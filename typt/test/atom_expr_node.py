"""atom_expr_node.py - holds AST node for atom expressions."""

from typt.test_node import TestNode
from typt.test.atom_node import AtomNode


class AtomExprNode(TestNode):
    """AtomExprNode AST node.

    A trailer is either an argument_list, a subscript_list, or a (.) name.
    Thus, the type of trailer is:
        List[Union[ArgListNode, SubscriptListNode, str]]

    """

    def __init__(self, atom: AtomNode):
        """Set atom and initial (empty) trailer_list."""
        self.atom = atom
        self.trailer_list = list()
