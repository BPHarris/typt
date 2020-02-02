"""class_node.py - holds the AST node for the class related rules."""

from typt.node import Node

from typt.class_initialiser_node import ClassInitialiserNode
from typt.class_method_node import ClassMethodNode

from typt_types import NameSuperPair, NameTypePair
from typt.suite_node import SuiteNode
from typt.var_dec_stmt_node import VarDecStmtNode

from typing import List


class ClassNode(Node):
    """ClassNode AST node."""

    def __init__(self, name_super_pair: NameSuperPair, init_params: List[NameTypePair], init_suite: SuiteNode):
        """Initialise statement list."""
        self.class_name = name_super_pair.name
        self.class_super_name = name_super_pair.super

        self.class_attributes = list()      # type: List[VarDecStmtNode]
        self.class_initialiser = ClassInitialiserNode(init_params, init_suite)
        self.class_methods = list()         # type: List[ClassMethodNode]
        self.class_static_methods = None    # TODO Static methods

        super().__init__()