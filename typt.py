"""Typt.py - Compiler for Typt language."""

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from Typt.TyptLexer import TyptLexer
from Typt.TyptParser import TyptParser
from Typt.TyptListener import TyptListener

from sys import argv
from os.path import isfile


class Typt(TyptListener):
    """Provide custom Typt listener."""

    def enterProgram(self, ctx: TyptParser.ProgramContext) -> None:
        """Entry function for program rule."""
        pass


def log_error(filename: str = None, line: int = None, msg: str = None) -> None:
    """Log an error to terminal."""
    prefix = 'Typt: '

    if filename:
        prefix += filename

        if line:
            prefix += ':' + line

        prefix += ': '

    print(prefix + msg)


def main(filename: str = None) -> None:
    """Provide entry point."""
    if not filename:
        log_error(msg='No file provided.')
        quit()

    if not isfile(filename):
        log_error(msg='Provided file does not exist.')
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

