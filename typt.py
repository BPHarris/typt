"""typt.py - compiler for the Typt language."""

from antlr4 import FileStream, CommonTokenStream

from antlr.TyptLexer import TyptLexer
from antlr.TyptParser import TyptParser

from typt.visitor import Typt
from typt.node import NodePrinter

from error import log_error

from sys import argv
from os.path import isfile

# See: https://tomassetti.me/antlr-mega-tutorial/
#   Sections:   19. Testing with Python (unittest stuffs)

# TODO Finish error listener
# TODO Add ANY rule to grammar? Section 33


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

    # Lex and parse the given program
    lexer = TyptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TyptParser(stream)

    # Parse the program
    tree = Typt().visit(parser.program())

    # Print parse tree
    # print(tree)
    NodePrinter(tree).print()

    # Type checking
    # TODO type checking

    # Codegen
    # TODO codegen


if __name__ == '__main__':
    argv.append('')
    main(argv[1])
