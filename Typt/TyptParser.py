# Generated from .\Typt\Typt.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("C\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\7\2\23\n\2\f\2\16\2\26\13\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\"\n\3\3\4\3\4\3\4\7\4\'")
        buf.write("\n\4\f\4\16\4*\13\4\3\4\5\4-\n\4\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\6\79\n\7\r\7\16\7:\3\7\3\7\5\7?\n\7")
        buf.write("\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16\2\3\3\2\t\r\2B\2\24")
        buf.write("\3\2\2\2\4!\3\2\2\2\6#\3\2\2\2\b\60\3\2\2\2\n\62\3\2\2")
        buf.write("\2\f>\3\2\2\2\16@\3\2\2\2\20\23\7\21\2\2\21\23\5\4\3\2")
        buf.write("\22\20\3\2\2\2\22\21\3\2\2\2\23\26\3\2\2\2\24\22\3\2\2")
        buf.write("\2\24\25\3\2\2\2\25\27\3\2\2\2\26\24\3\2\2\2\27\30\7\2")
        buf.write("\2\3\30\3\3\2\2\2\31\32\7\3\2\2\32\33\7\16\2\2\33\34\7")
        buf.write("\4\2\2\34\"\7\21\2\2\35\36\7\5\2\2\36\37\7\6\2\2\37 \7")
        buf.write("\7\2\2 \"\5\f\7\2!\31\3\2\2\2!\35\3\2\2\2\"\5\3\2\2\2")
        buf.write("#(\5\b\5\2$%\7\b\2\2%\'\5\b\5\2&$\3\2\2\2\'*\3\2\2\2(")
        buf.write("&\3\2\2\2()\3\2\2\2),\3\2\2\2*(\3\2\2\2+-\7\b\2\2,+\3")
        buf.write("\2\2\2,-\3\2\2\2-.\3\2\2\2./\7\21\2\2/\7\3\2\2\2\60\61")
        buf.write("\5\n\6\2\61\t\3\2\2\2\62\63\3\2\2\2\63\13\3\2\2\2\64?")
        buf.write("\5\6\4\2\65\66\7\21\2\2\668\7\27\2\2\679\5\4\3\28\67\3")
        buf.write("\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2;<\3\2\2\2<=\7\30")
        buf.write("\2\2=?\3\2\2\2>\64\3\2\2\2>\65\3\2\2\2?\r\3\2\2\2@A\t")
        buf.write("\2\2\2A\17\3\2\2\2\t\22\24!(,:>")
        return buf.getvalue()


class TyptParser ( Parser ):

    grammarFileName = "Typt.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'if'", "'test'", "':'", 
                     "';'", "'Bool'", "'Int'", "'Float'", "'String'", "'Dynamic'", 
                     "'def'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "DEF", "NUMBER", "INTEGER", "NEWLINE", "DECIMAL_INTEGER", 
                      "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", "SKIP_", 
                      "INDENT", "DEDENT" ]

    RULE_program = 0
    RULE_stmt = 1
    RULE_simple_stmt = 2
    RULE_small_stmt = 3
    RULE_expr_stmt = 4
    RULE_suite = 5
    RULE_base_types = 6

    ruleNames =  [ "program", "stmt", "simple_stmt", "small_stmt", "expr_stmt", 
                   "suite", "base_types" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    DEF=12
    NUMBER=13
    INTEGER=14
    NEWLINE=15
    DECIMAL_INTEGER=16
    OCT_INTEGER=17
    HEX_INTEGER=18
    BIN_INTEGER=19
    SKIP_=20
    INDENT=21
    DEDENT=22

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
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyptParser.T__0) | (1 << TyptParser.T__2) | (1 << TyptParser.NEWLINE))) != 0):
                self.state = 16
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [TyptParser.NEWLINE]:
                    self.state = 14
                    self.match(TyptParser.NEWLINE)
                    pass
                elif token in [TyptParser.T__0, TyptParser.T__2]:
                    self.state = 15
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 21
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

        def DEF(self):
            return self.getToken(TyptParser.DEF, 0)

        def NEWLINE(self):
            return self.getToken(TyptParser.NEWLINE, 0)

        def suite(self):
            return self.getTypedRuleContext(TyptParser.SuiteContext,0)


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
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyptParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(TyptParser.T__0)
                self.state = 24
                self.match(TyptParser.DEF)
                self.state = 25
                self.match(TyptParser.T__1)
                self.state = 26
                self.match(TyptParser.NEWLINE)
                pass
            elif token in [TyptParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(TyptParser.T__2)
                self.state = 28
                self.match(TyptParser.T__3)
                self.state = 29
                self.match(TyptParser.T__4)
                self.state = 30
                self.suite()
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

        def small_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyptParser.Small_stmtContext)
            else:
                return self.getTypedRuleContext(TyptParser.Small_stmtContext,i)


        def NEWLINE(self):
            return self.getToken(TyptParser.NEWLINE, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.small_stmt()
            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 34
                    self.match(TyptParser.T__5)
                    self.state = 35
                    self.small_stmt() 
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TyptParser.T__5:
                self.state = 41
                self.match(TyptParser.T__5)


            self.state = 44
            self.match(TyptParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Small_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_stmt(self):
            return self.getTypedRuleContext(TyptParser.Expr_stmtContext,0)


        def getRuleIndex(self):
            return TyptParser.RULE_small_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSmall_stmt" ):
                listener.enterSmall_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSmall_stmt" ):
                listener.exitSmall_stmt(self)




    def small_stmt(self):

        localctx = TyptParser.Small_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_small_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.expr_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TyptParser.RULE_expr_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_stmt" ):
                listener.enterExpr_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_stmt" ):
                listener.exitExpr_stmt(self)




    def expr_stmt(self):

        localctx = TyptParser.Expr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr_stmt)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuiteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stmt(self):
            return self.getTypedRuleContext(TyptParser.Simple_stmtContext,0)


        def NEWLINE(self):
            return self.getToken(TyptParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(TyptParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(TyptParser.DEDENT, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyptParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyptParser.StmtContext,i)


        def getRuleIndex(self):
            return TyptParser.RULE_suite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuite" ):
                listener.enterSuite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuite" ):
                listener.exitSuite(self)




    def suite(self):

        localctx = TyptParser.SuiteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_suite)
        self._la = 0 # Token type
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.simple_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.match(TyptParser.NEWLINE)
                self.state = 52
                self.match(TyptParser.INDENT)
                self.state = 54 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 53
                    self.stmt()
                    self.state = 56 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==TyptParser.T__0 or _la==TyptParser.T__2):
                        break

                self.state = 58
                self.match(TyptParser.DEDENT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Base_typesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TyptParser.RULE_base_types

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase_types" ):
                listener.enterBase_types(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase_types" ):
                listener.exitBase_types(self)




    def base_types(self):

        localctx = TyptParser.Base_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_base_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyptParser.T__6) | (1 << TyptParser.T__7) | (1 << TyptParser.T__8) | (1 << TyptParser.T__9) | (1 << TyptParser.T__10))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





