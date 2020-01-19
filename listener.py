"""listener.py - provides the custom listener for Typt."""

from antlr.TyptParser import TyptParser
from antlr.TyptListener import TyptListener


class Typt(TyptListener):
    """Provide custom Typt listener."""

    def enterProgram(self, ctx: TyptParser.ProgramContext) -> None:
        """Entry function for program rule."""
        pass
