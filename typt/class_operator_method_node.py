"""class_operator_method_node.py -- AST node for an operator method."""

from typt.node import Node
from typt.suite_node import SuiteNode

from typt.codegen import indent
from typt.environment import Environment
from typt.typt_types import is_invalid_type, log_type_error
from typt.typt_types import Type, InvalidType, FunctionType, UserDefinedType

from typing import Tuple


"""Mapping of operator symbols to names"""
_operator_names = {
    '==': 'eq', '!=': 'neq',
    '>': 'gt', '<': 'lt', '>=': 'gte', '<=': 'lte',
    'in': 'in', 'not in': 'not_in', 'is': 'is', 'is not': 'is_not',
    '|': 'or', '^': 'xor', '&': 'and', '<<': 'lshift', '>>': 'rshift',
    '+': 'add', '-': 'sub', '*': 'mul',
    '/': 'div', '%': 'mod', '//': 'idiv'
}


def operator_method_name(operator: str, other_type: Type) -> str:
    """Return the name of the method that implements the given operator."""
    if operator not in _operator_names.keys():
        return None

    operator_name = _operator_names[operator]

    other_type_name = other_type.__class__.__name__
    if isinstance(other_type, UserDefinedType):
        other_type_name = other_type.name

    return f'_typt_{operator_name}_{other_type_name}'


def get_operator_method(operator: str, self_type: Type, other_type: Type, environment: Environment) -> Tuple[str, Type]:
    """Return (name, return type) for self_type's method for operator."""
    operator_method = operator_method_name(operator, other_type)

    # Check operator exists in self_type
    for method_name, method_type in self_type.members:
        if method_name == operator_method:
            if is_invalid_type(method_type):
                return method_name, method_type
            return method_name, method_type.return_type

    return None, InvalidType()


class ClassOperatorMethodNode(Node):
    """ClassOperatorMethodNode AST node."""

    def __init__(self, lhs_type: Type, operator: str, rhs_type: Type, resultant_type: Type, suite: SuiteNode, *args, **kwargs):
        """Set attributes."""
        self.lhs_type = lhs_type
        self.operator = operator
        self.rhs_type = rhs_type
        self.resultant_type = resultant_type

        self.suite = suite

        self.method_name = operator_method_name(operator, rhs_type)

        super().__init__(*args, **kwargs)

    def check_type(self, environment: Environment) -> Type:
        """Check method type is valid."""
        # RULE lhs must be correct already (due to grammar)
        # RULE rhs type must be valid
        # RULE resultant type must be valid
        # RULE Register in environment as class method
        #       with argument as rhs type and return type as resultant type
        # RULE suite must be valid

        # Check RULE -- Valid other_type/rhs_type
        rhs_type = self.rhs_type
        # TODO CHeck valid
        # if isinstance(rhs_type, UserDefinedType):
        #     rhs_type = rhs_type.get_object_type(environment)
        # if not rhs_type or is_invalid_type(rhs_type):
        #     return log_type_error(
        #         f'invalid other type, could be out-of-scope',
        #         environment.filename,
        #         self.meta
        #     )

        # Check resultant type is valid
        resultant_type = self.resultant_type
        # TODO CHeck valid
        # if isinstance(resultant_type, UserDefinedType):
        #     resultant_type = resultant_type.get_object_type(environment)
        # if not resultant_type or is_invalid_type(resultant_type):
        #     return log_type_error(
        #         f'invalid resultant type, could be out-of-scope',
        #         environment.filename,
        #         self.meta
        #     )

        # Register operator in environment
        operator_type = FunctionType([rhs_type], resultant_type)
        environment[self.method_name] = operator_type

        # Register class operator method environment
        operator_environment = environment.add_child_environment(
            'function', self.method_name)

        operator_environment['other'] = rhs_type

        # Check suite is valid
        if is_invalid_type(self.suite.check_type(operator_environment)):
            return InvalidType()

        return operator_type

    def codegen(self, indentation_level: int = 0) -> str:
        """Return Python3 equivalent code."""
        indentation = indent(indentation_level)

        func_signature_code = f'def {self.method_name}(self, other)'
        suite_code = self.suite.codegen(indentation_level)

        return f'{indentation}{func_signature_code}:{suite_code}'
