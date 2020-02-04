"""codegen.py -- stores util functions for codegen."""

# The string representing a single indent
_indent_str = '    '     # type: str


def indent(indentation_level: int) -> str:
    """Return the string representing the current indentation level."""
    return _indent_str * indentation_level
