"""test.py - unit tests for Typt.py file."""

from unittest import TestCase, main

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from Typt.TyptLexer import TyptLexer
from Typt.TyptParser import TyptParser
from Typt.TyptListener import TyptListener


class TestFileHandling(TestCase):
    """Class for file handling test cases."""

    pass


class TestEmpty(TestCase):
    """Class for the empty file tests."""

    def setUp(self):
        """Set up method (run before any tests)."""
        self.input_stream = FileStream('tests/empty/empty.typt')

    def test_empty_lexer(self):
        """Test lexer on empty file."""
        lexer = TyptLexer(self.input_stream)
        self.assertEqual(lexer.tokens, list())

    def test_empty_parser(self):
        """Test parser on empty file."""
        lexer = TyptLexer(self.input_stream)
        stream = CommonTokenStream(lexer)
        parser = TyptParser(stream)

        # TODO: What to assert?
        parser.program

    def test_empty_ast(self):
        """Test ast on empty file."""
        lexer = TyptLexer(self.input_stream)
        stream = CommonTokenStream(lexer)
        parser = TyptParser(stream)

        ast = parser.program()
        ptw = ParseTreeWalker().walk(TyptListener(), ast)

        # TODO: What to assert?
        ptw


if __name__ == '__main__':
    main()
