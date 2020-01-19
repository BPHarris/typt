"""Typt.py - Compiler for the Typt language."""

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from antlr.TyptLexer import TyptLexer
from antlr.TyptParser import TyptParser
from antlr.TyptListener import TyptListener

from sys import argv
from os.path import isfile

# See: https://tomassetti.me/antlr-mega-tutorial/
#   Sections:   19. Testing with Python (unittest stuffs)


class Typt(TyptListener):
    """Provide custom Typt listener."""

    def enterProgram(self, ctx: TyptParser.ProgramContext) -> None:
        """Entry function for program rule."""
        pass


def log_error(filename: str = None, line: int = None, msg: str = None) -> None:
    """Log an error to terminal."""
    prefix = 'typt: '

    if filename:
        prefix += filename

        if line:
            prefix += ':' + line

        prefix += ': '

    print(prefix + msg)


def main(filename: str = None) -> None:
    """Provide entry point."""
    if not filename:
        log_error(msg='no file provided')
        quit()

    if not isfile(filename):
        log_error(msg='provided file does not exist')
        quit()

    print('Processing file {}:\n'.format(filename))
    input_stream = FileStream(filename)

    lexer = TyptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TyptParser(stream)

    ast = parser.program()
    ParseTreeWalker().walk(Typt(), ast)


if __name__ == '__main__':
    argv.append('')
    main(argv[1])
