"""error.py - handle errors in the Typt language, contains ErrorListener."""

from antlr4.error.ErrorListener import ErrorListener

from io import StringIO

class TyptErrorListener(ErrorListener):
    """Custom ErrorListener for Typt.

    Args:
        output  (StringIO)  : The StringIO for the given error listener

    Attributes:
        output  (StringIO)  : Object/stream to write errors to.
    """

    def __init__(self, output: StringIO):
        self.output = output        
        self._symbol = ''
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):        
        self.output.write(msg)
        self._symbol = offendingSymbol.text

    @property        
    def symbol(self) -> str:
        return self._symbol

    def __repr__(self) -> str:
        """Return string representation of the error lister."""
        return output.getvalue()
