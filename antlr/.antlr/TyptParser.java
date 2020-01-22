// Generated from /home/brandon/Documents/GitKraken/typt/antlr/Typt.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class TyptParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, T__40=41, T__41=42, T__42=43, T__43=44, T__44=45, 
		T__45=46, T__46=47, T__47=48, T__48=49, T__49=50, T__50=51, T__51=52, 
		T__52=53, T__53=54, T__54=55, T__55=56, T__56=57, T__57=58, T__58=59, 
		T__59=60, T__60=61, T__61=62, T__62=63, T__63=64, T__64=65, T__65=66, 
		T__66=67, T__67=68, T__68=69, T__69=70, T__70=71, T__71=72, T__72=73, 
		T__73=74, T__74=75, T__75=76, T__76=77, T__77=78, T__78=79, NUMBER=80, 
		STRING=81, BOOLEAN=82, INTEGER=83, NEWLINE=84, NAME=85, DECIMAL_INTEGER=86, 
		OCT_INTEGER=87, HEX_INTEGER=88, BIN_INTEGER=89, FLOAT_NUMBER=90, SKIP_=91, 
		UNKNOWN_CHAR=92, INDENT=93, DEDENT=94;
	public static final int
		RULE_program = 0, RULE_using = 1, RULE_stmt = 2, RULE_argument_list = 3, 
		RULE_argument = 4, RULE_simple_stmt = 5, RULE_small_stmt = 6, RULE_expr_stmt = 7, 
		RULE_anassign = 8, RULE_augassign = 9, RULE_var_dec_stmt = 10, RULE_del_stmt = 11, 
		RULE_pass_stmt = 12, RULE_flow_stmt = 13, RULE_break_stmt = 14, RULE_continue_stmt = 15, 
		RULE_return_stmt = 16, RULE_compound_stmt = 17, RULE_if_stmt = 18, RULE_while_stmt = 19, 
		RULE_for_stmt = 20, RULE_suite = 21, RULE_func_def = 22, RULE_func_signature = 23, 
		RULE_func_parameter_list = 24, RULE_class_def = 25, RULE_class_dec = 26, 
		RULE_class_method = 27, RULE_class_static_method = 28, RULE_test = 29, 
		RULE_or_test = 30, RULE_and_test = 31, RULE_not_test = 32, RULE_comparison = 33, 
		RULE_comp_op = 34, RULE_expr = 35, RULE_or_expr = 36, RULE_xor_expr = 37, 
		RULE_and_expr = 38, RULE_shift_expr = 39, RULE_shift_op = 40, RULE_arith_expr = 41, 
		RULE_arith_op = 42, RULE_term = 43, RULE_term_op = 44, RULE_factor = 45, 
		RULE_factor_op = 46, RULE_power = 47, RULE_atom_expr = 48, RULE_atom = 49, 
		RULE_trailer = 50, RULE_subscriptlist = 51, RULE_subscript = 52, RULE_sliceop = 53, 
		RULE_exprlist = 54, RULE_testlist = 55, RULE_name = 56, RULE_typt_type = 57;
	public static final String[] ruleNames = {
		"program", "using", "stmt", "argument_list", "argument", "simple_stmt", 
		"small_stmt", "expr_stmt", "anassign", "augassign", "var_dec_stmt", "del_stmt", 
		"pass_stmt", "flow_stmt", "break_stmt", "continue_stmt", "return_stmt", 
		"compound_stmt", "if_stmt", "while_stmt", "for_stmt", "suite", "func_def", 
		"func_signature", "func_parameter_list", "class_def", "class_dec", "class_method", 
		"class_static_method", "test", "or_test", "and_test", "not_test", "comparison", 
		"comp_op", "expr", "or_expr", "xor_expr", "and_expr", "shift_expr", "shift_op", 
		"arith_expr", "arith_op", "term", "term_op", "factor", "factor_op", "power", 
		"atom_expr", "atom", "trailer", "subscriptlist", "subscript", "sliceop", 
		"exprlist", "testlist", "name", "typt_type"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'using'", "':'", "'from'", "'as'", "','", "'='", "'+='", "'-='", 
		"'*='", "'@='", "'/='", "'%='", "'&='", "'|='", "'^='", "'<<='", "'>>='", 
		"'**='", "'//='", "'del'", "'pass'", "'break'", "'continue'", "'return'", 
		"'if'", "'elif'", "'else'", "'while'", "'for'", "'in'", "'def'", "'('", 
		"')'", "'->'", "'__init__'", "'self'", "'class'", "'@'", "'staticmethod'", 
		"'or'", "'and'", "'not'", "'<'", "'>'", "'=='", "'>='", "'<='", "'!='", 
		"'is'", "'|'", "'^'", "'&'", "'<<'", "'>>'", "'+'", "'-'", "'*'", "'/'", 
		"'%'", "'//'", "'~'", "'**'", "'None'", "'True'", "'False'", "'['", "']'", 
		"'.'", "'Bool'", "'Int'", "'Float'", "'String'", "'Object'", "'{'", "'}'", 
		"'List'", "'Tuple'", "'Set'", "'Dict'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, "NUMBER", "STRING", "BOOLEAN", 
		"INTEGER", "NEWLINE", "NAME", "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", 
		"BIN_INTEGER", "FLOAT_NUMBER", "SKIP_", "UNKNOWN_CHAR", "INDENT", "DEDENT"
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
	public String getGrammarFileName() { return "Typt.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public TyptParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(TyptParser.EOF, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(TyptParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(TyptParser.NEWLINE, i);
		}
		public List<UsingContext> using() {
			return getRuleContexts(UsingContext.class);
		}
		public UsingContext using(int i) {
			return getRuleContext(UsingContext.class,i);
		}
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
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
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(118);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case NEWLINE:
						{
						setState(116);
						match(NEWLINE);
						}
						break;
					case T__0:
						{
						setState(117);
						using();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					} 
				}
				setState(122);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			}
			setState(127);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__19) | (1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << T__27) | (1L << T__28) | (1L << T__30) | (1L << T__35) | (1L << T__36) | (1L << T__41) | (1L << T__54) | (1L << T__55) | (1L << T__60) | (1L << T__62))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (T__63 - 64)) | (1L << (T__64 - 64)) | (1L << (NUMBER - 64)) | (1L << (STRING - 64)) | (1L << (NEWLINE - 64)) | (1L << (NAME - 64)))) != 0)) {
				{
				setState(125);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case NEWLINE:
					{
					setState(123);
					match(NEWLINE);
					}
					break;
				case T__19:
				case T__20:
				case T__21:
				case T__22:
				case T__23:
				case T__24:
				case T__27:
				case T__28:
				case T__30:
				case T__35:
				case T__36:
				case T__41:
				case T__54:
				case T__55:
				case T__60:
				case T__62:
				case T__63:
				case T__64:
				case NUMBER:
				case STRING:
				case NAME:
					{
					setState(124);
					stmt();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(129);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(130);
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

	public static class UsingContext extends ParserRuleContext {
		public NameContext library_name;
		public NameContext library_alias;
		public List<TerminalNode> NEWLINE() { return getTokens(TyptParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(TyptParser.NEWLINE, i);
		}
		public TerminalNode INDENT() { return getToken(TyptParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(TyptParser.DEDENT, 0); }
		public List<NameContext> name() {
			return getRuleContexts(NameContext.class);
		}
		public NameContext name(int i) {
			return getRuleContext(NameContext.class,i);
		}
		public List<Func_signatureContext> func_signature() {
			return getRuleContexts(Func_signatureContext.class);
		}
		public Func_signatureContext func_signature(int i) {
			return getRuleContext(Func_signatureContext.class,i);
		}
		public UsingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_using; }
	}

	public final UsingContext using() throws RecognitionException {
		UsingContext _localctx = new UsingContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_using);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			match(T__0);
			setState(133);
			match(T__1);
			setState(134);
			match(NEWLINE);
			setState(135);
			match(INDENT);
			setState(139); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(136);
				func_signature();
				setState(137);
				match(NEWLINE);
				}
				}
				setState(141); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NAME );
			setState(143);
			match(DEDENT);
			setState(144);
			match(T__2);
			setState(145);
			((UsingContext)_localctx).library_name = name();
			setState(148);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__3) {
				{
				setState(146);
				match(T__3);
				setState(147);
				((UsingContext)_localctx).library_alias = name();
				}
			}

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

	public static class StmtContext extends ParserRuleContext {
		public Simple_stmtContext simple_stmt() {
			return getRuleContext(Simple_stmtContext.class,0);
		}
		public Compound_stmtContext compound_stmt() {
			return getRuleContext(Compound_stmtContext.class,0);
		}
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_stmt);
		try {
			setState(152);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__19:
			case T__20:
			case T__21:
			case T__22:
			case T__23:
			case T__35:
			case T__41:
			case T__54:
			case T__55:
			case T__60:
			case T__62:
			case T__63:
			case T__64:
			case NUMBER:
			case STRING:
			case NAME:
				enterOuterAlt(_localctx, 1);
				{
				setState(150);
				simple_stmt();
				}
				break;
			case T__24:
			case T__27:
			case T__28:
			case T__30:
			case T__36:
				enterOuterAlt(_localctx, 2);
				{
				setState(151);
				compound_stmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class Argument_listContext extends ParserRuleContext {
		public List<ArgumentContext> argument() {
			return getRuleContexts(ArgumentContext.class);
		}
		public ArgumentContext argument(int i) {
			return getRuleContext(ArgumentContext.class,i);
		}
		public Argument_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argument_list; }
	}

	public final Argument_listContext argument_list() throws RecognitionException {
		Argument_listContext _localctx = new Argument_listContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_argument_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(154);
			argument();
			setState(159);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__4) {
				{
				{
				setState(155);
				match(T__4);
				setState(156);
				argument();
				}
				}
				setState(161);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	public static class ArgumentContext extends ParserRuleContext {
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public ArgumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argument; }
	}

	public final ArgumentContext argument() throws RecognitionException {
		ArgumentContext _localctx = new ArgumentContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_argument);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			test();
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

	public static class Simple_stmtContext extends ParserRuleContext {
		public Small_stmtContext small_stmt() {
			return getRuleContext(Small_stmtContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(TyptParser.NEWLINE, 0); }
		public Simple_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simple_stmt; }
	}

	public final Simple_stmtContext simple_stmt() throws RecognitionException {
		Simple_stmtContext _localctx = new Simple_stmtContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_simple_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(164);
			small_stmt();
			setState(165);
			match(NEWLINE);
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

	public static class Small_stmtContext extends ParserRuleContext {
		public Expr_stmtContext expr_stmt() {
			return getRuleContext(Expr_stmtContext.class,0);
		}
		public Var_dec_stmtContext var_dec_stmt() {
			return getRuleContext(Var_dec_stmtContext.class,0);
		}
		public Del_stmtContext del_stmt() {
			return getRuleContext(Del_stmtContext.class,0);
		}
		public Pass_stmtContext pass_stmt() {
			return getRuleContext(Pass_stmtContext.class,0);
		}
		public Flow_stmtContext flow_stmt() {
			return getRuleContext(Flow_stmtContext.class,0);
		}
		public Small_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_small_stmt; }
	}

	public final Small_stmtContext small_stmt() throws RecognitionException {
		Small_stmtContext _localctx = new Small_stmtContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_small_stmt);
		try {
			setState(172);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(167);
				expr_stmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(168);
				var_dec_stmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(169);
				del_stmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(170);
				pass_stmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(171);
				flow_stmt();
				}
				break;
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

	public static class Expr_stmtContext extends ParserRuleContext {
		public TestContext lhs;
		public TestContext rhs;
		public List<TestContext> test() {
			return getRuleContexts(TestContext.class);
		}
		public TestContext test(int i) {
			return getRuleContext(TestContext.class,i);
		}
		public AnassignContext anassign() {
			return getRuleContext(AnassignContext.class,0);
		}
		public AugassignContext augassign() {
			return getRuleContext(AugassignContext.class,0);
		}
		public Expr_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_stmt; }
	}

	public final Expr_stmtContext expr_stmt() throws RecognitionException {
		Expr_stmtContext _localctx = new Expr_stmtContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_expr_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			((Expr_stmtContext)_localctx).lhs = test();
			setState(181);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__5) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18))) != 0)) {
				{
				setState(177);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__5:
					{
					setState(175);
					anassign();
					}
					break;
				case T__6:
				case T__7:
				case T__8:
				case T__9:
				case T__10:
				case T__11:
				case T__12:
				case T__13:
				case T__14:
				case T__15:
				case T__16:
				case T__17:
				case T__18:
					{
					setState(176);
					augassign();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(179);
				((Expr_stmtContext)_localctx).rhs = test();
				}
			}

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

	public static class AnassignContext extends ParserRuleContext {
		public AnassignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_anassign; }
	}

	public final AnassignContext anassign() throws RecognitionException {
		AnassignContext _localctx = new AnassignContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_anassign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(183);
			match(T__5);
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

	public static class AugassignContext extends ParserRuleContext {
		public AugassignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_augassign; }
	}

	public final AugassignContext augassign() throws RecognitionException {
		AugassignContext _localctx = new AugassignContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_augassign);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(185);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class Var_dec_stmtContext extends ParserRuleContext {
		public NameContext lhs;
		public TestContext rhs;
		public Typt_typeContext typt_type() {
			return getRuleContext(Typt_typeContext.class,0);
		}
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public Var_dec_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_dec_stmt; }
	}

	public final Var_dec_stmtContext var_dec_stmt() throws RecognitionException {
		Var_dec_stmtContext _localctx = new Var_dec_stmtContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_var_dec_stmt);
		try {
			setState(197);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(187);
				((Var_dec_stmtContext)_localctx).lhs = name();
				setState(188);
				match(T__1);
				setState(189);
				typt_type(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(191);
				((Var_dec_stmtContext)_localctx).lhs = name();
				setState(192);
				match(T__1);
				setState(193);
				typt_type(0);
				setState(194);
				match(T__5);
				setState(195);
				((Var_dec_stmtContext)_localctx).rhs = test();
				}
				break;
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

	public static class Del_stmtContext extends ParserRuleContext {
		public ExprlistContext exprlist() {
			return getRuleContext(ExprlistContext.class,0);
		}
		public Del_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_del_stmt; }
	}

	public final Del_stmtContext del_stmt() throws RecognitionException {
		Del_stmtContext _localctx = new Del_stmtContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_del_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(199);
			match(T__19);
			setState(200);
			exprlist();
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

	public static class Pass_stmtContext extends ParserRuleContext {
		public Pass_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pass_stmt; }
	}

	public final Pass_stmtContext pass_stmt() throws RecognitionException {
		Pass_stmtContext _localctx = new Pass_stmtContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_pass_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			match(T__20);
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

	public static class Flow_stmtContext extends ParserRuleContext {
		public Break_stmtContext break_stmt() {
			return getRuleContext(Break_stmtContext.class,0);
		}
		public Continue_stmtContext continue_stmt() {
			return getRuleContext(Continue_stmtContext.class,0);
		}
		public Return_stmtContext return_stmt() {
			return getRuleContext(Return_stmtContext.class,0);
		}
		public Flow_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_flow_stmt; }
	}

	public final Flow_stmtContext flow_stmt() throws RecognitionException {
		Flow_stmtContext _localctx = new Flow_stmtContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_flow_stmt);
		try {
			setState(207);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__21:
				enterOuterAlt(_localctx, 1);
				{
				setState(204);
				break_stmt();
				}
				break;
			case T__22:
				enterOuterAlt(_localctx, 2);
				{
				setState(205);
				continue_stmt();
				}
				break;
			case T__23:
				enterOuterAlt(_localctx, 3);
				{
				setState(206);
				return_stmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class Break_stmtContext extends ParserRuleContext {
		public Break_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_break_stmt; }
	}

	public final Break_stmtContext break_stmt() throws RecognitionException {
		Break_stmtContext _localctx = new Break_stmtContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_break_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(209);
			match(T__21);
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

	public static class Continue_stmtContext extends ParserRuleContext {
		public Continue_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continue_stmt; }
	}

	public final Continue_stmtContext continue_stmt() throws RecognitionException {
		Continue_stmtContext _localctx = new Continue_stmtContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_continue_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(211);
			match(T__22);
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

	public static class Return_stmtContext extends ParserRuleContext {
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public Return_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_stmt; }
	}

	public final Return_stmtContext return_stmt() throws RecognitionException {
		Return_stmtContext _localctx = new Return_stmtContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_return_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(213);
			match(T__23);
			setState(215);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 36)) & ~0x3f) == 0 && ((1L << (_la - 36)) & ((1L << (T__35 - 36)) | (1L << (T__41 - 36)) | (1L << (T__54 - 36)) | (1L << (T__55 - 36)) | (1L << (T__60 - 36)) | (1L << (T__62 - 36)) | (1L << (T__63 - 36)) | (1L << (T__64 - 36)) | (1L << (NUMBER - 36)) | (1L << (STRING - 36)) | (1L << (NAME - 36)))) != 0)) {
				{
				setState(214);
				test();
				}
			}

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

	public static class Compound_stmtContext extends ParserRuleContext {
		public If_stmtContext if_stmt() {
			return getRuleContext(If_stmtContext.class,0);
		}
		public While_stmtContext while_stmt() {
			return getRuleContext(While_stmtContext.class,0);
		}
		public For_stmtContext for_stmt() {
			return getRuleContext(For_stmtContext.class,0);
		}
		public Func_defContext func_def() {
			return getRuleContext(Func_defContext.class,0);
		}
		public Class_defContext class_def() {
			return getRuleContext(Class_defContext.class,0);
		}
		public Compound_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compound_stmt; }
	}

	public final Compound_stmtContext compound_stmt() throws RecognitionException {
		Compound_stmtContext _localctx = new Compound_stmtContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_compound_stmt);
		try {
			setState(222);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__24:
				enterOuterAlt(_localctx, 1);
				{
				setState(217);
				if_stmt();
				}
				break;
			case T__27:
				enterOuterAlt(_localctx, 2);
				{
				setState(218);
				while_stmt();
				}
				break;
			case T__28:
				enterOuterAlt(_localctx, 3);
				{
				setState(219);
				for_stmt();
				}
				break;
			case T__30:
				enterOuterAlt(_localctx, 4);
				{
				setState(220);
				func_def();
				}
				break;
			case T__36:
				enterOuterAlt(_localctx, 5);
				{
				setState(221);
				class_def();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class If_stmtContext extends ParserRuleContext {
		public TestContext if_test;
		public SuiteContext if_suite;
		public SuiteContext else_suite;
		public List<TestContext> test() {
			return getRuleContexts(TestContext.class);
		}
		public TestContext test(int i) {
			return getRuleContext(TestContext.class,i);
		}
		public List<SuiteContext> suite() {
			return getRuleContexts(SuiteContext.class);
		}
		public SuiteContext suite(int i) {
			return getRuleContext(SuiteContext.class,i);
		}
		public If_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_stmt; }
	}

	public final If_stmtContext if_stmt() throws RecognitionException {
		If_stmtContext _localctx = new If_stmtContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_if_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(224);
			match(T__24);
			setState(225);
			((If_stmtContext)_localctx).if_test = test();
			setState(226);
			match(T__1);
			setState(227);
			((If_stmtContext)_localctx).if_suite = suite();
			setState(235);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__25) {
				{
				{
				setState(228);
				match(T__25);
				setState(229);
				test();
				setState(230);
				match(T__1);
				setState(231);
				suite();
				}
				}
				setState(237);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(241);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__26) {
				{
				setState(238);
				match(T__26);
				setState(239);
				match(T__1);
				setState(240);
				((If_stmtContext)_localctx).else_suite = suite();
				}
			}

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

	public static class While_stmtContext extends ParserRuleContext {
		public TestContext while_test;
		public SuiteContext while_suite;
		public SuiteContext else_suite;
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public List<SuiteContext> suite() {
			return getRuleContexts(SuiteContext.class);
		}
		public SuiteContext suite(int i) {
			return getRuleContext(SuiteContext.class,i);
		}
		public While_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_stmt; }
	}

	public final While_stmtContext while_stmt() throws RecognitionException {
		While_stmtContext _localctx = new While_stmtContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_while_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(243);
			match(T__27);
			setState(244);
			((While_stmtContext)_localctx).while_test = test();
			setState(245);
			match(T__1);
			setState(246);
			((While_stmtContext)_localctx).while_suite = suite();
			setState(250);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__26) {
				{
				setState(247);
				match(T__26);
				setState(248);
				match(T__1);
				setState(249);
				((While_stmtContext)_localctx).else_suite = suite();
				}
			}

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

	public static class For_stmtContext extends ParserRuleContext {
		public ExprlistContext expr_list;
		public TestlistContext test_list;
		public SuiteContext for_suite;
		public SuiteContext else_suite;
		public ExprlistContext exprlist() {
			return getRuleContext(ExprlistContext.class,0);
		}
		public TestlistContext testlist() {
			return getRuleContext(TestlistContext.class,0);
		}
		public List<SuiteContext> suite() {
			return getRuleContexts(SuiteContext.class);
		}
		public SuiteContext suite(int i) {
			return getRuleContext(SuiteContext.class,i);
		}
		public For_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_stmt; }
	}

	public final For_stmtContext for_stmt() throws RecognitionException {
		For_stmtContext _localctx = new For_stmtContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_for_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(252);
			match(T__28);
			setState(253);
			((For_stmtContext)_localctx).expr_list = exprlist();
			setState(254);
			match(T__29);
			setState(255);
			((For_stmtContext)_localctx).test_list = testlist();
			setState(256);
			match(T__1);
			setState(257);
			((For_stmtContext)_localctx).for_suite = suite();
			setState(261);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__26) {
				{
				setState(258);
				match(T__26);
				setState(259);
				match(T__1);
				setState(260);
				((For_stmtContext)_localctx).else_suite = suite();
				}
			}

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

	public static class SuiteContext extends ParserRuleContext {
		public Simple_stmtContext simple_stmt() {
			return getRuleContext(Simple_stmtContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(TyptParser.NEWLINE, 0); }
		public TerminalNode INDENT() { return getToken(TyptParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(TyptParser.DEDENT, 0); }
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public SuiteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_suite; }
	}

	public final SuiteContext suite() throws RecognitionException {
		SuiteContext _localctx = new SuiteContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_suite);
		int _la;
		try {
			setState(273);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__19:
			case T__20:
			case T__21:
			case T__22:
			case T__23:
			case T__35:
			case T__41:
			case T__54:
			case T__55:
			case T__60:
			case T__62:
			case T__63:
			case T__64:
			case NUMBER:
			case STRING:
			case NAME:
				enterOuterAlt(_localctx, 1);
				{
				setState(263);
				simple_stmt();
				}
				break;
			case NEWLINE:
				enterOuterAlt(_localctx, 2);
				{
				setState(264);
				match(NEWLINE);
				setState(265);
				match(INDENT);
				setState(267); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(266);
					stmt();
					}
					}
					setState(269); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__19) | (1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << T__27) | (1L << T__28) | (1L << T__30) | (1L << T__35) | (1L << T__36) | (1L << T__41) | (1L << T__54) | (1L << T__55) | (1L << T__60) | (1L << T__62))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (T__63 - 64)) | (1L << (T__64 - 64)) | (1L << (NUMBER - 64)) | (1L << (STRING - 64)) | (1L << (NAME - 64)))) != 0) );
				setState(271);
				match(DEDENT);
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class Func_defContext extends ParserRuleContext {
		public Func_signatureContext func_signature() {
			return getRuleContext(Func_signatureContext.class,0);
		}
		public SuiteContext suite() {
			return getRuleContext(SuiteContext.class,0);
		}
		public Func_defContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_def; }
	}

	public final Func_defContext func_def() throws RecognitionException {
		Func_defContext _localctx = new Func_defContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_func_def);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(275);
			match(T__30);
			setState(276);
			func_signature();
			setState(277);
			match(T__1);
			setState(278);
			suite();
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

	public static class Func_signatureContext extends ParserRuleContext {
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public Typt_typeContext typt_type() {
			return getRuleContext(Typt_typeContext.class,0);
		}
		public Func_parameter_listContext func_parameter_list() {
			return getRuleContext(Func_parameter_listContext.class,0);
		}
		public Func_signatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_signature; }
	}

	public final Func_signatureContext func_signature() throws RecognitionException {
		Func_signatureContext _localctx = new Func_signatureContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_func_signature);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(280);
			name();
			setState(281);
			match(T__31);
			setState(283);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NAME) {
				{
				setState(282);
				func_parameter_list();
				}
			}

			setState(285);
			match(T__32);
			setState(286);
			match(T__33);
			setState(287);
			typt_type(0);
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

	public static class Func_parameter_listContext extends ParserRuleContext {
		public List<NameContext> name() {
			return getRuleContexts(NameContext.class);
		}
		public NameContext name(int i) {
			return getRuleContext(NameContext.class,i);
		}
		public List<Typt_typeContext> typt_type() {
			return getRuleContexts(Typt_typeContext.class);
		}
		public Typt_typeContext typt_type(int i) {
			return getRuleContext(Typt_typeContext.class,i);
		}
		public Func_parameter_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_parameter_list; }
	}

	public final Func_parameter_listContext func_parameter_list() throws RecognitionException {
		Func_parameter_listContext _localctx = new Func_parameter_listContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_func_parameter_list);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(289);
			name();
			setState(290);
			match(T__1);
			setState(291);
			typt_type(0);
			setState(299);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(292);
					match(T__4);
					setState(293);
					name();
					setState(294);
					match(T__1);
					setState(295);
					typt_type(0);
					}
					} 
				}
				setState(301);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			}
			setState(303);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(302);
				match(T__4);
				}
			}

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

	public static class Class_defContext extends ParserRuleContext {
		public Class_decContext class_dec() {
			return getRuleContext(Class_decContext.class,0);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(TyptParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(TyptParser.NEWLINE, i);
		}
		public TerminalNode INDENT() { return getToken(TyptParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(TyptParser.DEDENT, 0); }
		public List<NameContext> name() {
			return getRuleContexts(NameContext.class);
		}
		public NameContext name(int i) {
			return getRuleContext(NameContext.class,i);
		}
		public List<Typt_typeContext> typt_type() {
			return getRuleContexts(Typt_typeContext.class);
		}
		public Typt_typeContext typt_type(int i) {
			return getRuleContext(Typt_typeContext.class,i);
		}
		public SuiteContext suite() {
			return getRuleContext(SuiteContext.class,0);
		}
		public List<Class_methodContext> class_method() {
			return getRuleContexts(Class_methodContext.class);
		}
		public Class_methodContext class_method(int i) {
			return getRuleContext(Class_methodContext.class,i);
		}
		public List<Class_static_methodContext> class_static_method() {
			return getRuleContexts(Class_static_methodContext.class);
		}
		public Class_static_methodContext class_static_method(int i) {
			return getRuleContext(Class_static_methodContext.class,i);
		}
		public List<TestContext> test() {
			return getRuleContexts(TestContext.class);
		}
		public TestContext test(int i) {
			return getRuleContext(TestContext.class,i);
		}
		public Func_parameter_listContext func_parameter_list() {
			return getRuleContext(Func_parameter_listContext.class,0);
		}
		public Pass_stmtContext pass_stmt() {
			return getRuleContext(Pass_stmtContext.class,0);
		}
		public Class_defContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_def; }
	}

	public final Class_defContext class_def() throws RecognitionException {
		Class_defContext _localctx = new Class_defContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_class_def);
		int _la;
		try {
			setState(353);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(305);
				class_dec();
				setState(306);
				match(T__1);
				setState(307);
				match(NEWLINE);
				setState(308);
				match(INDENT);
				setState(320);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==NAME) {
					{
					{
					setState(309);
					name();
					setState(310);
					match(T__1);
					setState(311);
					typt_type(0);
					setState(314);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==T__5) {
						{
						setState(312);
						match(T__5);
						setState(313);
						test();
						}
					}

					setState(316);
					match(NEWLINE);
					}
					}
					setState(322);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(334);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
				case 1:
					{
					setState(323);
					match(T__30);
					setState(324);
					match(T__34);
					setState(325);
					match(T__31);
					setState(326);
					match(T__35);
					setState(329);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==T__4) {
						{
						setState(327);
						match(T__4);
						setState(328);
						func_parameter_list();
						}
					}

					setState(331);
					match(T__32);
					setState(332);
					match(T__1);
					setState(333);
					suite();
					}
					break;
				}
				setState(340);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__30 || _la==T__37) {
					{
					setState(338);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case T__30:
						{
						setState(336);
						class_method();
						}
						break;
					case T__37:
						{
						setState(337);
						class_static_method();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					setState(342);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(343);
				match(DEDENT);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(345);
				class_dec();
				setState(346);
				match(T__1);
				setState(347);
				match(NEWLINE);
				setState(348);
				match(INDENT);
				setState(349);
				pass_stmt();
				setState(350);
				match(NEWLINE);
				setState(351);
				match(DEDENT);
				}
				break;
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

	public static class Class_decContext extends ParserRuleContext {
		public List<NameContext> name() {
			return getRuleContexts(NameContext.class);
		}
		public NameContext name(int i) {
			return getRuleContext(NameContext.class,i);
		}
		public Class_decContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_dec; }
	}

	public final Class_decContext class_dec() throws RecognitionException {
		Class_decContext _localctx = new Class_decContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_class_dec);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(355);
			match(T__36);
			setState(356);
			name();
			setState(361);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__31) {
				{
				setState(357);
				match(T__31);
				setState(358);
				name();
				setState(359);
				match(T__32);
				}
			}

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

	public static class Class_methodContext extends ParserRuleContext {
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public Typt_typeContext typt_type() {
			return getRuleContext(Typt_typeContext.class,0);
		}
		public SuiteContext suite() {
			return getRuleContext(SuiteContext.class,0);
		}
		public Func_parameter_listContext func_parameter_list() {
			return getRuleContext(Func_parameter_listContext.class,0);
		}
		public Class_methodContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_method; }
	}

	public final Class_methodContext class_method() throws RecognitionException {
		Class_methodContext _localctx = new Class_methodContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_class_method);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(363);
			match(T__30);
			setState(364);
			name();
			setState(365);
			match(T__31);
			setState(366);
			match(T__35);
			setState(369);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(367);
				match(T__4);
				setState(368);
				func_parameter_list();
				}
			}

			setState(371);
			match(T__32);
			setState(372);
			match(T__33);
			setState(373);
			typt_type(0);
			setState(374);
			match(T__1);
			setState(375);
			suite();
			}
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

	public static class Class_static_methodContext extends ParserRuleContext {
		public TerminalNode NEWLINE() { return getToken(TyptParser.NEWLINE, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public Typt_typeContext typt_type() {
			return getRuleContext(Typt_typeContext.class,0);
		}
		public SuiteContext suite() {
			return getRuleContext(SuiteContext.class,0);
		}
		public Func_parameter_listContext func_parameter_list() {
			return getRuleContext(Func_parameter_listContext.class,0);
		}
		public Class_static_methodContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_static_method; }
	}

	public final Class_static_methodContext class_static_method() throws RecognitionException {
		Class_static_methodContext _localctx = new Class_static_methodContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_class_static_method);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(377);
			match(T__37);
			setState(378);
			match(T__38);
			setState(379);
			match(NEWLINE);
			{
			setState(380);
			match(T__30);
			setState(381);
			name();
			setState(382);
			match(T__31);
			setState(384);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NAME) {
				{
				setState(383);
				func_parameter_list();
				}
			}

			setState(386);
			match(T__32);
			setState(387);
			match(T__33);
			setState(388);
			typt_type(0);
			setState(389);
			match(T__1);
			setState(390);
			suite();
			}
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

	public static class TestContext extends ParserRuleContext {
		public Or_testContext or_test() {
			return getRuleContext(Or_testContext.class,0);
		}
		public TestContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_test; }
	}

	public final TestContext test() throws RecognitionException {
		TestContext _localctx = new TestContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_test);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(392);
			or_test();
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

	public static class Or_testContext extends ParserRuleContext {
		public And_testContext lhs;
		public Token op;
		public List<And_testContext> and_test() {
			return getRuleContexts(And_testContext.class);
		}
		public And_testContext and_test(int i) {
			return getRuleContext(And_testContext.class,i);
		}
		public Or_testContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_or_test; }
	}

	public final Or_testContext or_test() throws RecognitionException {
		Or_testContext _localctx = new Or_testContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_or_test);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(394);
			((Or_testContext)_localctx).lhs = and_test();
			setState(399);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__39) {
				{
				{
				setState(395);
				((Or_testContext)_localctx).op = match(T__39);
				setState(396);
				and_test();
				}
				}
				setState(401);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	public static class And_testContext extends ParserRuleContext {
		public Not_testContext lhs;
		public Token op;
		public List<Not_testContext> not_test() {
			return getRuleContexts(Not_testContext.class);
		}
		public Not_testContext not_test(int i) {
			return getRuleContext(Not_testContext.class,i);
		}
		public And_testContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_and_test; }
	}

	public final And_testContext and_test() throws RecognitionException {
		And_testContext _localctx = new And_testContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_and_test);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(402);
			((And_testContext)_localctx).lhs = not_test();
			setState(407);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__40) {
				{
				{
				setState(403);
				((And_testContext)_localctx).op = match(T__40);
				setState(404);
				not_test();
				}
				}
				setState(409);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	public static class Not_testContext extends ParserRuleContext {
		public Token op;
		public Not_testContext lhs;
		public Not_testContext not_test() {
			return getRuleContext(Not_testContext.class,0);
		}
		public ComparisonContext comparison() {
			return getRuleContext(ComparisonContext.class,0);
		}
		public Not_testContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_not_test; }
	}

	public final Not_testContext not_test() throws RecognitionException {
		Not_testContext _localctx = new Not_testContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_not_test);
		try {
			setState(413);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__41:
				enterOuterAlt(_localctx, 1);
				{
				setState(410);
				((Not_testContext)_localctx).op = match(T__41);
				setState(411);
				((Not_testContext)_localctx).lhs = not_test();
				}
				break;
			case T__35:
			case T__54:
			case T__55:
			case T__60:
			case T__62:
			case T__63:
			case T__64:
			case NUMBER:
			case STRING:
			case NAME:
				enterOuterAlt(_localctx, 2);
				{
				setState(412);
				comparison();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class ComparisonContext extends ParserRuleContext {
		public ExprContext lhs;
		public Comp_opContext op;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<Comp_opContext> comp_op() {
			return getRuleContexts(Comp_opContext.class);
		}
		public Comp_opContext comp_op(int i) {
			return getRuleContext(Comp_opContext.class,i);
		}
		public ComparisonContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison; }
	}

	public final ComparisonContext comparison() throws RecognitionException {
		ComparisonContext _localctx = new ComparisonContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_comparison);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(415);
			((ComparisonContext)_localctx).lhs = expr();
			setState(421);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__29) | (1L << T__41) | (1L << T__42) | (1L << T__43) | (1L << T__44) | (1L << T__45) | (1L << T__46) | (1L << T__47) | (1L << T__48))) != 0)) {
				{
				{
				setState(416);
				((ComparisonContext)_localctx).op = comp_op();
				setState(417);
				expr();
				}
				}
				setState(423);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	public static class Comp_opContext extends ParserRuleContext {
		public Comp_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comp_op; }
	}

	public final Comp_opContext comp_op() throws RecognitionException {
		Comp_opContext _localctx = new Comp_opContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_comp_op);
		try {
			setState(436);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,38,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(424);
				match(T__42);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(425);
				match(T__43);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(426);
				match(T__44);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(427);
				match(T__45);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(428);
				match(T__46);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(429);
				match(T__47);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(430);
				match(T__29);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(431);
				match(T__41);
				setState(432);
				match(T__29);
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(433);
				match(T__48);
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(434);
				match(T__48);
				setState(435);
				match(T__41);
				}
				break;
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

	public static class ExprContext extends ParserRuleContext {
		public Or_exprContext or_expr() {
			return getRuleContext(Or_exprContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(438);
			or_expr();
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

	public static class Or_exprContext extends ParserRuleContext {
		public Xor_exprContext lhs;
		public Token op;
		public List<Xor_exprContext> xor_expr() {
			return getRuleContexts(Xor_exprContext.class);
		}
		public Xor_exprContext xor_expr(int i) {
			return getRuleContext(Xor_exprContext.class,i);
		}
		public Or_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_or_expr; }
	}

	public final Or_exprContext or_expr() throws RecognitionException {
		Or_exprContext _localctx = new Or_exprContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_or_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(440);
			((Or_exprContext)_localctx).lhs = xor_expr();
			setState(445);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__49) {
				{
				{
				setState(441);
				((Or_exprContext)_localctx).op = match(T__49);
				setState(442);
				xor_expr();
				}
				}
				setState(447);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	public static class Xor_exprContext extends ParserRuleContext {
		public And_exprContext lhs;
		public Token op;
		public List<And_exprContext> and_expr() {
			return getRuleContexts(And_exprContext.class);
		}
		public And_exprContext and_expr(int i) {
			return getRuleContext(And_exprContext.class,i);
		}
		public Xor_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_xor_expr; }
	}

	public final Xor_exprContext xor_expr() throws RecognitionException {
		Xor_exprContext _localctx = new Xor_exprContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_xor_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(448);
			((Xor_exprContext)_localctx).lhs = and_expr();
			setState(453);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__50) {
				{
				{
				setState(449);
				((Xor_exprContext)_localctx).op = match(T__50);
				setState(450);
				and_expr();
				}
				}
				setState(455);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	public static class And_exprContext extends ParserRuleContext {
		public Shift_exprContext lhs;
		public Token op;
		public List<Shift_exprContext> shift_expr() {
			return getRuleContexts(Shift_exprContext.class);
		}
		public Shift_exprContext shift_expr(int i) {
			return getRuleContext(Shift_exprContext.class,i);
		}
		public And_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_and_expr; }
	}

	public final And_exprContext and_expr() throws RecognitionException {
		And_exprContext _localctx = new And_exprContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_and_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(456);
			((And_exprContext)_localctx).lhs = shift_expr();
			setState(461);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__51) {
				{
				{
				setState(457);
				((And_exprContext)_localctx).op = match(T__51);
				setState(458);
				shift_expr();
				}
				}
				setState(463);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	public static class Shift_exprContext extends ParserRuleContext {
		public Arith_exprContext lhs;
		public Shift_opContext op;
		public List<Arith_exprContext> arith_expr() {
			return getRuleContexts(Arith_exprContext.class);
		}
		public Arith_exprContext arith_expr(int i) {
			return getRuleContext(Arith_exprContext.class,i);
		}
		public List<Shift_opContext> shift_op() {
			return getRuleContexts(Shift_opContext.class);
		}
		public Shift_opContext shift_op(int i) {
			return getRuleContext(Shift_opContext.class,i);
		}
		public Shift_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shift_expr; }
	}

	public final Shift_exprContext shift_expr() throws RecognitionException {
		Shift_exprContext _localctx = new Shift_exprContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_shift_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(464);
			((Shift_exprContext)_localctx).lhs = arith_expr();
			setState(470);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__52 || _la==T__53) {
				{
				{
				setState(465);
				((Shift_exprContext)_localctx).op = shift_op();
				setState(466);
				arith_expr();
				}
				}
				setState(472);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	public static class Shift_opContext extends ParserRuleContext {
		public Shift_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shift_op; }
	}

	public final Shift_opContext shift_op() throws RecognitionException {
		Shift_opContext _localctx = new Shift_opContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_shift_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(473);
			_la = _input.LA(1);
			if ( !(_la==T__52 || _la==T__53) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class Arith_exprContext extends ParserRuleContext {
		public TermContext lhs;
		public Arith_opContext op;
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public List<Arith_opContext> arith_op() {
			return getRuleContexts(Arith_opContext.class);
		}
		public Arith_opContext arith_op(int i) {
			return getRuleContext(Arith_opContext.class,i);
		}
		public Arith_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arith_expr; }
	}

	public final Arith_exprContext arith_expr() throws RecognitionException {
		Arith_exprContext _localctx = new Arith_exprContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_arith_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(475);
			((Arith_exprContext)_localctx).lhs = term();
			setState(481);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__54 || _la==T__55) {
				{
				{
				setState(476);
				((Arith_exprContext)_localctx).op = arith_op();
				setState(477);
				term();
				}
				}
				setState(483);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	public static class Arith_opContext extends ParserRuleContext {
		public Arith_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arith_op; }
	}

	public final Arith_opContext arith_op() throws RecognitionException {
		Arith_opContext _localctx = new Arith_opContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_arith_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(484);
			_la = _input.LA(1);
			if ( !(_la==T__54 || _la==T__55) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class TermContext extends ParserRuleContext {
		public FactorContext lhs;
		public Term_opContext op;
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<Term_opContext> term_op() {
			return getRuleContexts(Term_opContext.class);
		}
		public Term_opContext term_op(int i) {
			return getRuleContext(Term_opContext.class,i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(486);
			((TermContext)_localctx).lhs = factor();
			setState(492);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__37) | (1L << T__56) | (1L << T__57) | (1L << T__58) | (1L << T__59))) != 0)) {
				{
				{
				setState(487);
				((TermContext)_localctx).op = term_op();
				setState(488);
				factor();
				}
				}
				setState(494);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	public static class Term_opContext extends ParserRuleContext {
		public Term_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term_op; }
	}

	public final Term_opContext term_op() throws RecognitionException {
		Term_opContext _localctx = new Term_opContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_term_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(495);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__37) | (1L << T__56) | (1L << T__57) | (1L << T__58) | (1L << T__59))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class FactorContext extends ParserRuleContext {
		public Factor_opContext op;
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public Factor_opContext factor_op() {
			return getRuleContext(Factor_opContext.class,0);
		}
		public PowerContext power() {
			return getRuleContext(PowerContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_factor);
		try {
			setState(501);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__54:
			case T__55:
			case T__60:
				enterOuterAlt(_localctx, 1);
				{
				setState(497);
				((FactorContext)_localctx).op = factor_op();
				setState(498);
				factor();
				}
				break;
			case T__35:
			case T__62:
			case T__63:
			case T__64:
			case NUMBER:
			case STRING:
			case NAME:
				enterOuterAlt(_localctx, 2);
				{
				setState(500);
				power();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class Factor_opContext extends ParserRuleContext {
		public Factor_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor_op; }
	}

	public final Factor_opContext factor_op() throws RecognitionException {
		Factor_opContext _localctx = new Factor_opContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_factor_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(503);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__54) | (1L << T__55) | (1L << T__60))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class PowerContext extends ParserRuleContext {
		public Atom_exprContext lhs;
		public Token op;
		public FactorContext rhs;
		public Atom_exprContext atom_expr() {
			return getRuleContext(Atom_exprContext.class,0);
		}
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public PowerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_power; }
	}

	public final PowerContext power() throws RecognitionException {
		PowerContext _localctx = new PowerContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_power);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(505);
			((PowerContext)_localctx).lhs = atom_expr();
			setState(508);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__61) {
				{
				setState(506);
				((PowerContext)_localctx).op = match(T__61);
				setState(507);
				((PowerContext)_localctx).rhs = factor();
				}
			}

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

	public static class Atom_exprContext extends ParserRuleContext {
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public List<TrailerContext> trailer() {
			return getRuleContexts(TrailerContext.class);
		}
		public TrailerContext trailer(int i) {
			return getRuleContext(TrailerContext.class,i);
		}
		public Atom_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom_expr; }
	}

	public final Atom_exprContext atom_expr() throws RecognitionException {
		Atom_exprContext _localctx = new Atom_exprContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_atom_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(510);
			atom();
			setState(514);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 32)) & ~0x3f) == 0 && ((1L << (_la - 32)) & ((1L << (T__31 - 32)) | (1L << (T__65 - 32)) | (1L << (T__67 - 32)))) != 0)) {
				{
				{
				setState(511);
				trailer();
				}
				}
				setState(516);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	public static class AtomContext extends ParserRuleContext {
		public Token string_literal;
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TerminalNode NUMBER() { return getToken(TyptParser.NUMBER, 0); }
		public TerminalNode STRING() { return getToken(TyptParser.STRING, 0); }
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_atom);
		try {
			setState(524);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NAME:
				enterOuterAlt(_localctx, 1);
				{
				setState(517);
				name();
				}
				break;
			case NUMBER:
				enterOuterAlt(_localctx, 2);
				{
				setState(518);
				match(NUMBER);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 3);
				{
				setState(519);
				((AtomContext)_localctx).string_literal = match(STRING);
				}
				break;
			case T__62:
				enterOuterAlt(_localctx, 4);
				{
				setState(520);
				match(T__62);
				}
				break;
			case T__63:
				enterOuterAlt(_localctx, 5);
				{
				setState(521);
				match(T__63);
				}
				break;
			case T__64:
				enterOuterAlt(_localctx, 6);
				{
				setState(522);
				match(T__64);
				}
				break;
			case T__35:
				enterOuterAlt(_localctx, 7);
				{
				setState(523);
				match(T__35);
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class TrailerContext extends ParserRuleContext {
		public Argument_listContext argument_list() {
			return getRuleContext(Argument_listContext.class,0);
		}
		public SubscriptlistContext subscriptlist() {
			return getRuleContext(SubscriptlistContext.class,0);
		}
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TrailerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_trailer; }
	}

	public final TrailerContext trailer() throws RecognitionException {
		TrailerContext _localctx = new TrailerContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_trailer);
		int _la;
		try {
			setState(537);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__31:
				enterOuterAlt(_localctx, 1);
				{
				setState(526);
				match(T__31);
				setState(528);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 36)) & ~0x3f) == 0 && ((1L << (_la - 36)) & ((1L << (T__35 - 36)) | (1L << (T__41 - 36)) | (1L << (T__54 - 36)) | (1L << (T__55 - 36)) | (1L << (T__60 - 36)) | (1L << (T__62 - 36)) | (1L << (T__63 - 36)) | (1L << (T__64 - 36)) | (1L << (NUMBER - 36)) | (1L << (STRING - 36)) | (1L << (NAME - 36)))) != 0)) {
					{
					setState(527);
					argument_list();
					}
				}

				setState(530);
				match(T__32);
				}
				break;
			case T__65:
				enterOuterAlt(_localctx, 2);
				{
				setState(531);
				match(T__65);
				setState(532);
				subscriptlist();
				setState(533);
				match(T__66);
				}
				break;
			case T__67:
				enterOuterAlt(_localctx, 3);
				{
				setState(535);
				match(T__67);
				setState(536);
				name();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class SubscriptlistContext extends ParserRuleContext {
		public List<SubscriptContext> subscript() {
			return getRuleContexts(SubscriptContext.class);
		}
		public SubscriptContext subscript(int i) {
			return getRuleContext(SubscriptContext.class,i);
		}
		public SubscriptlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subscriptlist; }
	}

	public final SubscriptlistContext subscriptlist() throws RecognitionException {
		SubscriptlistContext _localctx = new SubscriptlistContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_subscriptlist);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(539);
			subscript();
			setState(544);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,51,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(540);
					match(T__4);
					setState(541);
					subscript();
					}
					} 
				}
				setState(546);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,51,_ctx);
			}
			setState(548);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(547);
				match(T__4);
				}
			}

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

	public static class SubscriptContext extends ParserRuleContext {
		public List<TestContext> test() {
			return getRuleContexts(TestContext.class);
		}
		public TestContext test(int i) {
			return getRuleContext(TestContext.class,i);
		}
		public SliceopContext sliceop() {
			return getRuleContext(SliceopContext.class,0);
		}
		public SubscriptContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subscript; }
	}

	public final SubscriptContext subscript() throws RecognitionException {
		SubscriptContext _localctx = new SubscriptContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_subscript);
		int _la;
		try {
			setState(561);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,56,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(550);
				test();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(552);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 36)) & ~0x3f) == 0 && ((1L << (_la - 36)) & ((1L << (T__35 - 36)) | (1L << (T__41 - 36)) | (1L << (T__54 - 36)) | (1L << (T__55 - 36)) | (1L << (T__60 - 36)) | (1L << (T__62 - 36)) | (1L << (T__63 - 36)) | (1L << (T__64 - 36)) | (1L << (NUMBER - 36)) | (1L << (STRING - 36)) | (1L << (NAME - 36)))) != 0)) {
					{
					setState(551);
					test();
					}
				}

				setState(554);
				match(T__1);
				setState(556);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 36)) & ~0x3f) == 0 && ((1L << (_la - 36)) & ((1L << (T__35 - 36)) | (1L << (T__41 - 36)) | (1L << (T__54 - 36)) | (1L << (T__55 - 36)) | (1L << (T__60 - 36)) | (1L << (T__62 - 36)) | (1L << (T__63 - 36)) | (1L << (T__64 - 36)) | (1L << (NUMBER - 36)) | (1L << (STRING - 36)) | (1L << (NAME - 36)))) != 0)) {
					{
					setState(555);
					test();
					}
				}

				setState(559);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__1) {
					{
					setState(558);
					sliceop();
					}
				}

				}
				break;
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

	public static class SliceopContext extends ParserRuleContext {
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public SliceopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sliceop; }
	}

	public final SliceopContext sliceop() throws RecognitionException {
		SliceopContext _localctx = new SliceopContext(_ctx, getState());
		enterRule(_localctx, 106, RULE_sliceop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(563);
			match(T__1);
			setState(565);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 36)) & ~0x3f) == 0 && ((1L << (_la - 36)) & ((1L << (T__35 - 36)) | (1L << (T__41 - 36)) | (1L << (T__54 - 36)) | (1L << (T__55 - 36)) | (1L << (T__60 - 36)) | (1L << (T__62 - 36)) | (1L << (T__63 - 36)) | (1L << (T__64 - 36)) | (1L << (NUMBER - 36)) | (1L << (STRING - 36)) | (1L << (NAME - 36)))) != 0)) {
				{
				setState(564);
				test();
				}
			}

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

	public static class ExprlistContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ExprlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprlist; }
	}

	public final ExprlistContext exprlist() throws RecognitionException {
		ExprlistContext _localctx = new ExprlistContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_exprlist);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(567);
			expr();
			setState(572);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,58,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(568);
					match(T__4);
					setState(569);
					expr();
					}
					} 
				}
				setState(574);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,58,_ctx);
			}
			setState(576);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(575);
				match(T__4);
				}
			}

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

	public static class TestlistContext extends ParserRuleContext {
		public List<TestContext> test() {
			return getRuleContexts(TestContext.class);
		}
		public TestContext test(int i) {
			return getRuleContext(TestContext.class,i);
		}
		public TestlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_testlist; }
	}

	public final TestlistContext testlist() throws RecognitionException {
		TestlistContext _localctx = new TestlistContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_testlist);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(578);
			test();
			setState(583);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,60,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(579);
					match(T__4);
					setState(580);
					test();
					}
					} 
				}
				setState(585);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,60,_ctx);
			}
			setState(587);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(586);
				match(T__4);
				}
			}

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

	public static class NameContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(TyptParser.NAME, 0); }
		public NameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_name; }
	}

	public final NameContext name() throws RecognitionException {
		NameContext _localctx = new NameContext(_ctx, getState());
		enterRule(_localctx, 112, RULE_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(589);
			match(NAME);
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

	public static class Typt_typeContext extends ParserRuleContext {
		public Token none_type;
		public Token bool_type;
		public Token int_type;
		public Token float_type;
		public Token string_type;
		public Token object_base_type;
		public Token object_type;
		public Token function_type;
		public Typt_typeContext return_type;
		public Token list_type;
		public Typt_typeContext element_type;
		public Token tuple_type;
		public Token set_type;
		public Token dict_type;
		public Typt_typeContext key_type;
		public Typt_typeContext value_type;
		public List<NameContext> name() {
			return getRuleContexts(NameContext.class);
		}
		public NameContext name(int i) {
			return getRuleContext(NameContext.class,i);
		}
		public List<Typt_typeContext> typt_type() {
			return getRuleContexts(Typt_typeContext.class);
		}
		public Typt_typeContext typt_type(int i) {
			return getRuleContext(Typt_typeContext.class,i);
		}
		public Typt_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typt_type; }
	}

	public final Typt_typeContext typt_type() throws RecognitionException {
		return typt_type(0);
	}

	private Typt_typeContext typt_type(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Typt_typeContext _localctx = new Typt_typeContext(_ctx, _parentState);
		Typt_typeContext _prevctx = _localctx;
		int _startState = 114;
		enterRecursionRule(_localctx, 114, RULE_typt_type, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(659);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,66,_ctx) ) {
			case 1:
				{
				setState(592);
				((Typt_typeContext)_localctx).none_type = match(T__62);
				}
				break;
			case 2:
				{
				setState(593);
				((Typt_typeContext)_localctx).bool_type = match(T__68);
				}
				break;
			case 3:
				{
				setState(594);
				((Typt_typeContext)_localctx).int_type = match(T__69);
				}
				break;
			case 4:
				{
				setState(595);
				((Typt_typeContext)_localctx).float_type = match(T__70);
				}
				break;
			case 5:
				{
				setState(596);
				((Typt_typeContext)_localctx).string_type = match(T__71);
				}
				break;
			case 6:
				{
				setState(597);
				((Typt_typeContext)_localctx).object_base_type = match(T__72);
				}
				break;
			case 7:
				{
				setState(598);
				((Typt_typeContext)_localctx).object_type = match(T__72);
				setState(599);
				match(T__73);
				{
				setState(600);
				name();
				setState(601);
				match(T__1);
				setState(602);
				typt_type(0);
				}
				setState(611);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__4) {
					{
					{
					setState(604);
					match(T__4);
					setState(605);
					name();
					setState(606);
					match(T__1);
					setState(607);
					typt_type(0);
					}
					}
					setState(613);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(614);
				match(T__74);
				}
				break;
			case 8:
				{
				setState(616);
				match(T__42);
				setState(617);
				typt_type(0);
				setState(622);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__4) {
					{
					{
					setState(618);
					match(T__4);
					setState(619);
					typt_type(0);
					}
					}
					setState(624);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(625);
				match(T__43);
				setState(626);
				((Typt_typeContext)_localctx).function_type = match(T__33);
				setState(627);
				((Typt_typeContext)_localctx).return_type = typt_type(5);
				}
				break;
			case 9:
				{
				setState(629);
				((Typt_typeContext)_localctx).list_type = match(T__75);
				setState(630);
				match(T__65);
				setState(631);
				((Typt_typeContext)_localctx).element_type = typt_type(0);
				setState(632);
				match(T__66);
				}
				break;
			case 10:
				{
				setState(634);
				((Typt_typeContext)_localctx).tuple_type = match(T__76);
				setState(635);
				match(T__31);
				setState(644);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 43)) & ~0x3f) == 0 && ((1L << (_la - 43)) & ((1L << (T__42 - 43)) | (1L << (T__62 - 43)) | (1L << (T__68 - 43)) | (1L << (T__69 - 43)) | (1L << (T__70 - 43)) | (1L << (T__71 - 43)) | (1L << (T__72 - 43)) | (1L << (T__75 - 43)) | (1L << (T__76 - 43)) | (1L << (T__77 - 43)) | (1L << (T__78 - 43)))) != 0)) {
					{
					setState(636);
					typt_type(0);
					setState(641);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__4) {
						{
						{
						setState(637);
						match(T__4);
						setState(638);
						typt_type(0);
						}
						}
						setState(643);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(646);
				match(T__32);
				}
				break;
			case 11:
				{
				setState(647);
				((Typt_typeContext)_localctx).set_type = match(T__77);
				setState(648);
				match(T__31);
				setState(649);
				((Typt_typeContext)_localctx).element_type = typt_type(0);
				setState(650);
				match(T__32);
				}
				break;
			case 12:
				{
				setState(652);
				((Typt_typeContext)_localctx).dict_type = match(T__78);
				setState(653);
				match(T__73);
				setState(654);
				((Typt_typeContext)_localctx).key_type = typt_type(0);
				setState(655);
				match(T__4);
				setState(656);
				((Typt_typeContext)_localctx).value_type = typt_type(0);
				setState(657);
				match(T__74);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(666);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,67,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Typt_typeContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_typt_type);
					setState(661);
					if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
					setState(662);
					((Typt_typeContext)_localctx).function_type = match(T__33);
					setState(663);
					((Typt_typeContext)_localctx).return_type = typt_type(7);
					}
					} 
				}
				setState(668);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,67,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 57:
			return typt_type_sempred((Typt_typeContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean typt_type_sempred(Typt_typeContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 6);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3`\u02a0\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\3\2\3\2\7\2"+
		"y\n\2\f\2\16\2|\13\2\3\2\3\2\7\2\u0080\n\2\f\2\16\2\u0083\13\2\3\2\3\2"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\6\3\u008e\n\3\r\3\16\3\u008f\3\3\3\3\3\3"+
		"\3\3\3\3\5\3\u0097\n\3\3\4\3\4\5\4\u009b\n\4\3\5\3\5\3\5\7\5\u00a0\n\5"+
		"\f\5\16\5\u00a3\13\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\5\b\u00af"+
		"\n\b\3\t\3\t\3\t\5\t\u00b4\n\t\3\t\3\t\5\t\u00b8\n\t\3\n\3\n\3\13\3\13"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00c8\n\f\3\r\3\r\3\r\3\16"+
		"\3\16\3\17\3\17\3\17\5\17\u00d2\n\17\3\20\3\20\3\21\3\21\3\22\3\22\5\22"+
		"\u00da\n\22\3\23\3\23\3\23\3\23\3\23\5\23\u00e1\n\23\3\24\3\24\3\24\3"+
		"\24\3\24\3\24\3\24\3\24\3\24\7\24\u00ec\n\24\f\24\16\24\u00ef\13\24\3"+
		"\24\3\24\3\24\5\24\u00f4\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25"+
		"\u00fd\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0108\n"+
		"\26\3\27\3\27\3\27\3\27\6\27\u010e\n\27\r\27\16\27\u010f\3\27\3\27\5\27"+
		"\u0114\n\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\5\31\u011e\n\31\3"+
		"\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u012c"+
		"\n\32\f\32\16\32\u012f\13\32\3\32\5\32\u0132\n\32\3\33\3\33\3\33\3\33"+
		"\3\33\3\33\3\33\3\33\3\33\5\33\u013d\n\33\3\33\3\33\7\33\u0141\n\33\f"+
		"\33\16\33\u0144\13\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u014c\n\33\3"+
		"\33\3\33\3\33\5\33\u0151\n\33\3\33\3\33\7\33\u0155\n\33\f\33\16\33\u0158"+
		"\13\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0164\n"+
		"\33\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u016c\n\34\3\35\3\35\3\35\3\35"+
		"\3\35\3\35\5\35\u0174\n\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36"+
		"\3\36\3\36\3\36\3\36\5\36\u0183\n\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37"+
		"\3\37\3 \3 \3 \7 \u0190\n \f \16 \u0193\13 \3!\3!\3!\7!\u0198\n!\f!\16"+
		"!\u019b\13!\3\"\3\"\3\"\5\"\u01a0\n\"\3#\3#\3#\3#\7#\u01a6\n#\f#\16#\u01a9"+
		"\13#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u01b7\n$\3%\3%\3&\3&\3&\7"+
		"&\u01be\n&\f&\16&\u01c1\13&\3\'\3\'\3\'\7\'\u01c6\n\'\f\'\16\'\u01c9\13"+
		"\'\3(\3(\3(\7(\u01ce\n(\f(\16(\u01d1\13(\3)\3)\3)\3)\7)\u01d7\n)\f)\16"+
		")\u01da\13)\3*\3*\3+\3+\3+\3+\7+\u01e2\n+\f+\16+\u01e5\13+\3,\3,\3-\3"+
		"-\3-\3-\7-\u01ed\n-\f-\16-\u01f0\13-\3.\3.\3/\3/\3/\3/\5/\u01f8\n/\3\60"+
		"\3\60\3\61\3\61\3\61\5\61\u01ff\n\61\3\62\3\62\7\62\u0203\n\62\f\62\16"+
		"\62\u0206\13\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u020f\n\63\3\64"+
		"\3\64\5\64\u0213\n\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u021c\n"+
		"\64\3\65\3\65\3\65\7\65\u0221\n\65\f\65\16\65\u0224\13\65\3\65\5\65\u0227"+
		"\n\65\3\66\3\66\5\66\u022b\n\66\3\66\3\66\5\66\u022f\n\66\3\66\5\66\u0232"+
		"\n\66\5\66\u0234\n\66\3\67\3\67\5\67\u0238\n\67\38\38\38\78\u023d\n8\f"+
		"8\168\u0240\138\38\58\u0243\n8\39\39\39\79\u0248\n9\f9\169\u024b\139\3"+
		"9\59\u024e\n9\3:\3:\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3"+
		";\3;\7;\u0264\n;\f;\16;\u0267\13;\3;\3;\3;\3;\3;\3;\7;\u026f\n;\f;\16"+
		";\u0272\13;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\7;\u0282\n;\f;\16"+
		";\u0285\13;\5;\u0287\n;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\5;\u0296"+
		"\n;\3;\3;\3;\7;\u029b\n;\f;\16;\u029e\13;\3;\2\3t<\2\4\6\b\n\f\16\20\22"+
		"\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnp"+
		"rt\2\7\3\2\t\25\3\2\678\3\29:\4\2((;>\4\29:??\2\u02c8\2z\3\2\2\2\4\u0086"+
		"\3\2\2\2\6\u009a\3\2\2\2\b\u009c\3\2\2\2\n\u00a4\3\2\2\2\f\u00a6\3\2\2"+
		"\2\16\u00ae\3\2\2\2\20\u00b0\3\2\2\2\22\u00b9\3\2\2\2\24\u00bb\3\2\2\2"+
		"\26\u00c7\3\2\2\2\30\u00c9\3\2\2\2\32\u00cc\3\2\2\2\34\u00d1\3\2\2\2\36"+
		"\u00d3\3\2\2\2 \u00d5\3\2\2\2\"\u00d7\3\2\2\2$\u00e0\3\2\2\2&\u00e2\3"+
		"\2\2\2(\u00f5\3\2\2\2*\u00fe\3\2\2\2,\u0113\3\2\2\2.\u0115\3\2\2\2\60"+
		"\u011a\3\2\2\2\62\u0123\3\2\2\2\64\u0163\3\2\2\2\66\u0165\3\2\2\28\u016d"+
		"\3\2\2\2:\u017b\3\2\2\2<\u018a\3\2\2\2>\u018c\3\2\2\2@\u0194\3\2\2\2B"+
		"\u019f\3\2\2\2D\u01a1\3\2\2\2F\u01b6\3\2\2\2H\u01b8\3\2\2\2J\u01ba\3\2"+
		"\2\2L\u01c2\3\2\2\2N\u01ca\3\2\2\2P\u01d2\3\2\2\2R\u01db\3\2\2\2T\u01dd"+
		"\3\2\2\2V\u01e6\3\2\2\2X\u01e8\3\2\2\2Z\u01f1\3\2\2\2\\\u01f7\3\2\2\2"+
		"^\u01f9\3\2\2\2`\u01fb\3\2\2\2b\u0200\3\2\2\2d\u020e\3\2\2\2f\u021b\3"+
		"\2\2\2h\u021d\3\2\2\2j\u0233\3\2\2\2l\u0235\3\2\2\2n\u0239\3\2\2\2p\u0244"+
		"\3\2\2\2r\u024f\3\2\2\2t\u0295\3\2\2\2vy\7V\2\2wy\5\4\3\2xv\3\2\2\2xw"+
		"\3\2\2\2y|\3\2\2\2zx\3\2\2\2z{\3\2\2\2{\u0081\3\2\2\2|z\3\2\2\2}\u0080"+
		"\7V\2\2~\u0080\5\6\4\2\177}\3\2\2\2\177~\3\2\2\2\u0080\u0083\3\2\2\2\u0081"+
		"\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0084\3\2\2\2\u0083\u0081\3\2\2"+
		"\2\u0084\u0085\7\2\2\3\u0085\3\3\2\2\2\u0086\u0087\7\3\2\2\u0087\u0088"+
		"\7\4\2\2\u0088\u0089\7V\2\2\u0089\u008d\7_\2\2\u008a\u008b\5\60\31\2\u008b"+
		"\u008c\7V\2\2\u008c\u008e\3\2\2\2\u008d\u008a\3\2\2\2\u008e\u008f\3\2"+
		"\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0091\3\2\2\2\u0091"+
		"\u0092\7`\2\2\u0092\u0093\7\5\2\2\u0093\u0096\5r:\2\u0094\u0095\7\6\2"+
		"\2\u0095\u0097\5r:\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\5\3"+
		"\2\2\2\u0098\u009b\5\f\7\2\u0099\u009b\5$\23\2\u009a\u0098\3\2\2\2\u009a"+
		"\u0099\3\2\2\2\u009b\7\3\2\2\2\u009c\u00a1\5\n\6\2\u009d\u009e\7\7\2\2"+
		"\u009e\u00a0\5\n\6\2\u009f\u009d\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u009f"+
		"\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\t\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4"+
		"\u00a5\5<\37\2\u00a5\13\3\2\2\2\u00a6\u00a7\5\16\b\2\u00a7\u00a8\7V\2"+
		"\2\u00a8\r\3\2\2\2\u00a9\u00af\5\20\t\2\u00aa\u00af\5\26\f\2\u00ab\u00af"+
		"\5\30\r\2\u00ac\u00af\5\32\16\2\u00ad\u00af\5\34\17\2\u00ae\u00a9\3\2"+
		"\2\2\u00ae\u00aa\3\2\2\2\u00ae\u00ab\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae"+
		"\u00ad\3\2\2\2\u00af\17\3\2\2\2\u00b0\u00b7\5<\37\2\u00b1\u00b4\5\22\n"+
		"\2\u00b2\u00b4\5\24\13\2\u00b3\u00b1\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4"+
		"\u00b5\3\2\2\2\u00b5\u00b6\5<\37\2\u00b6\u00b8\3\2\2\2\u00b7\u00b3\3\2"+
		"\2\2\u00b7\u00b8\3\2\2\2\u00b8\21\3\2\2\2\u00b9\u00ba\7\b\2\2\u00ba\23"+
		"\3\2\2\2\u00bb\u00bc\t\2\2\2\u00bc\25\3\2\2\2\u00bd\u00be\5r:\2\u00be"+
		"\u00bf\7\4\2\2\u00bf\u00c0\5t;\2\u00c0\u00c8\3\2\2\2\u00c1\u00c2\5r:\2"+
		"\u00c2\u00c3\7\4\2\2\u00c3\u00c4\5t;\2\u00c4\u00c5\7\b\2\2\u00c5\u00c6"+
		"\5<\37\2\u00c6\u00c8\3\2\2\2\u00c7\u00bd\3\2\2\2\u00c7\u00c1\3\2\2\2\u00c8"+
		"\27\3\2\2\2\u00c9\u00ca\7\26\2\2\u00ca\u00cb\5n8\2\u00cb\31\3\2\2\2\u00cc"+
		"\u00cd\7\27\2\2\u00cd\33\3\2\2\2\u00ce\u00d2\5\36\20\2\u00cf\u00d2\5 "+
		"\21\2\u00d0\u00d2\5\"\22\2\u00d1\u00ce\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1"+
		"\u00d0\3\2\2\2\u00d2\35\3\2\2\2\u00d3\u00d4\7\30\2\2\u00d4\37\3\2\2\2"+
		"\u00d5\u00d6\7\31\2\2\u00d6!\3\2\2\2\u00d7\u00d9\7\32\2\2\u00d8\u00da"+
		"\5<\37\2\u00d9\u00d8\3\2\2\2\u00d9\u00da\3\2\2\2\u00da#\3\2\2\2\u00db"+
		"\u00e1\5&\24\2\u00dc\u00e1\5(\25\2\u00dd\u00e1\5*\26\2\u00de\u00e1\5."+
		"\30\2\u00df\u00e1\5\64\33\2\u00e0\u00db\3\2\2\2\u00e0\u00dc\3\2\2\2\u00e0"+
		"\u00dd\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00df\3\2\2\2\u00e1%\3\2\2\2"+
		"\u00e2\u00e3\7\33\2\2\u00e3\u00e4\5<\37\2\u00e4\u00e5\7\4\2\2\u00e5\u00ed"+
		"\5,\27\2\u00e6\u00e7\7\34\2\2\u00e7\u00e8\5<\37\2\u00e8\u00e9\7\4\2\2"+
		"\u00e9\u00ea\5,\27\2\u00ea\u00ec\3\2\2\2\u00eb\u00e6\3\2\2\2\u00ec\u00ef"+
		"\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00f3\3\2\2\2\u00ef"+
		"\u00ed\3\2\2\2\u00f0\u00f1\7\35\2\2\u00f1\u00f2\7\4\2\2\u00f2\u00f4\5"+
		",\27\2\u00f3\u00f0\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\'\3\2\2\2\u00f5\u00f6"+
		"\7\36\2\2\u00f6\u00f7\5<\37\2\u00f7\u00f8\7\4\2\2\u00f8\u00fc\5,\27\2"+
		"\u00f9\u00fa\7\35\2\2\u00fa\u00fb\7\4\2\2\u00fb\u00fd\5,\27\2\u00fc\u00f9"+
		"\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd)\3\2\2\2\u00fe\u00ff\7\37\2\2\u00ff"+
		"\u0100\5n8\2\u0100\u0101\7 \2\2\u0101\u0102\5p9\2\u0102\u0103\7\4\2\2"+
		"\u0103\u0107\5,\27\2\u0104\u0105\7\35\2\2\u0105\u0106\7\4\2\2\u0106\u0108"+
		"\5,\27\2\u0107\u0104\3\2\2\2\u0107\u0108\3\2\2\2\u0108+\3\2\2\2\u0109"+
		"\u0114\5\f\7\2\u010a\u010b\7V\2\2\u010b\u010d\7_\2\2\u010c\u010e\5\6\4"+
		"\2\u010d\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110"+
		"\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0112\7`\2\2\u0112\u0114\3\2\2\2\u0113"+
		"\u0109\3\2\2\2\u0113\u010a\3\2\2\2\u0114-\3\2\2\2\u0115\u0116\7!\2\2\u0116"+
		"\u0117\5\60\31\2\u0117\u0118\7\4\2\2\u0118\u0119\5,\27\2\u0119/\3\2\2"+
		"\2\u011a\u011b\5r:\2\u011b\u011d\7\"\2\2\u011c\u011e\5\62\32\2\u011d\u011c"+
		"\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0120\7#\2\2\u0120"+
		"\u0121\7$\2\2\u0121\u0122\5t;\2\u0122\61\3\2\2\2\u0123\u0124\5r:\2\u0124"+
		"\u0125\7\4\2\2\u0125\u012d\5t;\2\u0126\u0127\7\7\2\2\u0127\u0128\5r:\2"+
		"\u0128\u0129\7\4\2\2\u0129\u012a\5t;\2\u012a\u012c\3\2\2\2\u012b\u0126"+
		"\3\2\2\2\u012c\u012f\3\2\2\2\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e"+
		"\u0131\3\2\2\2\u012f\u012d\3\2\2\2\u0130\u0132\7\7\2\2\u0131\u0130\3\2"+
		"\2\2\u0131\u0132\3\2\2\2\u0132\63\3\2\2\2\u0133\u0134\5\66\34\2\u0134"+
		"\u0135\7\4\2\2\u0135\u0136\7V\2\2\u0136\u0142\7_\2\2\u0137\u0138\5r:\2"+
		"\u0138\u0139\7\4\2\2\u0139\u013c\5t;\2\u013a\u013b\7\b\2\2\u013b\u013d"+
		"\5<\37\2\u013c\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013e\3\2\2\2\u013e"+
		"\u013f\7V\2\2\u013f\u0141\3\2\2\2\u0140\u0137\3\2\2\2\u0141\u0144\3\2"+
		"\2\2\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0150\3\2\2\2\u0144"+
		"\u0142\3\2\2\2\u0145\u0146\7!\2\2\u0146\u0147\7%\2\2\u0147\u0148\7\"\2"+
		"\2\u0148\u014b\7&\2\2\u0149\u014a\7\7\2\2\u014a\u014c\5\62\32\2\u014b"+
		"\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014e\7#"+
		"\2\2\u014e\u014f\7\4\2\2\u014f\u0151\5,\27\2\u0150\u0145\3\2\2\2\u0150"+
		"\u0151\3\2\2\2\u0151\u0156\3\2\2\2\u0152\u0155\58\35\2\u0153\u0155\5:"+
		"\36\2\u0154\u0152\3\2\2\2\u0154\u0153\3\2\2\2\u0155\u0158\3\2\2\2\u0156"+
		"\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0159\3\2\2\2\u0158\u0156\3\2"+
		"\2\2\u0159\u015a\7`\2\2\u015a\u0164\3\2\2\2\u015b\u015c\5\66\34\2\u015c"+
		"\u015d\7\4\2\2\u015d\u015e\7V\2\2\u015e\u015f\7_\2\2\u015f\u0160\5\32"+
		"\16\2\u0160\u0161\7V\2\2\u0161\u0162\7`\2\2\u0162\u0164\3\2\2\2\u0163"+
		"\u0133\3\2\2\2\u0163\u015b\3\2\2\2\u0164\65\3\2\2\2\u0165\u0166\7\'\2"+
		"\2\u0166\u016b\5r:\2\u0167\u0168\7\"\2\2\u0168\u0169\5r:\2\u0169\u016a"+
		"\7#\2\2\u016a\u016c\3\2\2\2\u016b\u0167\3\2\2\2\u016b\u016c\3\2\2\2\u016c"+
		"\67\3\2\2\2\u016d\u016e\7!\2\2\u016e\u016f\5r:\2\u016f\u0170\7\"\2\2\u0170"+
		"\u0173\7&\2\2\u0171\u0172\7\7\2\2\u0172\u0174\5\62\32\2\u0173\u0171\3"+
		"\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176\7#\2\2\u0176"+
		"\u0177\7$\2\2\u0177\u0178\5t;\2\u0178\u0179\7\4\2\2\u0179\u017a\5,\27"+
		"\2\u017a9\3\2\2\2\u017b\u017c\7(\2\2\u017c\u017d\7)\2\2\u017d\u017e\7"+
		"V\2\2\u017e\u017f\7!\2\2\u017f\u0180\5r:\2\u0180\u0182\7\"\2\2\u0181\u0183"+
		"\5\62\32\2\u0182\u0181\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184\3\2\2\2"+
		"\u0184\u0185\7#\2\2\u0185\u0186\7$\2\2\u0186\u0187\5t;\2\u0187\u0188\7"+
		"\4\2\2\u0188\u0189\5,\27\2\u0189;\3\2\2\2\u018a\u018b\5> \2\u018b=\3\2"+
		"\2\2\u018c\u0191\5@!\2\u018d\u018e\7*\2\2\u018e\u0190\5@!\2\u018f\u018d"+
		"\3\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192"+
		"?\3\2\2\2\u0193\u0191\3\2\2\2\u0194\u0199\5B\"\2\u0195\u0196\7+\2\2\u0196"+
		"\u0198\5B\"\2\u0197\u0195\3\2\2\2\u0198\u019b\3\2\2\2\u0199\u0197\3\2"+
		"\2\2\u0199\u019a\3\2\2\2\u019aA\3\2\2\2\u019b\u0199\3\2\2\2\u019c\u019d"+
		"\7,\2\2\u019d\u01a0\5B\"\2\u019e\u01a0\5D#\2\u019f\u019c\3\2\2\2\u019f"+
		"\u019e\3\2\2\2\u01a0C\3\2\2\2\u01a1\u01a7\5H%\2\u01a2\u01a3\5F$\2\u01a3"+
		"\u01a4\5H%\2\u01a4\u01a6\3\2\2\2\u01a5\u01a2\3\2\2\2\u01a6\u01a9\3\2\2"+
		"\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8E\3\2\2\2\u01a9\u01a7"+
		"\3\2\2\2\u01aa\u01b7\7-\2\2\u01ab\u01b7\7.\2\2\u01ac\u01b7\7/\2\2\u01ad"+
		"\u01b7\7\60\2\2\u01ae\u01b7\7\61\2\2\u01af\u01b7\7\62\2\2\u01b0\u01b7"+
		"\7 \2\2\u01b1\u01b2\7,\2\2\u01b2\u01b7\7 \2\2\u01b3\u01b7\7\63\2\2\u01b4"+
		"\u01b5\7\63\2\2\u01b5\u01b7\7,\2\2\u01b6\u01aa\3\2\2\2\u01b6\u01ab\3\2"+
		"\2\2\u01b6\u01ac\3\2\2\2\u01b6\u01ad\3\2\2\2\u01b6\u01ae\3\2\2\2\u01b6"+
		"\u01af\3\2\2\2\u01b6\u01b0\3\2\2\2\u01b6\u01b1\3\2\2\2\u01b6\u01b3\3\2"+
		"\2\2\u01b6\u01b4\3\2\2\2\u01b7G\3\2\2\2\u01b8\u01b9\5J&\2\u01b9I\3\2\2"+
		"\2\u01ba\u01bf\5L\'\2\u01bb\u01bc\7\64\2\2\u01bc\u01be\5L\'\2\u01bd\u01bb"+
		"\3\2\2\2\u01be\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0"+
		"K\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c7\5N(\2\u01c3\u01c4\7\65\2\2\u01c4"+
		"\u01c6\5N(\2\u01c5\u01c3\3\2\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3\2\2"+
		"\2\u01c7\u01c8\3\2\2\2\u01c8M\3\2\2\2\u01c9\u01c7\3\2\2\2\u01ca\u01cf"+
		"\5P)\2\u01cb\u01cc\7\66\2\2\u01cc\u01ce\5P)\2\u01cd\u01cb\3\2\2\2\u01ce"+
		"\u01d1\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0O\3\2\2\2"+
		"\u01d1\u01cf\3\2\2\2\u01d2\u01d8\5T+\2\u01d3\u01d4\5R*\2\u01d4\u01d5\5"+
		"T+\2\u01d5\u01d7\3\2\2\2\u01d6\u01d3\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8"+
		"\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9Q\3\2\2\2\u01da\u01d8\3\2\2\2"+
		"\u01db\u01dc\t\3\2\2\u01dcS\3\2\2\2\u01dd\u01e3\5X-\2\u01de\u01df\5V,"+
		"\2\u01df\u01e0\5X-\2\u01e0\u01e2\3\2\2\2\u01e1\u01de\3\2\2\2\u01e2\u01e5"+
		"\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4U\3\2\2\2\u01e5"+
		"\u01e3\3\2\2\2\u01e6\u01e7\t\4\2\2\u01e7W\3\2\2\2\u01e8\u01ee\5\\/\2\u01e9"+
		"\u01ea\5Z.\2\u01ea\u01eb\5\\/\2\u01eb\u01ed\3\2\2\2\u01ec\u01e9\3\2\2"+
		"\2\u01ed\u01f0\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01efY"+
		"\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f1\u01f2\t\5\2\2\u01f2[\3\2\2\2\u01f3"+
		"\u01f4\5^\60\2\u01f4\u01f5\5\\/\2\u01f5\u01f8\3\2\2\2\u01f6\u01f8\5`\61"+
		"\2\u01f7\u01f3\3\2\2\2\u01f7\u01f6\3\2\2\2\u01f8]\3\2\2\2\u01f9\u01fa"+
		"\t\6\2\2\u01fa_\3\2\2\2\u01fb\u01fe\5b\62\2\u01fc\u01fd\7@\2\2\u01fd\u01ff"+
		"\5\\/\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ffa\3\2\2\2\u0200\u0204"+
		"\5d\63\2\u0201\u0203\5f\64\2\u0202\u0201\3\2\2\2\u0203\u0206\3\2\2\2\u0204"+
		"\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205c\3\2\2\2\u0206\u0204\3\2\2\2"+
		"\u0207\u020f\5r:\2\u0208\u020f\7R\2\2\u0209\u020f\7S\2\2\u020a\u020f\7"+
		"A\2\2\u020b\u020f\7B\2\2\u020c\u020f\7C\2\2\u020d\u020f\7&\2\2\u020e\u0207"+
		"\3\2\2\2\u020e\u0208\3\2\2\2\u020e\u0209\3\2\2\2\u020e\u020a\3\2\2\2\u020e"+
		"\u020b\3\2\2\2\u020e\u020c\3\2\2\2\u020e\u020d\3\2\2\2\u020fe\3\2\2\2"+
		"\u0210\u0212\7\"\2\2\u0211\u0213\5\b\5\2\u0212\u0211\3\2\2\2\u0212\u0213"+
		"\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u021c\7#\2\2\u0215\u0216\7D\2\2\u0216"+
		"\u0217\5h\65\2\u0217\u0218\7E\2\2\u0218\u021c\3\2\2\2\u0219\u021a\7F\2"+
		"\2\u021a\u021c\5r:\2\u021b\u0210\3\2\2\2\u021b\u0215\3\2\2\2\u021b\u0219"+
		"\3\2\2\2\u021cg\3\2\2\2\u021d\u0222\5j\66\2\u021e\u021f\7\7\2\2\u021f"+
		"\u0221\5j\66\2\u0220\u021e\3\2\2\2\u0221\u0224\3\2\2\2\u0222\u0220\3\2"+
		"\2\2\u0222\u0223\3\2\2\2\u0223\u0226\3\2\2\2\u0224\u0222\3\2\2\2\u0225"+
		"\u0227\7\7\2\2\u0226\u0225\3\2\2\2\u0226\u0227\3\2\2\2\u0227i\3\2\2\2"+
		"\u0228\u0234\5<\37\2\u0229\u022b\5<\37\2\u022a\u0229\3\2\2\2\u022a\u022b"+
		"\3\2\2\2\u022b\u022c\3\2\2\2\u022c\u022e\7\4\2\2\u022d\u022f\5<\37\2\u022e"+
		"\u022d\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u0231\3\2\2\2\u0230\u0232\5l"+
		"\67\2\u0231\u0230\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u0234\3\2\2\2\u0233"+
		"\u0228\3\2\2\2\u0233\u022a\3\2\2\2\u0234k\3\2\2\2\u0235\u0237\7\4\2\2"+
		"\u0236\u0238\5<\37\2\u0237\u0236\3\2\2\2\u0237\u0238\3\2\2\2\u0238m\3"+
		"\2\2\2\u0239\u023e\5H%\2\u023a\u023b\7\7\2\2\u023b\u023d\5H%\2\u023c\u023a"+
		"\3\2\2\2\u023d\u0240\3\2\2\2\u023e\u023c\3\2\2\2\u023e\u023f\3\2\2\2\u023f"+
		"\u0242\3\2\2\2\u0240\u023e\3\2\2\2\u0241\u0243\7\7\2\2\u0242\u0241\3\2"+
		"\2\2\u0242\u0243\3\2\2\2\u0243o\3\2\2\2\u0244\u0249\5<\37\2\u0245\u0246"+
		"\7\7\2\2\u0246\u0248\5<\37\2\u0247\u0245\3\2\2\2\u0248\u024b\3\2\2\2\u0249"+
		"\u0247\3\2\2\2\u0249\u024a\3\2\2\2\u024a\u024d\3\2\2\2\u024b\u0249\3\2"+
		"\2\2\u024c\u024e\7\7\2\2\u024d\u024c\3\2\2\2\u024d\u024e\3\2\2\2\u024e"+
		"q\3\2\2\2\u024f\u0250\7W\2\2\u0250s\3\2\2\2\u0251\u0252\b;\1\2\u0252\u0296"+
		"\7A\2\2\u0253\u0296\7G\2\2\u0254\u0296\7H\2\2\u0255\u0296\7I\2\2\u0256"+
		"\u0296\7J\2\2\u0257\u0296\7K\2\2\u0258\u0259\7K\2\2\u0259\u025a\7L\2\2"+
		"\u025a\u025b\5r:\2\u025b\u025c\7\4\2\2\u025c\u025d\5t;\2\u025d\u0265\3"+
		"\2\2\2\u025e\u025f\7\7\2\2\u025f\u0260\5r:\2\u0260\u0261\7\4\2\2\u0261"+
		"\u0262\5t;\2\u0262\u0264\3\2\2\2\u0263\u025e\3\2\2\2\u0264\u0267\3\2\2"+
		"\2\u0265\u0263\3\2\2\2\u0265\u0266\3\2\2\2\u0266\u0268\3\2\2\2\u0267\u0265"+
		"\3\2\2\2\u0268\u0269\7M\2\2\u0269\u0296\3\2\2\2\u026a\u026b\7-\2\2\u026b"+
		"\u0270\5t;\2\u026c\u026d\7\7\2\2\u026d\u026f\5t;\2\u026e\u026c\3\2\2\2"+
		"\u026f\u0272\3\2\2\2\u0270\u026e\3\2\2\2\u0270\u0271\3\2\2\2\u0271\u0273"+
		"\3\2\2\2\u0272\u0270\3\2\2\2\u0273\u0274\7.\2\2\u0274\u0275\7$\2\2\u0275"+
		"\u0276\5t;\7\u0276\u0296\3\2\2\2\u0277\u0278\7N\2\2\u0278\u0279\7D\2\2"+
		"\u0279\u027a\5t;\2\u027a\u027b\7E\2\2\u027b\u0296\3\2\2\2\u027c\u027d"+
		"\7O\2\2\u027d\u0286\7\"\2\2\u027e\u0283\5t;\2\u027f\u0280\7\7\2\2\u0280"+
		"\u0282\5t;\2\u0281\u027f\3\2\2\2\u0282\u0285\3\2\2\2\u0283\u0281\3\2\2"+
		"\2\u0283\u0284\3\2\2\2\u0284\u0287\3\2\2\2\u0285\u0283\3\2\2\2\u0286\u027e"+
		"\3\2\2\2\u0286\u0287\3\2\2\2\u0287\u0288\3\2\2\2\u0288\u0296\7#\2\2\u0289"+
		"\u028a\7P\2\2\u028a\u028b\7\"\2\2\u028b\u028c\5t;\2\u028c\u028d\7#\2\2"+
		"\u028d\u0296\3\2\2\2\u028e\u028f\7Q\2\2\u028f\u0290\7L\2\2\u0290\u0291"+
		"\5t;\2\u0291\u0292\7\7\2\2\u0292\u0293\5t;\2\u0293\u0294\7M\2\2\u0294"+
		"\u0296\3\2\2\2\u0295\u0251\3\2\2\2\u0295\u0253\3\2\2\2\u0295\u0254\3\2"+
		"\2\2\u0295\u0255\3\2\2\2\u0295\u0256\3\2\2\2\u0295\u0257\3\2\2\2\u0295"+
		"\u0258\3\2\2\2\u0295\u026a\3\2\2\2\u0295\u0277\3\2\2\2\u0295\u027c\3\2"+
		"\2\2\u0295\u0289\3\2\2\2\u0295\u028e\3\2\2\2\u0296\u029c\3\2\2\2\u0297"+
		"\u0298\f\b\2\2\u0298\u0299\7$\2\2\u0299\u029b\5t;\t\u029a\u0297\3\2\2"+
		"\2\u029b\u029e\3\2\2\2\u029c\u029a\3\2\2\2\u029c\u029d\3\2\2\2\u029du"+
		"\3\2\2\2\u029e\u029c\3\2\2\2Fxz\177\u0081\u008f\u0096\u009a\u00a1\u00ae"+
		"\u00b3\u00b7\u00c7\u00d1\u00d9\u00e0\u00ed\u00f3\u00fc\u0107\u010f\u0113"+
		"\u011d\u012d\u0131\u013c\u0142\u014b\u0150\u0154\u0156\u0163\u016b\u0173"+
		"\u0182\u0191\u0199\u019f\u01a7\u01b6\u01bf\u01c7\u01cf\u01d8\u01e3\u01ee"+
		"\u01f7\u01fe\u0204\u020e\u0212\u021b\u0222\u0226\u022a\u022e\u0231\u0233"+
		"\u0237\u023e\u0242\u0249\u024d\u0265\u0270\u0283\u0286\u0295\u029c";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}