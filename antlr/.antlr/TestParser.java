// Generated from d:\Brandon\University\Third Year Project\typt\Typt\Test.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class TestParser extends Parser {
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
		IDIV_ASSIGN=83, SKIP_=84, UNKNOWN_CHAR=85, INDENT=86, DEDENT=87;
	public static final int
		RULE_program = 0;
	public static final String[] ruleNames = {
		"program"
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
		"POWER_ASSIGN", "IDIV_ASSIGN", "SKIP_", "UNKNOWN_CHAR", "INDENT", "DEDENT"
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

	@Override
	public String getGrammarFileName() { return "Test.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public TestParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(TestParser.EOF, 0); }
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2);
			match(T__0);
			setState(6);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(3);
				match(T__1);
				}
				}
				setState(8);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(9);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3Y\16\4\2\t\2\3\2\3"+
		"\2\7\2\7\n\2\f\2\16\2\n\13\2\3\2\3\2\3\2\2\2\3\2\2\2\2\r\2\4\3\2\2\2\4"+
		"\b\7\3\2\2\5\7\7\4\2\2\6\5\3\2\2\2\7\n\3\2\2\2\b\6\3\2\2\2\b\t\3\2\2\2"+
		"\t\13\3\2\2\2\n\b\3\2\2\2\13\f\7\2\2\3\f\3\3\2\2\2\3\b";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}