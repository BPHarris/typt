"""error.py - handle errors in the Typt language, contains ErrorListener."""

from antlr4.error.ErrorListener import ErrorListener

from io import StringIO


def log_error(filename: str = None, line: int = None, msg: str = None) -> None:
    """Log an error to terminal."""
    prefix = '\x1b[31mtypt\x1b[0m: '

    # Add filename and line number to prefix, if present
    if filename:
        prefix += filename

        if line:
            prefix += ':' + line

        prefix += ': '

    print(prefix, msg, sep='')


def log_critical_error(msg: str = '', *args, **kwargs) -> None:
    """Log a critical error in white text with ared background."""
    log_error(msg='\x1b[1;37;41m' + msg + '\x1b[0m', *args, **kwargs)


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
