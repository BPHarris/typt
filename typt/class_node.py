"""class_node.py - holds the AST node for the class related rules."""

from typt.node import Node

from typt.class_initialiser_node import ClassInitialiserNode
from typt.class_method_node import ClassMethodNode

from typt.suite_node import SuiteNode
from typt.var_dec_stmt_node import VarDecStmtNode
from typt.typt_types import NameSuperPair, NameTypePair, Type, InvalidType

from typt.codegen import indent
from typt.environment import Environment
from typt.typt_types import ObjectBaseType, ObjectType
from typt.typt_types import is_invalid_type, log_type_error

from typing import List


class ClassNode(Node):
    """ClassNode AST node."""

    def __init__(self, name_super_pair: NameSuperPair, init_params: List[NameTypePair] = None, init_suite: SuiteNode = None, *args, **kwargs):
        """Initialise statement list."""
        self.class_name = name_super_pair.name
        self.class_super_name = name_super_pair.super

        self.class_attributes = list()      # type: List[VarDecStmtNode]

        # Class initialiser
        # NOTE if no init_suite then no init (must at least have pass_stmt)
        self.class_initialiser = None
        if init_suite:
            self.class_initialiser = ClassInitialiserNode(
                init_params,
                init_suite
            )

        self.class_methods = list()         # type: List[ClassMethodNode]
        self.class_static_methods = None    # TODO Static methods

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Check class is defined in a valid mannor."""
        # RULE Class name is free in environment
        # RULE Super class exists in environment and is subtype of base Object
        # RULE Attributes are valid
        # RULE Initialiser is valid
        # RULE Methods are valid
        # RULE TODO Class methods are valid

        # RULE 1
        if environment.get(self.class_name):
            return log_type_error(
                f'name {self.class_name} is not free in {environment.scope}',
                environment.filename,
                self.meta
            )

        # RULE 2
        super_class = environment.get(self.class_super_name)
        if not super_class:
            return log_type_error(
                f'{self.class_super_name} does not exist in {environment.scope}',
                environment.filename,
                self.meta
            )
        if not super_class == ObjectBaseType():
            return log_type_error(
                f'{self.class_name} is of type {super_class}, not an object',
                environment.filename,
                self.meta
            )

        # Get class environment
        class_environment = environment.add_child_environment(
            'class', self.class_name
        )

        # Add class to environment
        environment[self.class_name] = ObjectType()

        # RULE 3
        attributes_invalid = list()
        for attribute in self.class_attributes:
            attributes_invalid += [
                is_invalid_type(attribute.check_type(class_environment))
            ]

        # RULE 4
        initialiser_invalid = True
        if self.class_initialiser:
            initialiser_invalid = is_invalid_type(
                self.class_initialiser.check_type(class_environment)
            )

        # RULE 5
        methods_invalid = list()
        for method in self.class_methods:
            methods_invalid += [
                is_invalid_type(method.check_type(class_environment))
            ]

        # (Valid)Type iff all children are valid
        children_invalid = attributes_invalid + methods_invalid
        children_invalid += [initialiser_invalid]
        return InvalidType() if any(children_invalid) else Type()

    def codegen(self, indentation_level: int = 0) -> str:
        """Return the Python3 equivalent to the class."""
        indentation = indent(indentation_level)

        # Get attributes
        attributes = '\n'.join(
            [a.codegen(indentation_level + 1) for a in self.class_attributes]
        )

        # Get initialiser
        initialiser = ''
        if self.class_initialiser:
            initialiser = self.class_initialiser.codegen(indentation_level + 1)

        # Get methods
        methods = '\n'.join(
            [m.codegen(indentation_level + 1) for m in self.class_methods]
        )

        class_code = f'{indentation}class {self.class_name}'
        if self.class_super_name:
            class_code += f'({self.class_super_name})'
        class_code += f':\n{attributes}\n{initialiser}\n{methods}\n'

        return class_code
