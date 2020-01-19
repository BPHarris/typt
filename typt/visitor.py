"""listener.py - provides the custom listener for Typt."""

from antlr.TyptParser import TyptParser
from antlr.TyptVisitor import TyptVisitor

import typt.node


class Typt(TyptVisitor):
    """Provide custom Typt listener."""

    def __init__(self):
        """Initialise custom visitor."""
        self.program = None

        super().__init__()

    def visitProgram(self, ctx: TyptParser.ProgramContext):
        """Visit `program' rule."""
        print('porgram')
        return self.visitChildren(ctx)
    
    def visitStmt(self, ctx: TyptParser.StmtContext):
        """Visit `stmt' rule."""
        print('stmt')
        return self.visitChildren(ctx)