"""listener.py - provides the custom listener for Typt."""

from antlr.TyptParser import TyptParser
from antlr.TyptVisitor import TyptVisitor

from typt.node import Node
from typt.program_node import ProgramNode


class Typt(TyptVisitor):
    """Provide custom Typt listener."""

    def __init__(self):
        """Initialise custom visitor."""
        self.program = None

        super().__init__()

    def visitProgram(self, ctx: TyptParser.ProgramContext):
        """Visit `program' rule.

        Args:
            ctx (ProgramContext) : The program context

        Get the child using-declarations and statements.

        program => using* stmt* EOF

        """

        self.program = ProgramNode()

        # Add using-declarations to program
        for using_ctx in ctx.using():
            using = self.visitUsing(using_ctx)
            self.program.using_list += [using]

        # Add stmts to program
        for stmt_ctx in ctx.stmt():
            stmt = self.visitStmt(stmt_ctx)

        return self.program
    
    def visitStmt(self, ctx: TyptParser.StmtContext):
        """Visit `stmt' rule."""
        return self.visitChildren(ctx)