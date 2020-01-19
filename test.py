"""test.py - unit tests for Typt.py file."""

from unittest import TestCase, main

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from Typt.TyptLexer import TyptLexer
from Typt.TyptParser import TyptParser
from Typt.TyptListener import TyptListener

from io import StringIO
from contextlib import redirect_stdout, redirect_stderr


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

        # TODO: Fix this. stdout/err not redirected to buf correctly
        buf = StringIO()
        with redirect_stderr(buf), redirect_stdout(buf):
            ParseTreeWalker().walk(TyptListener(), ast)

        self.assertEqual(buf.getvalue(), '')

    def tearDown(self):
        """Tear down method (run after all tests)."""
        del self.input_stream


if __name__ == '__main__':
    main()
