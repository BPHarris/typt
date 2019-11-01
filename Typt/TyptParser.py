# Generated from .\Typt.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,")
        buf.write("(\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\7\2\r\n\2\f")
        buf.write("\2\16\2\20\13\2\3\2\3\2\3\3\3\3\5\3\26\n\3\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\6\5 \n\5\r\5\16\5!\3\5\3\5\3\5\3")
        buf.write("\5\3\5\2\2\6\2\4\6\b\2\2\2\'\2\16\3\2\2\2\4\25\3\2\2\2")
        buf.write("\6\27\3\2\2\2\b\33\3\2\2\2\n\r\7*\2\2\13\r\5\4\3\2\f\n")
        buf.write("\3\2\2\2\f\13\3\2\2\2\r\20\3\2\2\2\16\f\3\2\2\2\16\17")
        buf.write("\3\2\2\2\17\21\3\2\2\2\20\16\3\2\2\2\21\22\7\2\2\3\22")
        buf.write("\3\3\2\2\2\23\26\5\6\4\2\24\26\5\b\5\2\25\23\3\2\2\2\25")
        buf.write("\24\3\2\2\2\26\5\3\2\2\2\27\30\7\3\2\2\30\31\7\7\2\2\31")
        buf.write("\32\7\4\2\2\32\7\3\2\2\2\33\34\7\5\2\2\34\35\7*\2\2\35")
        buf.write("\37\7+\2\2\36 \7\b\2\2\37\36\3\2\2\2 !\3\2\2\2!\37\3\2")
        buf.write("\2\2!\"\3\2\2\2\"#\3\2\2\2#$\7,\2\2$%\3\2\2\2%&\7\6\2")
        buf.write("\2&\t\3\2\2\2\6\f\16\25!")
        return buf.getvalue()


class TyptParser ( Parser ):

    grammarFileName = "Typt.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'['", "']'", "'def'", "'return'", 
                     "'raise'", "'from'", "'import'", "'as'", "'global'", 
                     "'nonlocal'", "'assert'", "'if'", "'elif'", "'else'", 
                     "'while'", "'for'", "'in'", "'try'", "'finally'", "'with'", 
                     "'except'", "'lambda'", "'or'", "'and'", "'not'", "'is'", 
                     "'None'", "'True'", "'False'", "'class'", "'yield'", 
                     "'del'", "'pass'", "'continue'", "'break'", "'async'", 
                     "'await'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "DEF", "RETURN", "RAISE", "FROM", "IMPORT", 
                      "AS", "GLOBAL", "NONLOCAL", "ASSERT", "IF", "ELIF", 
                      "ELSE", "WHILE", "FOR", "IN", "TRY", "FINALLY", "WITH", 
                      "EXCEPT", "LAMBDA", "OR", "AND", "NOT", "IS", "NONE", 
                      "TRUE", "FALSE", "CLASS", "YIELD", "DEL", "PASS", 
                      "CONTINUE", "BREAK", "ASYNC", "AWAIT", "NEWLINE", 
                      "INDENT", "DEDENT" ]

    RULE_program = 0
    RULE_stmt = 1
    RULE_simple_stmt = 2
    RULE_compound_stmt = 3

    ruleNames =  [ "program", "stmt", "simple_stmt", "compound_stmt" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    DEF=5
    RETURN=6
    RAISE=7
    FROM=8
    IMPORT=9
    AS=10
    GLOBAL=11
    NONLOCAL=12
    ASSERT=13
    IF=14
    ELIF=15
    ELSE=16
    WHILE=17
    FOR=18
    IN=19
    TRY=20
    FINALLY=21
    WITH=22
    EXCEPT=23
    LAMBDA=24
    OR=25
    AND=26
    NOT=27
    IS=28
    NONE=29
    TRUE=30
    FALSE=31
    CLASS=32
    YIELD=33
    DEL=34
    PASS=35
    CONTINUE=36
    BREAK=37
    ASYNC=38
    AWAIT=39
    NEWLINE=40
    INDENT=41
    DEDENT=42

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TyptParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(TyptParser.NEWLINE)
            else:
                return self.getToken(TyptParser.NEWLINE, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyptParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyptParser.StmtContext,i)


        def getRuleIndex(self):
            return TyptParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = TyptParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyptParser.T__0) | (1 << TyptParser.T__2) | (1 << TyptParser.NEWLINE))) != 0):
                self.state = 10
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [TyptParser.NEWLINE]:
                    self.state = 8
                    self.match(TyptParser.NEWLINE)
                    pass
                elif token in [TyptParser.T__0, TyptParser.T__2]:
                    self.state = 9
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 15
            self.match(TyptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stmt(self):
            return self.getTypedRuleContext(TyptParser.Simple_stmtContext,0)


        def compound_stmt(self):
            return self.getTypedRuleContext(TyptParser.Compound_stmtContext,0)


        def getRuleIndex(self):
            return TyptParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = TyptParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyptParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.simple_stmt()
                pass
            elif token in [TyptParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.compound_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(TyptParser.DEF, 0)

        def getRuleIndex(self):
            return TyptParser.RULE_simple_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_stmt" ):
                listener.enterSimple_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_stmt" ):
                listener.exitSimple_stmt(self)




    def simple_stmt(self):

        localctx = TyptParser.Simple_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_simple_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(TyptParser.T__0)
            self.state = 22
            self.match(TyptParser.DEF)
            self.state = 23
            self.match(TyptParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(TyptParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(TyptParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(TyptParser.DEDENT, 0)

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(TyptParser.RETURN)
            else:
                return self.getToken(TyptParser.RETURN, i)

        def getRuleIndex(self):
            return TyptParser.RULE_compound_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_stmt" ):
                listener.enterCompound_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_stmt" ):
                listener.exitCompound_stmt(self)




    def compound_stmt(self):

        localctx = TyptParser.Compound_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_compound_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(TyptParser.T__2)

            self.state = 26
            self.match(TyptParser.NEWLINE)
            self.state = 27
            self.match(TyptParser.INDENT)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.match(TyptParser.RETURN)
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==TyptParser.RETURN):
                    break

            self.state = 33
            self.match(TyptParser.DEDENT)
            self.state = 35
            self.match(TyptParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





