"""test.py - unit tests for Typt.py file."""

from unittest import TestCase, main

from error import TyptErrorListener

from io import StringIO

# Todo list:
#   TODO: Error listener
#   TODO: TestCase for long_examples/
#   TODO: TestCase for regression_tests/
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
        self.error_listener = TyptErrorListener(self.output)

    def test_empty(self):
        """Test lexer on empty file."""
        pass

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
