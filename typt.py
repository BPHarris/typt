"""typt.py -- compiler for the Typt language.

Usage: typt.py [[-vaer] FILE | [-h] | [--version]] [--output=<OUTPUT>]

-h, --help              show this
-v, --verbose           display verbose output (i.e. show AST, environment, etc.)
-a, --show-ast          show the program AST
-e, --show-environment  show the program environment after compilation
-r, --run               run the program after compiling
--version               print the program version
--output=<OUTPUT>       the file to output the compiled code to [default: output.py]

"""

from antlr4 import FileStream, CommonTokenStream

from antlr.TyptLexer import TyptLexer
from antlr.TyptParser import TyptParser

from typt.visitor import Typt, SourceGetter
from typt.node import NodePrinter
from typt.environment import get_initial_environment, json_encode_environment
from typt.typt_types import is_invalid_type

from error import log_critical_error
from json import dumps as json_dumps
from os.path import isfile

from os import system as execute
from platform import system

from docopt import docopt

# TODO Finish error listener
# See: https://tomassetti.me/antlr-mega-tutorial/
#   Sections:   19. Testing with Python (unittest stuffs)

runnable_systems = ('Linux', 'Darwin', 'Windows')


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
            log_critical_error(msg='operation cancelled.')
            exit()

    # Check if system supports --run
    if arguments['--run'] and not system() in runnable_systems:
        log_critical_error(msg=f'run option not supported on {system()}')
        quit()

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
    if arguments['--show-ast'] or arguments['--verbose']:
        NodePrinter(program).print()

    # Type checking
    environment = get_initial_environment(arguments['FILE'])
    program_type = program.check_type(environment)
    if is_invalid_type(program_type):
        quit()

    # Codegen
    output_code = program.codegen()

    if arguments['--show-environment'] or arguments['--verbose']:
        print(json_dumps(environment, indent=4, default=json_encode_environment))

    with open(arguments['--output'], 'w') as file:
        file.write(output_code)

    if arguments['--run']:
        interpreter = 'python' if system() == 'Windows' else 'python3'
        execute(f'{interpreter} {arguments["--output"]}')


if __name__ == '__main__':
    main(docopt(__doc__, version='Typt 0.0.1a'))
