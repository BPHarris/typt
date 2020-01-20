"""test.py - unit tests for Typt.py file."""

from unittest import TestCase, main

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from antlr.TyptLexer import TyptLexer
from antlr.TyptParser import TyptParser

from error import TyptErrorListener

from io import StringIO

# Todo list:
#   TODO: TestCase for long_examples/
#   TODO: (finish) TestCase for regression_tests/
#   TODO: TestCase for lexer/
#   TODO: TestCase for parser/
#
#   TODO: Add preamble to *.typt test files


class TestFileHandling(TestCase):
    """Class for file handling test cases."""

    pass


class TestEmpty(TestCase):
    """Class for the empty file tests."""

    def setUp(self):
        """Set up method (run before any tests)."""
        self.output = StringIO()
        self.input_stream = FileStream('tests/empty/empty.typt')
        self.error_listener = TyptErrorListener(self.output)

    def test_empty(self):
        """Test lexer on empty file."""
        # TODO: Redo
        # lexer = TyptLexer(self.input_stream)
        # stream = CommonTokenStream(lexer)
        # parser = TyptParser(stream, self.error_listener)

        # Set error listener

        # ast = parser.program()

        # FIXME: stdout/err not redirected to buf correctly
        # See Section 19: https://tomassetti.me/antlr-mega-tutorial/
        # ParseTreeWalker().walk(TyptListener(), ast)

        # self.assertEqual(buf.getvalue(), '')

    def tearDown(self):
        """Tear down method (run after all tests)."""
        del self.output
        del self.input_stream
        del self.error_listener


class TestRegression(TestCase):
    """Class for running regression tests."""

    def setUp(self):
        """Set up method (run before any tests)."""
        pass

    def tearDown(self):
        """Tear down method (run after all tests)."""
        pass


if __name__ == '__main__':
    main()
