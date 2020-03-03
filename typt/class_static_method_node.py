"""class_static_method_node.py - holds the AST node for a static method."""

from typt.class_method_node import ClassMethodNode

from typt.codegen import indent


class ClassStaticMethodNode(ClassMethodNode):
    """ClassMethodNode AST node.

    The same as a standard method, but check_type is called with a different
    environment.

    Codegen is the only difference (the @staticmethod decorator is added).

    """

    def codegen(self, indentation_level: int = 0) -> str:
        """Return Python3 equivalent code."""
        decorator = f'{indent(indentation_level)}@staticmethod\n'
        return decorator + super().codegen(indentation_level)
