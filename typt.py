"""typt.py - compiler for the Typt language.

Usage: typt.py [[-v] FILE | [-h] | [--version]] [--output=<OUTPUT>]

-h, --help          show this
-v, --verbose       display verbose output (i.e. print AST, etc.)
--version           print the program version
--output=<OUTPUT>   the file to output the compile code to [default: output.py]

"""

from antlr4 import FileStream, CommonTokenStream

from antlr.TyptLexer import TyptLexer
from antlr.TyptParser import TyptParser

from typt.visitor import Typt, SourceGetter
from typt.node import NodePrinter
from typt.environment import Environment, get_initial_environment
from typt.typt_types import is_invalid_type

from error import log_error, log_critical_error

from os.path import isfile

from docopt import docopt

# See: https://tomassetti.me/antlr-mega-tutorial/
#   Sections:   19. Testing with Python (unittest stuffs)

# TODO Finish error listener
# TODO Add ANY rule to grammar? Section 33


def main(arguments: dict = None) -> None:
    """Provide entry point."""
    if not arguments['FILE']:
        log_critical_error(msg='no file provided')
        quit()

    if not isfile(arguments['FILE']):
        log_critical_error(msg='provided file does not exist')
        quit()

    if isfile(arguments['--output']):
        confirm_overwrite = input(
            f'{arguments["--output"]} already exists, overwrite (y/N)? '
        )

        if not confirm_overwrite.lower() in ('y', 'yes'):
            print('Operation cancelled.')
            exit()

    # Get file input stream
    if arguments['--verbose']:
        print(f'typt: processing file {arguments.get("FILE")}:\n')
    input_stream = FileStream(arguments['FILE'])

    # Lex and parse the given program
    lexer = TyptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TyptParser(stream)

    # Initialise SourceGetter
    with open(arguments['FILE'], 'r') as source_file:
        SourceGetter.source_code = source_file.readlines()

    # Parse the program
    program = Typt().visit(parser.program())
    if arguments['--verbose']:
        NodePrinter(program).print()

    # Type checking
    program_type = program.check_type(
        get_initial_environment(arguments['FILE'])
    )
    if is_invalid_type(program_type):
        log_critical_error('critcal type error occurred', arguments['FILE'])

    # Codegen
    if arguments['--verbose']:
        print('\nBegining codegen.\n')
    output_code = program.codegen()

    with open(arguments['--output'], 'w') as file:
        file.write(output_code)


if __name__ == '__main__':
    main(docopt(__doc__, version='Typt 0.0.1a'))
