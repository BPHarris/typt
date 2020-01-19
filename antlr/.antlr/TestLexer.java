// Generated from d:\Brandon\University\Third Year Project\typt\Typt\Test.g4 by ANTLR 4.7.1

from antlr4.Token import CommonToken
import re
import importlib

# Allow languages to extend the lexer and parser, by loading the parser dynamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class TestLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, VALUE=3, NUMBER=4, STRING=5, BOOLEAN=6, INTEGER=7, USING=8, 
		DEF=9, RETURN=10, IMPORT=11, IF=12, ELIF=13, ELSE=14, WHILE=15, FOR=16, 
		IN=17, OR=18, AND=19, NOT=20, IS=21, CLASS=22, DEL=23, PASS=24, CONTINUE=25, 
		BREAK=26, NONE=27, TRUE=28, FALSE=29, NEWLINE=30, NAME=31, DECIMAL_INTEGER=32, 
		OCT_INTEGER=33, HEX_INTEGER=34, BIN_INTEGER=35, FLOAT_NUMBER=36, DOT=37, 
		ELLIPSIS=38, STAR=39, COMMA=40, COLON=41, SEMI_COLON=42, AND_OP=43, OR_OP=44, 
		XOR_OP=45, NOT_OP=46, POWER=47, LEFT_SHIFT=48, RIGHT_SHIFT=49, ADD=50, 
		MINUS=51, DIV=52, MOD=53, IDIV=54, OPEN_PARENTHESIS=55, CLOSE_PARENTHESIS=56, 
		OPEN_BRACKET=57, CLOSE_BRACKET=58, OPEN_BRACE=59, CLOSE_BRACE=60, LESS_THAN=61, 
		GREATER_THAN=62, EQUALS=63, GT_EQ=64, LT_EQ=65, NOT_EQ_1=66, NOT_EQ_2=67, 
		AT=68, ARROW=69, ASSIGN=70, ADD_ASSIGN=71, SUB_ASSIGN=72, MULT_ASSIGN=73, 
		AT_ASSIGN=74, DIV_ASSIGN=75, MOD_ASSIGN=76, AND_ASSIGN=77, OR_ASSIGN=78, 
		XOR_ASSIGN=79, LEFT_SHIFT_ASSIGN=80, RIGHT_SHIFT_ASSIGN=81, POWER_ASSIGN=82, 
		IDIV_ASSIGN=83, SKIP_=84, UNKNOWN_CHAR=85;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "VALUE", "NUMBER", "STRING", "BOOLEAN", "INTEGER", "USING", 
		"DEF", "RETURN", "IMPORT", "IF", "ELIF", "ELSE", "WHILE", "FOR", "IN", 
		"OR", "AND", "NOT", "IS", "CLASS", "DEL", "PASS", "CONTINUE", "BREAK", 
		"NONE", "TRUE", "FALSE", "NEWLINE", "NAME", "DECIMAL_INTEGER", "OCT_INTEGER", 
		"HEX_INTEGER", "BIN_INTEGER", "FLOAT_NUMBER", "DOT", "ELLIPSIS", "STAR", 
		"COMMA", "COLON", "SEMI_COLON", "AND_OP", "OR_OP", "XOR_OP", "NOT_OP", 
		"POWER", "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", "MINUS", "DIV", "MOD", "IDIV", 
		"OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", "OPEN_BRACKET", "CLOSE_BRACKET", 
		"OPEN_BRACE", "CLOSE_BRACE", "LESS_THAN", "GREATER_THAN", "EQUALS", "GT_EQ", 
		"LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "AT", "ARROW", "ASSIGN", "ADD_ASSIGN", 
		"SUB_ASSIGN", "MULT_ASSIGN", "AT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
		"AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN", "RIGHT_SHIFT_ASSIGN", 
		"POWER_ASSIGN", "IDIV_ASSIGN", "SKIP_", "UNKNOWN_CHAR", "NAME_START", 
		"NAME_CONTINUE", "NON_ZERO_DIGIT", "DIGIT", "OCT_DIGIT", "HEX_DIGIT", 
		"BIN_DIGIT", "INT_PART", "FRACTION", "EXPONENT", "SHORT_STRING", "LONG_STRING", 
		"LONG_STRING_ITEM", "LONG_STRING_CHAR", "STRING_ESCAPE_SEQ", "SPACES", 
		"COMMENT", "LINE_JOINING"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'hi'", "' hi'", null, null, null, null, null, "'using'", "'def'", 
		"'return'", "'import'", "'if'", "'elif'", "'else'", "'while'", "'for'", 
		"'in'", "'or'", "'and'", "'not'", "'is'", "'class'", "'del'", "'pass'", 
		"'continue'", "'break'", "'None'", "'True'", "'False'", null, null, null, 
		null, null, null, null, "'.'", "'...'", "'*'", "','", "':'", "';'", "'&'", 
		"'|'", "'^'", "'~'", "'**'", "'<<'", "'>>'", "'+'", "'-'", "'/'", "'%'", 
		"'//'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'<'", "'>'", "'=='", 
		"'>='", "'<='", "'<>'", "'!='", "'@'", "'->'", "'='", "'+='", "'-='", 
		"'*='", "'@='", "'/='", "'%='", "'&='", "'|='", "'^='", "'<<='", "'>>='", 
		"'**='", "'//='"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, "VALUE", "NUMBER", "STRING", "BOOLEAN", "INTEGER", "USING", 
		"DEF", "RETURN", "IMPORT", "IF", "ELIF", "ELSE", "WHILE", "FOR", "IN", 
		"OR", "AND", "NOT", "IS", "CLASS", "DEL", "PASS", "CONTINUE", "BREAK", 
		"NONE", "TRUE", "FALSE", "NEWLINE", "NAME", "DECIMAL_INTEGER", "OCT_INTEGER", 
		"HEX_INTEGER", "BIN_INTEGER", "FLOAT_NUMBER", "DOT", "ELLIPSIS", "STAR", 
		"COMMA", "COLON", "SEMI_COLON", "AND_OP", "OR_OP", "XOR_OP", "NOT_OP", 
		"POWER", "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", "MINUS", "DIV", "MOD", "IDIV", 
		"OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", "OPEN_BRACKET", "CLOSE_BRACKET", 
		"OPEN_BRACE", "CLOSE_BRACE", "LESS_THAN", "GREATER_THAN", "EQUALS", "GT_EQ", 
		"LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "AT", "ARROW", "ASSIGN", "ADD_ASSIGN", 
		"SUB_ASSIGN", "MULT_ASSIGN", "AT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
		"AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN", "RIGHT_SHIFT_ASSIGN", 
		"POWER_ASSIGN", "IDIV_ASSIGN", "SKIP_", "UNKNOWN_CHAR"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


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



	public TestLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Test.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 29:
			NEWLINE_action((RuleContext)_localctx, actionIndex);
			break;
		case 54:
			OPEN_PARENTHESIS_action((RuleContext)_localctx, actionIndex);
			break;
		case 55:
			CLOSE_PARENTHESIS_action((RuleContext)_localctx, actionIndex);
			break;
		case 56:
			OPEN_BRACKET_action((RuleContext)_localctx, actionIndex);
			break;
		case 57:
			CLOSE_BRACKET_action((RuleContext)_localctx, actionIndex);
			break;
		case 58:
			OPEN_BRACE_action((RuleContext)_localctx, actionIndex);
			break;
		case 59:
			CLOSE_BRACE_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void NEWLINE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:

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
			    
			    
			break;
		}
	}
	private void OPEN_PARENTHESIS_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 1:
			self.opened += 1
			break;
		}
	}
	private void CLOSE_PARENTHESIS_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 2:
			self.opened -= 1
			break;
		}
	}
	private void OPEN_BRACKET_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 3:
			self.opened += 1
			break;
		}
	}
	private void CLOSE_BRACKET_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 4:
			self.opened -= 1
			break;
		}
	}
	private void OPEN_BRACE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 5:
			self.opened += 1
			break;
		}
	}
	private void CLOSE_BRACE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 6:
			self.opened -= 1
			break;
		}
	}
	@Override
	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 29:
			return NEWLINE_sempred((RuleContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean NEWLINE_sempred(RuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return self.at_start_of_line();
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2W\u02a9\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT"+
		"\4U\tU\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4_\t_\4"+
		"`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4g\tg\4h\th\3\2\3\2\3\2\3\3\3"+
		"\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\5\4\u00de\n\4\3\5\3\5\5\5\u00e2\n\5\3\6"+
		"\3\6\5\6\u00e6\n\6\3\7\3\7\5\7\u00ea\n\7\3\b\3\b\3\b\3\b\5\b\u00f0\n\b"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13"+
		"\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16"+
		"\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21"+
		"\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25"+
		"\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30"+
		"\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32"+
		"\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35"+
		"\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\5\37\u0163\n\37"+
		"\3\37\3\37\5\37\u0167\n\37\3\37\5\37\u016a\n\37\5\37\u016c\n\37\3\37\3"+
		"\37\3 \3 \7 \u0172\n \f \16 \u0175\13 \3!\3!\7!\u0179\n!\f!\16!\u017c"+
		"\13!\3!\6!\u017f\n!\r!\16!\u0180\5!\u0183\n!\3\"\3\"\3\"\6\"\u0188\n\""+
		"\r\"\16\"\u0189\3#\3#\3#\6#\u018f\n#\r#\16#\u0190\3$\3$\3$\6$\u0196\n"+
		"$\r$\16$\u0197\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u01a7\n%\3&\3"+
		"&\3\'\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60"+
		"\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65"+
		"\3\66\3\66\3\67\3\67\3\67\38\38\38\39\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3"+
		"<\3=\3=\3=\3>\3>\3?\3?\3@\3@\3@\3A\3A\3A\3B\3B\3B\3C\3C\3C\3D\3D\3D\3"+
		"E\3E\3F\3F\3F\3G\3G\3H\3H\3H\3I\3I\3I\3J\3J\3J\3K\3K\3K\3L\3L\3L\3M\3"+
		"M\3M\3N\3N\3N\3O\3O\3O\3P\3P\3P\3Q\3Q\3Q\3Q\3R\3R\3R\3R\3S\3S\3S\3S\3"+
		"T\3T\3T\3T\3U\3U\3U\5U\u022d\nU\3U\3U\3V\3V\3W\5W\u0234\nW\3X\3X\5X\u0238"+
		"\nX\3Y\3Y\3Z\3Z\3[\3[\3\\\3\\\3]\3]\3^\6^\u0245\n^\r^\16^\u0246\3_\6_"+
		"\u024a\n_\r_\16_\u024b\3`\3`\5`\u0250\n`\3`\6`\u0253\n`\r`\16`\u0254\3"+
		"a\3a\3a\7a\u025a\na\fa\16a\u025d\13a\3a\3a\3a\3a\7a\u0263\na\fa\16a\u0266"+
		"\13a\3a\5a\u0269\na\3b\3b\3b\3b\3b\7b\u0270\nb\fb\16b\u0273\13b\3b\3b"+
		"\3b\3b\3b\3b\3b\3b\7b\u027d\nb\fb\16b\u0280\13b\3b\3b\3b\5b\u0285\nb\3"+
		"c\3c\5c\u0289\nc\3d\3d\3e\3e\3e\3e\5e\u0291\ne\3f\6f\u0294\nf\rf\16f\u0295"+
		"\3g\3g\7g\u029a\ng\fg\16g\u029d\13g\3h\3h\5h\u02a1\nh\3h\5h\u02a4\nh\3"+
		"h\3h\5h\u02a8\nh\2\2i\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27"+
		"\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33"+
		"\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63"+
		"e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089"+
		"F\u008bG\u008dH\u008fI\u0091J\u0093K\u0095L\u0097M\u0099N\u009bO\u009d"+
		"P\u009fQ\u00a1R\u00a3S\u00a5T\u00a7U\u00a9V\u00abW\u00ad\2\u00af\2\u00b1"+
		"\2\u00b3\2\u00b5\2\u00b7\2\u00b9\2\u00bb\2\u00bd\2\u00bf\2\u00c1\2\u00c3"+
		"\2\u00c5\2\u00c7\2\u00c9\2\u00cb\2\u00cd\2\u00cf\2\3\2\22\4\2QQqq\4\2"+
		"ZZzz\4\2DDdd\5\2C\\aac|\3\2\63;\3\2\62;\3\2\629\5\2\62;CHch\3\2\62\63"+
		"\4\2GGgg\4\2--//\6\2\f\f\16\17))^^\6\2\f\f\16\17$$^^\3\2^^\4\2\13\13\""+
		"\"\4\2\f\f\16\17\2\u02c3\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2"+
		"\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25"+
		"\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2"+
		"\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2"+
		"\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3"+
		"\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2"+
		"\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2"+
		"Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3"+
		"\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2"+
		"\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2"+
		"w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2"+
		"\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b"+
		"\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2"+
		"\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d"+
		"\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2"+
		"\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\3\u00d1\3\2\2\2\5\u00d4"+
		"\3\2\2\2\7\u00dd\3\2\2\2\t\u00e1\3\2\2\2\13\u00e5\3\2\2\2\r\u00e9\3\2"+
		"\2\2\17\u00ef\3\2\2\2\21\u00f1\3\2\2\2\23\u00f7\3\2\2\2\25\u00fb\3\2\2"+
		"\2\27\u0102\3\2\2\2\31\u0109\3\2\2\2\33\u010c\3\2\2\2\35\u0111\3\2\2\2"+
		"\37\u0116\3\2\2\2!\u011c\3\2\2\2#\u0120\3\2\2\2%\u0123\3\2\2\2\'\u0126"+
		"\3\2\2\2)\u012a\3\2\2\2+\u012e\3\2\2\2-\u0131\3\2\2\2/\u0137\3\2\2\2\61"+
		"\u013b\3\2\2\2\63\u0140\3\2\2\2\65\u0149\3\2\2\2\67\u014f\3\2\2\29\u0154"+
		"\3\2\2\2;\u0159\3\2\2\2=\u016b\3\2\2\2?\u016f\3\2\2\2A\u0182\3\2\2\2C"+
		"\u0184\3\2\2\2E\u018b\3\2\2\2G\u0192\3\2\2\2I\u01a6\3\2\2\2K\u01a8\3\2"+
		"\2\2M\u01aa\3\2\2\2O\u01ae\3\2\2\2Q\u01b0\3\2\2\2S\u01b2\3\2\2\2U\u01b4"+
		"\3\2\2\2W\u01b6\3\2\2\2Y\u01b8\3\2\2\2[\u01ba\3\2\2\2]\u01bc\3\2\2\2_"+
		"\u01be\3\2\2\2a\u01c1\3\2\2\2c\u01c4\3\2\2\2e\u01c7\3\2\2\2g\u01c9\3\2"+
		"\2\2i\u01cb\3\2\2\2k\u01cd\3\2\2\2m\u01cf\3\2\2\2o\u01d2\3\2\2\2q\u01d5"+
		"\3\2\2\2s\u01d8\3\2\2\2u\u01db\3\2\2\2w\u01de\3\2\2\2y\u01e1\3\2\2\2{"+
		"\u01e4\3\2\2\2}\u01e6\3\2\2\2\177\u01e8\3\2\2\2\u0081\u01eb\3\2\2\2\u0083"+
		"\u01ee\3\2\2\2\u0085\u01f1\3\2\2\2\u0087\u01f4\3\2\2\2\u0089\u01f7\3\2"+
		"\2\2\u008b\u01f9\3\2\2\2\u008d\u01fc\3\2\2\2\u008f\u01fe\3\2\2\2\u0091"+
		"\u0201\3\2\2\2\u0093\u0204\3\2\2\2\u0095\u0207\3\2\2\2\u0097\u020a\3\2"+
		"\2\2\u0099\u020d\3\2\2\2\u009b\u0210\3\2\2\2\u009d\u0213\3\2\2\2\u009f"+
		"\u0216\3\2\2\2\u00a1\u0219\3\2\2\2\u00a3\u021d\3\2\2\2\u00a5\u0221\3\2"+
		"\2\2\u00a7\u0225\3\2\2\2\u00a9\u022c\3\2\2\2\u00ab\u0230\3\2\2\2\u00ad"+
		"\u0233\3\2\2\2\u00af\u0237\3\2\2\2\u00b1\u0239\3\2\2\2\u00b3\u023b\3\2"+
		"\2\2\u00b5\u023d\3\2\2\2\u00b7\u023f\3\2\2\2\u00b9\u0241\3\2\2\2\u00bb"+
		"\u0244\3\2\2\2\u00bd\u0249\3\2\2\2\u00bf\u024d\3\2\2\2\u00c1\u0268\3\2"+
		"\2\2\u00c3\u0284\3\2\2\2\u00c5\u0288\3\2\2\2\u00c7\u028a\3\2\2\2\u00c9"+
		"\u0290\3\2\2\2\u00cb\u0293\3\2\2\2\u00cd\u0297\3\2\2\2\u00cf\u029e\3\2"+
		"\2\2\u00d1\u00d2\7j\2\2\u00d2\u00d3\7k\2\2\u00d3\4\3\2\2\2\u00d4\u00d5"+
		"\7\"\2\2\u00d5\u00d6\7j\2\2\u00d6\u00d7\7k\2\2\u00d7\6\3\2\2\2\u00d8\u00de"+
		"\5? \2\u00d9\u00de\5\t\5\2\u00da\u00de\5\13\6\2\u00db\u00de\5\r\7\2\u00dc"+
		"\u00de\5\67\34\2\u00dd\u00d8\3\2\2\2\u00dd\u00d9\3\2\2\2\u00dd\u00da\3"+
		"\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de\b\3\2\2\2\u00df\u00e2"+
		"\5\17\b\2\u00e0\u00e2\5I%\2\u00e1\u00df\3\2\2\2\u00e1\u00e0\3\2\2\2\u00e2"+
		"\n\3\2\2\2\u00e3\u00e6\5\u00c1a\2\u00e4\u00e6\5\u00c3b\2\u00e5\u00e3\3"+
		"\2\2\2\u00e5\u00e4\3\2\2\2\u00e6\f\3\2\2\2\u00e7\u00ea\59\35\2\u00e8\u00ea"+
		"\5;\36\2\u00e9\u00e7\3\2\2\2\u00e9\u00e8\3\2\2\2\u00ea\16\3\2\2\2\u00eb"+
		"\u00f0\5A!\2\u00ec\u00f0\5C\"\2\u00ed\u00f0\5E#\2\u00ee\u00f0\5G$\2\u00ef"+
		"\u00eb\3\2\2\2\u00ef\u00ec\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00ee\3\2"+
		"\2\2\u00f0\20\3\2\2\2\u00f1\u00f2\7w\2\2\u00f2\u00f3\7u\2\2\u00f3\u00f4"+
		"\7k\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6\7i\2\2\u00f6\22\3\2\2\2\u00f7\u00f8"+
		"\7f\2\2\u00f8\u00f9\7g\2\2\u00f9\u00fa\7h\2\2\u00fa\24\3\2\2\2\u00fb\u00fc"+
		"\7t\2\2\u00fc\u00fd\7g\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7w\2\2\u00ff"+
		"\u0100\7t\2\2\u0100\u0101\7p\2\2\u0101\26\3\2\2\2\u0102\u0103\7k\2\2\u0103"+
		"\u0104\7o\2\2\u0104\u0105\7r\2\2\u0105\u0106\7q\2\2\u0106\u0107\7t\2\2"+
		"\u0107\u0108\7v\2\2\u0108\30\3\2\2\2\u0109\u010a\7k\2\2\u010a\u010b\7"+
		"h\2\2\u010b\32\3\2\2\2\u010c\u010d\7g\2\2\u010d\u010e\7n\2\2\u010e\u010f"+
		"\7k\2\2\u010f\u0110\7h\2\2\u0110\34\3\2\2\2\u0111\u0112\7g\2\2\u0112\u0113"+
		"\7n\2\2\u0113\u0114\7u\2\2\u0114\u0115\7g\2\2\u0115\36\3\2\2\2\u0116\u0117"+
		"\7y\2\2\u0117\u0118\7j\2\2\u0118\u0119\7k\2\2\u0119\u011a\7n\2\2\u011a"+
		"\u011b\7g\2\2\u011b \3\2\2\2\u011c\u011d\7h\2\2\u011d\u011e\7q\2\2\u011e"+
		"\u011f\7t\2\2\u011f\"\3\2\2\2\u0120\u0121\7k\2\2\u0121\u0122\7p\2\2\u0122"+
		"$\3\2\2\2\u0123\u0124\7q\2\2\u0124\u0125\7t\2\2\u0125&\3\2\2\2\u0126\u0127"+
		"\7c\2\2\u0127\u0128\7p\2\2\u0128\u0129\7f\2\2\u0129(\3\2\2\2\u012a\u012b"+
		"\7p\2\2\u012b\u012c\7q\2\2\u012c\u012d\7v\2\2\u012d*\3\2\2\2\u012e\u012f"+
		"\7k\2\2\u012f\u0130\7u\2\2\u0130,\3\2\2\2\u0131\u0132\7e\2\2\u0132\u0133"+
		"\7n\2\2\u0133\u0134\7c\2\2\u0134\u0135\7u\2\2\u0135\u0136\7u\2\2\u0136"+
		".\3\2\2\2\u0137\u0138\7f\2\2\u0138\u0139\7g\2\2\u0139\u013a\7n\2\2\u013a"+
		"\60\3\2\2\2\u013b\u013c\7r\2\2\u013c\u013d\7c\2\2\u013d\u013e\7u\2\2\u013e"+
		"\u013f\7u\2\2\u013f\62\3\2\2\2\u0140\u0141\7e\2\2\u0141\u0142\7q\2\2\u0142"+
		"\u0143\7p\2\2\u0143\u0144\7v\2\2\u0144\u0145\7k\2\2\u0145\u0146\7p\2\2"+
		"\u0146\u0147\7w\2\2\u0147\u0148\7g\2\2\u0148\64\3\2\2\2\u0149\u014a\7"+
		"d\2\2\u014a\u014b\7t\2\2\u014b\u014c\7g\2\2\u014c\u014d\7c\2\2\u014d\u014e"+
		"\7m\2\2\u014e\66\3\2\2\2\u014f\u0150\7P\2\2\u0150\u0151\7q\2\2\u0151\u0152"+
		"\7p\2\2\u0152\u0153\7g\2\2\u01538\3\2\2\2\u0154\u0155\7V\2\2\u0155\u0156"+
		"\7t\2\2\u0156\u0157\7w\2\2\u0157\u0158\7g\2\2\u0158:\3\2\2\2\u0159\u015a"+
		"\7H\2\2\u015a\u015b\7c\2\2\u015b\u015c\7n\2\2\u015c\u015d\7u\2\2\u015d"+
		"\u015e\7g\2\2\u015e<\3\2\2\2\u015f\u0160\6\37\2\2\u0160\u016c\5\u00cb"+
		"f\2\u0161\u0163\7\17\2\2\u0162\u0161\3\2\2\2\u0162\u0163\3\2\2\2\u0163"+
		"\u0164\3\2\2\2\u0164\u0167\7\f\2\2\u0165\u0167\4\16\17\2\u0166\u0162\3"+
		"\2\2\2\u0166\u0165\3\2\2\2\u0167\u0169\3\2\2\2\u0168\u016a\5\u00cbf\2"+
		"\u0169\u0168\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016c\3\2\2\2\u016b\u015f"+
		"\3\2\2\2\u016b\u0166\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016e\b\37\2\2"+
		"\u016e>\3\2\2\2\u016f\u0173\5\u00adW\2\u0170\u0172\5\u00afX\2\u0171\u0170"+
		"\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174"+
		"@\3\2\2\2\u0175\u0173\3\2\2\2\u0176\u017a\5\u00b1Y\2\u0177\u0179\5\u00b3"+
		"Z\2\u0178\u0177\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2\u017a"+
		"\u017b\3\2\2\2\u017b\u0183\3\2\2\2\u017c\u017a\3\2\2\2\u017d\u017f\7\62"+
		"\2\2\u017e\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u017e\3\2\2\2\u0180"+
		"\u0181\3\2\2\2\u0181\u0183\3\2\2\2\u0182\u0176\3\2\2\2\u0182\u017e\3\2"+
		"\2\2\u0183B\3\2\2\2\u0184\u0185\7\62\2\2\u0185\u0187\t\2\2\2\u0186\u0188"+
		"\5\u00b5[\2\u0187\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u0187\3\2\2"+
		"\2\u0189\u018a\3\2\2\2\u018aD\3\2\2\2\u018b\u018c\7\62\2\2\u018c\u018e"+
		"\t\3\2\2\u018d\u018f\5\u00b7\\\2\u018e\u018d\3\2\2\2\u018f\u0190\3\2\2"+
		"\2\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191F\3\2\2\2\u0192\u0193"+
		"\7\62\2\2\u0193\u0195\t\4\2\2\u0194\u0196\5\u00b9]\2\u0195\u0194\3\2\2"+
		"\2\u0196\u0197\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198H"+
		"\3\2\2\2\u0199\u019a\5\u00bb^\2\u019a\u019b\7\60\2\2\u019b\u019c\5\u00bd"+
		"_\2\u019c\u01a7\3\2\2\2\u019d\u019e\5\u00bb^\2\u019e\u019f\5\u00bf`\2"+
		"\u019f\u01a7\3\2\2\2\u01a0\u01a1\5\u00bb^\2\u01a1\u01a2\7\60\2\2\u01a2"+
		"\u01a3\5\u00bd_\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5\5\u00bf`\2\u01a5\u01a7"+
		"\3\2\2\2\u01a6\u0199\3\2\2\2\u01a6\u019d\3\2\2\2\u01a6\u01a0\3\2\2\2\u01a7"+
		"J\3\2\2\2\u01a8\u01a9\7\60\2\2\u01a9L\3\2\2\2\u01aa\u01ab\7\60\2\2\u01ab"+
		"\u01ac\7\60\2\2\u01ac\u01ad\7\60\2\2\u01adN\3\2\2\2\u01ae\u01af\7,\2\2"+
		"\u01afP\3\2\2\2\u01b0\u01b1\7.\2\2\u01b1R\3\2\2\2\u01b2\u01b3\7<\2\2\u01b3"+
		"T\3\2\2\2\u01b4\u01b5\7=\2\2\u01b5V\3\2\2\2\u01b6\u01b7\7(\2\2\u01b7X"+
		"\3\2\2\2\u01b8\u01b9\7~\2\2\u01b9Z\3\2\2\2\u01ba\u01bb\7`\2\2\u01bb\\"+
		"\3\2\2\2\u01bc\u01bd\7\u0080\2\2\u01bd^\3\2\2\2\u01be\u01bf\7,\2\2\u01bf"+
		"\u01c0\7,\2\2\u01c0`\3\2\2\2\u01c1\u01c2\7>\2\2\u01c2\u01c3\7>\2\2\u01c3"+
		"b\3\2\2\2\u01c4\u01c5\7@\2\2\u01c5\u01c6\7@\2\2\u01c6d\3\2\2\2\u01c7\u01c8"+
		"\7-\2\2\u01c8f\3\2\2\2\u01c9\u01ca\7/\2\2\u01cah\3\2\2\2\u01cb\u01cc\7"+
		"\61\2\2\u01ccj\3\2\2\2\u01cd\u01ce\7\'\2\2\u01cel\3\2\2\2\u01cf\u01d0"+
		"\7\61\2\2\u01d0\u01d1\7\61\2\2\u01d1n\3\2\2\2\u01d2\u01d3\7*\2\2\u01d3"+
		"\u01d4\b8\3\2\u01d4p\3\2\2\2\u01d5\u01d6\7+\2\2\u01d6\u01d7\b9\4\2\u01d7"+
		"r\3\2\2\2\u01d8\u01d9\7]\2\2\u01d9\u01da\b:\5\2\u01dat\3\2\2\2\u01db\u01dc"+
		"\7_\2\2\u01dc\u01dd\b;\6\2\u01ddv\3\2\2\2\u01de\u01df\7}\2\2\u01df\u01e0"+
		"\b<\7\2\u01e0x\3\2\2\2\u01e1\u01e2\7\177\2\2\u01e2\u01e3\b=\b\2\u01e3"+
		"z\3\2\2\2\u01e4\u01e5\7>\2\2\u01e5|\3\2\2\2\u01e6\u01e7\7@\2\2\u01e7~"+
		"\3\2\2\2\u01e8\u01e9\7?\2\2\u01e9\u01ea\7?\2\2\u01ea\u0080\3\2\2\2\u01eb"+
		"\u01ec\7@\2\2\u01ec\u01ed\7?\2\2\u01ed\u0082\3\2\2\2\u01ee\u01ef\7>\2"+
		"\2\u01ef\u01f0\7?\2\2\u01f0\u0084\3\2\2\2\u01f1\u01f2\7>\2\2\u01f2\u01f3"+
		"\7@\2\2\u01f3\u0086\3\2\2\2\u01f4\u01f5\7#\2\2\u01f5\u01f6\7?\2\2\u01f6"+
		"\u0088\3\2\2\2\u01f7\u01f8\7B\2\2\u01f8\u008a\3\2\2\2\u01f9\u01fa\7/\2"+
		"\2\u01fa\u01fb\7@\2\2\u01fb\u008c\3\2\2\2\u01fc\u01fd\7?\2\2\u01fd\u008e"+
		"\3\2\2\2\u01fe\u01ff\7-\2\2\u01ff\u0200\7?\2\2\u0200\u0090\3\2\2\2\u0201"+
		"\u0202\7/\2\2\u0202\u0203\7?\2\2\u0203\u0092\3\2\2\2\u0204\u0205\7,\2"+
		"\2\u0205\u0206\7?\2\2\u0206\u0094\3\2\2\2\u0207\u0208\7B\2\2\u0208\u0209"+
		"\7?\2\2\u0209\u0096\3\2\2\2\u020a\u020b\7\61\2\2\u020b\u020c\7?\2\2\u020c"+
		"\u0098\3\2\2\2\u020d\u020e\7\'\2\2\u020e\u020f\7?\2\2\u020f\u009a\3\2"+
		"\2\2\u0210\u0211\7(\2\2\u0211\u0212\7?\2\2\u0212\u009c\3\2\2\2\u0213\u0214"+
		"\7~\2\2\u0214\u0215\7?\2\2\u0215\u009e\3\2\2\2\u0216\u0217\7`\2\2\u0217"+
		"\u0218\7?\2\2\u0218\u00a0\3\2\2\2\u0219\u021a\7>\2\2\u021a\u021b\7>\2"+
		"\2\u021b\u021c\7?\2\2\u021c\u00a2\3\2\2\2\u021d\u021e\7@\2\2\u021e\u021f"+
		"\7@\2\2\u021f\u0220\7?\2\2\u0220\u00a4\3\2\2\2\u0221\u0222\7,\2\2\u0222"+
		"\u0223\7,\2\2\u0223\u0224\7?\2\2\u0224\u00a6\3\2\2\2\u0225\u0226\7\61"+
		"\2\2\u0226\u0227\7\61\2\2\u0227\u0228\7?\2\2\u0228\u00a8\3\2\2\2\u0229"+
		"\u022d\5\u00cbf\2\u022a\u022d\5\u00cdg\2\u022b\u022d\5\u00cfh\2\u022c"+
		"\u0229\3\2\2\2\u022c\u022a\3\2\2\2\u022c\u022b\3\2\2\2\u022d\u022e\3\2"+
		"\2\2\u022e\u022f\bU\t\2\u022f\u00aa\3\2\2\2\u0230\u0231\13\2\2\2\u0231"+
		"\u00ac\3\2\2\2\u0232\u0234\t\5\2\2\u0233\u0232\3\2\2\2\u0234\u00ae\3\2"+
		"\2\2\u0235\u0238\5\u00adW\2\u0236\u0238\5\u00b3Z\2\u0237\u0235\3\2\2\2"+
		"\u0237\u0236\3\2\2\2\u0238\u00b0\3\2\2\2\u0239\u023a\t\6\2\2\u023a\u00b2"+
		"\3\2\2\2\u023b\u023c\t\7\2\2\u023c\u00b4\3\2\2\2\u023d\u023e\t\b\2\2\u023e"+
		"\u00b6\3\2\2\2\u023f\u0240\t\t\2\2\u0240\u00b8\3\2\2\2\u0241\u0242\t\n"+
		"\2\2\u0242\u00ba\3\2\2\2\u0243\u0245\5\u00b3Z\2\u0244\u0243\3\2\2\2\u0245"+
		"\u0246\3\2\2\2\u0246\u0244\3\2\2\2\u0246\u0247\3\2\2\2\u0247\u00bc\3\2"+
		"\2\2\u0248\u024a\5\u00b3Z\2\u0249\u0248\3\2\2\2\u024a\u024b\3\2\2\2\u024b"+
		"\u0249\3\2\2\2\u024b\u024c\3\2\2\2\u024c\u00be\3\2\2\2\u024d\u024f\t\13"+
		"\2\2\u024e\u0250\t\f\2\2\u024f\u024e\3\2\2\2\u024f\u0250\3\2\2\2\u0250"+
		"\u0252\3\2\2\2\u0251\u0253\5\u00b3Z\2\u0252\u0251\3\2\2\2\u0253\u0254"+
		"\3\2\2\2\u0254\u0252\3\2\2\2\u0254\u0255\3\2\2\2\u0255\u00c0\3\2\2\2\u0256"+
		"\u025b\7)\2\2\u0257\u025a\5\u00c9e\2\u0258\u025a\n\r\2\2\u0259\u0257\3"+
		"\2\2\2\u0259\u0258\3\2\2\2\u025a\u025d\3\2\2\2\u025b\u0259\3\2\2\2\u025b"+
		"\u025c\3\2\2\2\u025c\u025e\3\2\2\2\u025d\u025b\3\2\2\2\u025e\u0269\7)"+
		"\2\2\u025f\u0264\7$\2\2\u0260\u0263\5\u00c9e\2\u0261\u0263\n\16\2\2\u0262"+
		"\u0260\3\2\2\2\u0262\u0261\3\2\2\2\u0263\u0266\3\2\2\2\u0264\u0262\3\2"+
		"\2\2\u0264\u0265\3\2\2\2\u0265\u0267\3\2\2\2\u0266\u0264\3\2\2\2\u0267"+
		"\u0269\7$\2\2\u0268\u0256\3\2\2\2\u0268\u025f\3\2\2\2\u0269\u00c2\3\2"+
		"\2\2\u026a\u026b\7)\2\2\u026b\u026c\7)\2\2\u026c\u026d\7)\2\2\u026d\u0271"+
		"\3\2\2\2\u026e\u0270\5\u00c5c\2\u026f\u026e\3\2\2\2\u0270\u0273\3\2\2"+
		"\2\u0271\u026f\3\2\2\2\u0271\u0272\3\2\2\2\u0272\u0274\3\2\2\2\u0273\u0271"+
		"\3\2\2\2\u0274\u0275\7)\2\2\u0275\u0276\7)\2\2\u0276\u0285\7)\2\2\u0277"+
		"\u0278\7$\2\2\u0278\u0279\7$\2\2\u0279\u027a\7$\2\2\u027a\u027e\3\2\2"+
		"\2\u027b\u027d\5\u00c5c\2\u027c\u027b\3\2\2\2\u027d\u0280\3\2\2\2\u027e"+
		"\u027c\3\2\2\2\u027e\u027f\3\2\2\2\u027f\u0281\3\2\2\2\u0280\u027e\3\2"+
		"\2\2\u0281\u0282\7$\2\2\u0282\u0283\7$\2\2\u0283\u0285\7$\2\2\u0284\u026a"+
		"\3\2\2\2\u0284\u0277\3\2\2\2\u0285\u00c4\3\2\2\2\u0286\u0289\5\u00c7d"+
		"\2\u0287\u0289\5\u00c9e\2\u0288\u0286\3\2\2\2\u0288\u0287\3\2\2\2\u0289"+
		"\u00c6\3\2\2\2\u028a\u028b\n\17\2\2\u028b\u00c8\3\2\2\2\u028c\u028d\7"+
		"^\2\2\u028d\u0291\13\2\2\2\u028e\u028f\7^\2\2\u028f\u0291\5=\37\2\u0290"+
		"\u028c\3\2\2\2\u0290\u028e\3\2\2\2\u0291\u00ca\3\2\2\2\u0292\u0294\t\20"+
		"\2\2\u0293\u0292\3\2\2\2\u0294\u0295\3\2\2\2\u0295\u0293\3\2\2\2\u0295"+
		"\u0296\3\2\2\2\u0296\u00cc\3\2\2\2\u0297\u029b\7%\2\2\u0298\u029a\n\21"+
		"\2\2\u0299\u0298\3\2\2\2\u029a\u029d\3\2\2\2\u029b\u0299\3\2\2\2\u029b"+
		"\u029c\3\2\2\2\u029c\u00ce\3\2\2\2\u029d\u029b\3\2\2\2\u029e\u02a0\7^"+
		"\2\2\u029f\u02a1\5\u00cbf\2\u02a0\u029f\3\2\2\2\u02a0\u02a1\3\2\2\2\u02a1"+
		"\u02a7\3\2\2\2\u02a2\u02a4\7\17\2\2\u02a3\u02a2\3\2\2\2\u02a3\u02a4\3"+
		"\2\2\2\u02a4\u02a5\3\2\2\2\u02a5\u02a8\7\f\2\2\u02a6\u02a8\4\16\17\2\u02a7"+
		"\u02a3\3\2\2\2\u02a7\u02a6\3\2\2\2\u02a8\u00d0\3\2\2\2*\2\u00dd\u00e1"+
		"\u00e5\u00e9\u00ef\u0162\u0166\u0169\u016b\u0173\u017a\u0180\u0182\u0189"+
		"\u0190\u0197\u01a6\u022c\u0233\u0237\u0246\u024b\u024f\u0254\u0259\u025b"+
		"\u0262\u0264\u0268\u0271\u027e\u0284\u0288\u0290\u0295\u029b\u02a0\u02a3"+
		"\u02a7\n\3\37\2\38\3\39\4\3:\5\3;\6\3<\7\3=\b\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}