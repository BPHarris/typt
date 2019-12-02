# Generated from .\Typt\Typt.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr4.Token import CommonToken
import re
import importlib

# Allow languages to extend the lexer and parser, by loading the parser dynamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("\u00d0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\5\17t\n\17\3\20\3\20\3\20\5\20y\n\20")
        buf.write("\3\20\3\20\5\20}\n\20\3\20\5\20\u0080\n\20\5\20\u0082")
        buf.write("\n\20\3\20\3\20\3\21\3\21\7\21\u0088\n\21\f\21\16\21\u008b")
        buf.write("\13\21\3\21\6\21\u008e\n\21\r\21\16\21\u008f\5\21\u0092")
        buf.write("\n\21\3\22\3\22\3\22\6\22\u0097\n\22\r\22\16\22\u0098")
        buf.write("\3\23\3\23\3\23\6\23\u009e\n\23\r\23\16\23\u009f\3\24")
        buf.write("\3\24\3\24\6\24\u00a5\n\24\r\24\16\24\u00a6\3\25\3\25")
        buf.write("\3\25\5\25\u00ac\n\25\3\25\3\25\3\26\3\26\3\27\3\27\3")
        buf.write("\30\3\30\3\31\3\31\3\32\3\32\3\33\6\33\u00bb\n\33\r\33")
        buf.write("\16\33\u00bc\3\34\3\34\7\34\u00c1\n\34\f\34\16\34\u00c4")
        buf.write("\13\34\3\35\3\35\5\35\u00c8\n\35\3\35\5\35\u00cb\n\35")
        buf.write("\3\35\3\35\5\35\u00cf\n\35\2\2\36\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\2-\2/\2\61\2\63\2\65\2\67\29\2")
        buf.write("\3\2\f\4\2QQqq\4\2ZZzz\4\2DDdd\3\2\63;\3\2\62;\3\2\62")
        buf.write("9\5\2\62;CHch\3\2\62\63\4\2\13\13\"\"\4\2\f\f\16\17\2")
        buf.write("\u00db\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\3;\3\2\2\2\5=\3\2")
        buf.write("\2\2\7?\3\2\2\2\tB\3\2\2\2\13G\3\2\2\2\rI\3\2\2\2\17K")
        buf.write("\3\2\2\2\21P\3\2\2\2\23T\3\2\2\2\25Z\3\2\2\2\27a\3\2\2")
        buf.write("\2\31i\3\2\2\2\33m\3\2\2\2\35s\3\2\2\2\37\u0081\3\2\2")
        buf.write("\2!\u0091\3\2\2\2#\u0093\3\2\2\2%\u009a\3\2\2\2\'\u00a1")
        buf.write("\3\2\2\2)\u00ab\3\2\2\2+\u00af\3\2\2\2-\u00b1\3\2\2\2")
        buf.write("/\u00b3\3\2\2\2\61\u00b5\3\2\2\2\63\u00b7\3\2\2\2\65\u00ba")
        buf.write("\3\2\2\2\67\u00be\3\2\2\29\u00c5\3\2\2\2;<\7*\2\2<\4\3")
        buf.write("\2\2\2=>\7+\2\2>\6\3\2\2\2?@\7k\2\2@A\7h\2\2A\b\3\2\2")
        buf.write("\2BC\7v\2\2CD\7g\2\2DE\7u\2\2EF\7v\2\2F\n\3\2\2\2GH\7")
        buf.write("<\2\2H\f\3\2\2\2IJ\7=\2\2J\16\3\2\2\2KL\7D\2\2LM\7q\2")
        buf.write("\2MN\7q\2\2NO\7n\2\2O\20\3\2\2\2PQ\7K\2\2QR\7p\2\2RS\7")
        buf.write("v\2\2S\22\3\2\2\2TU\7H\2\2UV\7n\2\2VW\7q\2\2WX\7c\2\2")
        buf.write("XY\7v\2\2Y\24\3\2\2\2Z[\7U\2\2[\\\7v\2\2\\]\7t\2\2]^\7")
        buf.write("k\2\2^_\7p\2\2_`\7i\2\2`\26\3\2\2\2ab\7F\2\2bc\7{\2\2")
        buf.write("cd\7p\2\2de\7c\2\2ef\7o\2\2fg\7k\2\2gh\7e\2\2h\30\3\2")
        buf.write("\2\2ij\7f\2\2jk\7g\2\2kl\7h\2\2l\32\3\2\2\2mn\5\35\17")
        buf.write("\2n\34\3\2\2\2ot\5!\21\2pt\5#\22\2qt\5%\23\2rt\5\'\24")
        buf.write("\2so\3\2\2\2sp\3\2\2\2sq\3\2\2\2sr\3\2\2\2t\36\3\2\2\2")
        buf.write("uv\6\20\2\2v\u0082\5\65\33\2wy\7\17\2\2xw\3\2\2\2xy\3")
        buf.write("\2\2\2yz\3\2\2\2z}\7\f\2\2{}\4\16\17\2|x\3\2\2\2|{\3\2")
        buf.write("\2\2}\177\3\2\2\2~\u0080\5\65\33\2\177~\3\2\2\2\177\u0080")
        buf.write("\3\2\2\2\u0080\u0082\3\2\2\2\u0081u\3\2\2\2\u0081|\3\2")
        buf.write("\2\2\u0082\u0083\3\2\2\2\u0083\u0084\b\20\2\2\u0084 \3")
        buf.write("\2\2\2\u0085\u0089\5+\26\2\u0086\u0088\5-\27\2\u0087\u0086")
        buf.write("\3\2\2\2\u0088\u008b\3\2\2\2\u0089\u0087\3\2\2\2\u0089")
        buf.write("\u008a\3\2\2\2\u008a\u0092\3\2\2\2\u008b\u0089\3\2\2\2")
        buf.write("\u008c\u008e\7\62\2\2\u008d\u008c\3\2\2\2\u008e\u008f")
        buf.write("\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090")
        buf.write("\u0092\3\2\2\2\u0091\u0085\3\2\2\2\u0091\u008d\3\2\2\2")
        buf.write("\u0092\"\3\2\2\2\u0093\u0094\7\62\2\2\u0094\u0096\t\2")
        buf.write("\2\2\u0095\u0097\5/\30\2\u0096\u0095\3\2\2\2\u0097\u0098")
        buf.write("\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099")
        buf.write("$\3\2\2\2\u009a\u009b\7\62\2\2\u009b\u009d\t\3\2\2\u009c")
        buf.write("\u009e\5\61\31\2\u009d\u009c\3\2\2\2\u009e\u009f\3\2\2")
        buf.write("\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0&\3\2")
        buf.write("\2\2\u00a1\u00a2\7\62\2\2\u00a2\u00a4\t\4\2\2\u00a3\u00a5")
        buf.write("\5\63\32\2\u00a4\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6")
        buf.write("\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7(\3\2\2\2\u00a8")
        buf.write("\u00ac\5\65\33\2\u00a9\u00ac\5\67\34\2\u00aa\u00ac\59")
        buf.write("\35\2\u00ab\u00a8\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa")
        buf.write("\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\b\25\3\2\u00ae")
        buf.write("*\3\2\2\2\u00af\u00b0\t\5\2\2\u00b0,\3\2\2\2\u00b1\u00b2")
        buf.write("\t\6\2\2\u00b2.\3\2\2\2\u00b3\u00b4\t\7\2\2\u00b4\60\3")
        buf.write("\2\2\2\u00b5\u00b6\t\b\2\2\u00b6\62\3\2\2\2\u00b7\u00b8")
        buf.write("\t\t\2\2\u00b8\64\3\2\2\2\u00b9\u00bb\t\n\2\2\u00ba\u00b9")
        buf.write("\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc")
        buf.write("\u00bd\3\2\2\2\u00bd\66\3\2\2\2\u00be\u00c2\7%\2\2\u00bf")
        buf.write("\u00c1\n\13\2\2\u00c0\u00bf\3\2\2\2\u00c1\u00c4\3\2\2")
        buf.write("\2\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c38\3\2")
        buf.write("\2\2\u00c4\u00c2\3\2\2\2\u00c5\u00c7\7^\2\2\u00c6\u00c8")
        buf.write("\5\65\33\2\u00c7\u00c6\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8")
        buf.write("\u00ce\3\2\2\2\u00c9\u00cb\7\17\2\2\u00ca\u00c9\3\2\2")
        buf.write("\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cf")
        buf.write("\7\f\2\2\u00cd\u00cf\4\16\17\2\u00ce\u00ca\3\2\2\2\u00ce")
        buf.write("\u00cd\3\2\2\2\u00cf:\3\2\2\2\24\2sx|\177\u0081\u0089")
        buf.write("\u008f\u0091\u0098\u009f\u00a6\u00ab\u00bc\u00c2\u00c7")
        buf.write("\u00ca\u00ce\4\3\20\2\b\2\2")
        return buf.getvalue()


class TyptLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    DEF = 12
    NUMBER = 13
    INTEGER = 14
    NEWLINE = 15
    DECIMAL_INTEGER = 16
    OCT_INTEGER = 17
    HEX_INTEGER = 18
    BIN_INTEGER = 19
    SKIP_ = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'if'", "'test'", "':'", "';'", "'Bool'", "'Int'", 
            "'Float'", "'String'", "'Dynamic'", "'def'" ]

    symbolicNames = [ "<INVALID>",
            "DEF", "NUMBER", "INTEGER", "NEWLINE", "DECIMAL_INTEGER", "OCT_INTEGER", 
            "HEX_INTEGER", "BIN_INTEGER", "SKIP_" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "DEF", "NUMBER", "INTEGER", 
                  "NEWLINE", "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", 
                  "BIN_INTEGER", "SKIP_", "NON_ZERO_DIGIT", "DIGIT", "OCT_DIGIT", 
                  "HEX_DIGIT", "BIN_DIGIT", "SPACES", "COMMENT", "LINE_JOINING" ]

    grammarFileName = "Typt.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    @property
    def tokens(self):
        try:
            return self._tokens
        except AttributeError:
            self._tokens = []
            return self._tokens

    @property
    def indents(self):
        try:
            return self._indents
        except AttributeError:
            self._indents = []
            return self._indents

    @property
    def opened(self):
        try:
            return self._opened
        except AttributeError:
            self._opened = 0
            return self._opened

    @opened.setter
    def opened(self, value):
        self._opened = value

    @property
    def last_token(self):
        try:
            return self._last_token
        except AttributeError:
            self._last_token = None
            return self._last_token

    @last_token.setter
    def last_token(self, value):
        self._last_token = value

    def reset(self):
        super().reset()
        self.tokens = []
        self.indents = []
        self.opened = 0
        self.last_token = None

    def emitToken(self, t):
        """Name non-PEP8 as name is fixed by antlr."""
        super().emitToken(t)
        self.tokens.append(t)

    def nextToken(self):
        """Name non-PEP8 as name is fixed by antlr."""
        if self._input.LA(1) == Token.EOF and self.indents:
            for i in range(len(self.tokens)-1,-1,-1):
                if self.tokens[i].type == Token.EOF:
                    self.tokens.pop(i)
        
            self.emitToken(self.common_token(LanguageParser.NEWLINE, '\n'))
        
            # Handle dedents
            while self.indents:
                self.emitToken(self.create_dedent())
                self.indents.pop()
        
            self.emitToken(self.common_token(LanguageParser.EOF, "<EOF>"))
        
        next = super().nextToken()
        if next.channel == Token.DEFAULT_CHANNEL:
            self.last_token = next
        
        return next if not self.tokens else self.tokens.pop(0)

    def create_dedent(self):
        """Return a new DEDENT token at the current line."""
        dedent = self.common_token(LanguageParser.DEDENT, "")
        dedent.line = self.last_token.line
        return dedent

    def common_token(self, type, text, indent=0):
        """Create a common token of the the given type."""
        stop = self.getCharIndex() - 1 - indent
        start = (stop - len(text) + 1) if text else stop
        return CommonToken(self._tokenFactorySourcePair, type, super().DEFAULT_TOKEN_CHANNEL, start, stop)

    @staticmethod
    def get_indentation_count(spaces):
        count = 0
        for ch in spaces:
            if ch == '\t':
                count += 8 - (count % 8)
            else:
                count += 1
        return count

    def at_start_of_line(self):
        """Get the token at the begining of the current line."""
        return Lexer.column.fget(self) == 0 and Lexer.line.fget(self) == 1



    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[14] = self.NEWLINE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            tempt = Lexer.text.fget(self)
            newline = re.sub("[^\r\n\f]+", "", tempt)
            spaces = re.sub("[\r\n\f]+", "", tempt)

            la_char = ""
            try:
                la_char = chr(self._input.LA(1))
            except ValueError:
                # Occurs on EOF
                pass

            if self.opened > 0 or la_char in ('\r', '\n', '\f', '#'):
                self.skip()
            else:
                indent = self.get_indentation_count(spaces)
                previous = self.indents[-1] if self.indents else 0
                self.emitToken(self.common_token(self.NEWLINE, newline, indent=indent))
                
                if indent == previous:
                    self.skip()
                elif indent > previous:
                    self.indents.append(indent)
                    self.emitToken(self.common_token(LanguageParser.INDENT, spaces))
                else:
                    while self.indents and self.indents[-1] > indent:
                        self.emitToken(self.create_dedent())
                        self.indents.pop()
                
                
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[14] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.at_start_of_line()
         


