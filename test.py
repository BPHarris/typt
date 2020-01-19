"""test.py - unit tests for Typt.py file."""

from unittest import TestCase, main

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from antlr.TyptLexer import TyptLexer
from antlr.TyptParser import TyptParser
from antlr.TyptListener import TyptListener

from io import StringIO
from contextlib import redirect_stdout

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
        self.input_stream = FileStream('tests/empty/empty.typt')

    def test_empty(self):
        """Test lexer on empty file."""
        lexer = TyptLexer(self.input_stream)
        stream = CommonTokenStream(lexer)
        parser = TyptParser(stream)

        ast = parser.program()

        # FIXME: stdout/err not redirected to buf correctly
        with StringIO() as buf, redirect_stdout(buf):
            ParseTreeWalker().walk(TyptListener(), ast)

        # self.assertEqual(buf.getvalue(), '')

    def tearDown(self):
        """Tear down method (run after all tests)."""
        del self.input_stream


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
