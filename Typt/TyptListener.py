# Generated from .\Typt.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TyptParser import TyptParser
else:
    from TyptParser import TyptParser

# This class defines a complete listener for a parse tree produced by TyptParser.
class TyptListener(ParseTreeListener):

    # Enter a parse tree produced by TyptParser#program.
    def enterProgram(self, ctx:TyptParser.ProgramContext):
        pass

    # Exit a parse tree produced by TyptParser#program.
    def exitProgram(self, ctx:TyptParser.ProgramContext):
        pass


    # Enter a parse tree produced by TyptParser#stmt.
    def enterStmt(self, ctx:TyptParser.StmtContext):
        pass

    # Exit a parse tree produced by TyptParser#stmt.
    def exitStmt(self, ctx:TyptParser.StmtContext):
        pass


    # Enter a parse tree produced by TyptParser#simple_stmt.
    def enterSimple_stmt(self, ctx:TyptParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by TyptParser#simple_stmt.
    def exitSimple_stmt(self, ctx:TyptParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by TyptParser#compound_stmt.
    def enterCompound_stmt(self, ctx:TyptParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by TyptParser#compound_stmt.
    def exitCompound_stmt(self, ctx:TyptParser.Compound_stmtContext):
        pass


