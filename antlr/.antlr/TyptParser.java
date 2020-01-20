// Generated from d:\Brandon\University\Third Year Project\Typt\antlr\Typt.g4 by ANTLR 4.7.1
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
		RULE_comp_op = 34, RULE_expr = 35, RULE_xor_expr = 36, RULE_and_expr = 37, 
		RULE_shift_expr = 38, RULE_arith_expr = 39, RULE_term = 40, RULE_factor = 41, 
		RULE_power = 42, RULE_atom_expr = 43, RULE_atom = 44, RULE_trailer = 45, 
		RULE_subscriptlist = 46, RULE_subscript = 47, RULE_sliceop = 48, RULE_exprlist = 49, 
		RULE_testlist = 50, RULE_name = 51, RULE_value = 52, RULE_typt_type = 53;
	public static final String[] ruleNames = {
		"program", "using", "stmt", "argument_list", "argument", "simple_stmt", 
		"small_stmt", "expr_stmt", "anassign", "augassign", "var_dec_stmt", "del_stmt", 
		"pass_stmt", "flow_stmt", "break_stmt", "continue_stmt", "return_stmt", 
		"compound_stmt", "if_stmt", "while_stmt", "for_stmt", "suite", "func_def", 
		"func_signature", "func_parameter_list", "class_def", "class_dec", "class_method", 
		"class_static_method", "test", "or_test", "and_test", "not_test", "comparison", 
		"comp_op", "expr", "xor_expr", "and_expr", "shift_expr", "arith_expr", 
		"term", "factor", "power", "atom_expr", "atom", "trailer", "subscriptlist", 
		"subscript", "sliceop", "exprlist", "testlist", "name", "value", "typt_type"
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
			setState(112);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(110);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case NEWLINE:
						{
						setState(108);
						match(NEWLINE);
						}
						break;
					case T__0:
						{
						setState(109);
						using();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					} 
				}
				setState(114);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			}
			setState(119);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__19) | (1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << T__27) | (1L << T__28) | (1L << T__30) | (1L << T__35) | (1L << T__36) | (1L << T__41) | (1L << T__54) | (1L << T__55) | (1L << T__60) | (1L << T__62))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (T__63 - 64)) | (1L << (T__64 - 64)) | (1L << (NUMBER - 64)) | (1L << (STRING - 64)) | (1L << (NEWLINE - 64)) | (1L << (NAME - 64)))) != 0)) {
				{
				setState(117);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case NEWLINE:
					{
					setState(115);
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
					setState(116);
					stmt();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(121);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(122);
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
			setState(124);
			match(T__0);
			setState(125);
			match(T__1);
			setState(126);
			match(NEWLINE);
			setState(127);
			match(INDENT);
			setState(131); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(128);
				func_signature();
				setState(129);
				match(NEWLINE);
				}
				}
				setState(133); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NAME );
			setState(135);
			match(DEDENT);
			setState(136);
			match(T__2);
			setState(137);
			((UsingContext)_localctx).library_name = name();
			setState(140);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__3) {
				{
				setState(138);
				match(T__3);
				setState(139);
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
			setState(144);
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
				setState(142);
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
				setState(143);
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
			setState(146);
			argument();
			setState(151);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__4) {
				{
				{
				setState(147);
				match(T__4);
				setState(148);
				argument();
				}
				}
				setState(153);
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
			setState(154);
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
			setState(156);
			small_stmt();
			setState(157);
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
			setState(164);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(159);
				expr_stmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(160);
				var_dec_stmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(161);
				del_stmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(162);
				pass_stmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(163);
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
			setState(166);
			((Expr_stmtContext)_localctx).lhs = test();
			setState(173);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__5) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18))) != 0)) {
				{
				setState(169);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__5:
					{
					setState(167);
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
					setState(168);
					augassign();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(171);
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
			setState(175);
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
			setState(177);
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
			setState(189);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(179);
				((Var_dec_stmtContext)_localctx).lhs = name();
				setState(180);
				match(T__1);
				setState(181);
				typt_type(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(183);
				((Var_dec_stmtContext)_localctx).lhs = name();
				setState(184);
				match(T__1);
				setState(185);
				typt_type(0);
				setState(186);
				match(T__5);
				setState(187);
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
			setState(191);
			match(T__19);
			setState(192);
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
			setState(194);
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
			setState(199);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__21:
				enterOuterAlt(_localctx, 1);
				{
				setState(196);
				break_stmt();
				}
				break;
			case T__22:
				enterOuterAlt(_localctx, 2);
				{
				setState(197);
				continue_stmt();
				}
				break;
			case T__23:
				enterOuterAlt(_localctx, 3);
				{
				setState(198);
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
			setState(201);
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
			setState(203);
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
		public TestlistContext testlist() {
			return getRuleContext(TestlistContext.class,0);
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
			setState(205);
			match(T__23);
			setState(207);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 36)) & ~0x3f) == 0 && ((1L << (_la - 36)) & ((1L << (T__35 - 36)) | (1L << (T__41 - 36)) | (1L << (T__54 - 36)) | (1L << (T__55 - 36)) | (1L << (T__60 - 36)) | (1L << (T__62 - 36)) | (1L << (T__63 - 36)) | (1L << (T__64 - 36)) | (1L << (NUMBER - 36)) | (1L << (STRING - 36)) | (1L << (NAME - 36)))) != 0)) {
				{
				setState(206);
				testlist();
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
			setState(214);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__24:
				enterOuterAlt(_localctx, 1);
				{
				setState(209);
				if_stmt();
				}
				break;
			case T__27:
				enterOuterAlt(_localctx, 2);
				{
				setState(210);
				while_stmt();
				}
				break;
			case T__28:
				enterOuterAlt(_localctx, 3);
				{
				setState(211);
				for_stmt();
				}
				break;
			case T__30:
				enterOuterAlt(_localctx, 4);
				{
				setState(212);
				func_def();
				}
				break;
			case T__36:
				enterOuterAlt(_localctx, 5);
				{
				setState(213);
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
			setState(216);
			match(T__24);
			setState(217);
			test();
			setState(218);
			match(T__1);
			setState(219);
			suite();
			setState(227);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__25) {
				{
				{
				setState(220);
				match(T__25);
				setState(221);
				test();
				setState(222);
				match(T__1);
				setState(223);
				suite();
				}
				}
				setState(229);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(233);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__26) {
				{
				setState(230);
				match(T__26);
				setState(231);
				match(T__1);
				setState(232);
				suite();
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
			setState(235);
			match(T__27);
			setState(236);
			test();
			setState(237);
			match(T__1);
			setState(238);
			suite();
			setState(242);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__26) {
				{
				setState(239);
				match(T__26);
				setState(240);
				match(T__1);
				setState(241);
				suite();
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
			setState(244);
			match(T__28);
			setState(245);
			exprlist();
			setState(246);
			match(T__29);
			setState(247);
			testlist();
			setState(248);
			match(T__1);
			setState(249);
			suite();
			setState(253);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__26) {
				{
				setState(250);
				match(T__26);
				setState(251);
				match(T__1);
				setState(252);
				suite();
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
			setState(265);
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
				setState(255);
				simple_stmt();
				}
				break;
			case NEWLINE:
				enterOuterAlt(_localctx, 2);
				{
				setState(256);
				match(NEWLINE);
				setState(257);
				match(INDENT);
				setState(259); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(258);
					stmt();
					}
					}
					setState(261); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__19) | (1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << T__27) | (1L << T__28) | (1L << T__30) | (1L << T__35) | (1L << T__36) | (1L << T__41) | (1L << T__54) | (1L << T__55) | (1L << T__60) | (1L << T__62))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (T__63 - 64)) | (1L << (T__64 - 64)) | (1L << (NUMBER - 64)) | (1L << (STRING - 64)) | (1L << (NAME - 64)))) != 0) );
				setState(263);
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
			setState(267);
			match(T__30);
			setState(268);
			func_signature();
			setState(269);
			match(T__1);
			setState(270);
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
			setState(272);
			name();
			setState(273);
			match(T__31);
			setState(275);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NAME) {
				{
				setState(274);
				func_parameter_list();
				}
			}

			setState(277);
			match(T__32);
			setState(278);
			match(T__33);
			setState(279);
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
			setState(281);
			name();
			setState(282);
			match(T__1);
			setState(283);
			typt_type(0);
			setState(291);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(284);
					match(T__4);
					setState(285);
					name();
					setState(286);
					match(T__1);
					setState(287);
					typt_type(0);
					}
					} 
				}
				setState(293);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			}
			setState(295);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(294);
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
		public List<AtomContext> atom() {
			return getRuleContexts(AtomContext.class);
		}
		public AtomContext atom(int i) {
			return getRuleContext(AtomContext.class,i);
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
			setState(345);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(297);
				class_dec();
				setState(298);
				match(T__1);
				setState(299);
				match(NEWLINE);
				setState(300);
				match(INDENT);
				setState(312);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==NAME) {
					{
					{
					setState(301);
					name();
					setState(302);
					match(T__1);
					setState(303);
					typt_type(0);
					setState(306);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==T__5) {
						{
						setState(304);
						match(T__5);
						setState(305);
						atom();
						}
					}

					setState(308);
					match(NEWLINE);
					}
					}
					setState(314);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(326);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
				case 1:
					{
					setState(315);
					match(T__30);
					setState(316);
					match(T__34);
					setState(317);
					match(T__31);
					setState(318);
					match(T__35);
					setState(321);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==T__4) {
						{
						setState(319);
						match(T__4);
						setState(320);
						func_parameter_list();
						}
					}

					setState(323);
					match(T__32);
					setState(324);
					match(T__1);
					setState(325);
					suite();
					}
					break;
				}
				setState(332);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__30 || _la==T__37) {
					{
					setState(330);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case T__30:
						{
						setState(328);
						class_method();
						}
						break;
					case T__37:
						{
						setState(329);
						class_static_method();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					setState(334);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(335);
				match(DEDENT);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(337);
				class_dec();
				setState(338);
				match(T__1);
				setState(339);
				match(NEWLINE);
				setState(340);
				match(INDENT);
				setState(341);
				pass_stmt();
				setState(342);
				match(NEWLINE);
				setState(343);
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
			setState(347);
			match(T__36);
			setState(348);
			name();
			setState(353);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__31) {
				{
				setState(349);
				match(T__31);
				setState(350);
				name();
				setState(351);
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
			setState(355);
			match(T__30);
			setState(356);
			name();
			setState(357);
			match(T__31);
			setState(358);
			match(T__35);
			setState(361);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(359);
				match(T__4);
				setState(360);
				func_parameter_list();
				}
			}

			setState(363);
			match(T__32);
			setState(364);
			match(T__33);
			setState(365);
			typt_type(0);
			setState(366);
			match(T__1);
			setState(367);
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
			setState(369);
			match(T__37);
			setState(370);
			match(T__38);
			setState(371);
			match(NEWLINE);
			{
			setState(372);
			match(T__30);
			setState(373);
			name();
			setState(374);
			match(T__31);
			setState(376);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NAME) {
				{
				setState(375);
				func_parameter_list();
				}
			}

			setState(378);
			match(T__32);
			setState(379);
			match(T__33);
			setState(380);
			typt_type(0);
			setState(381);
			match(T__1);
			setState(382);
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
			setState(384);
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
			setState(386);
			and_test();
			setState(391);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__39) {
				{
				{
				setState(387);
				match(T__39);
				setState(388);
				and_test();
				}
				}
				setState(393);
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
			setState(394);
			not_test();
			setState(399);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__40) {
				{
				{
				setState(395);
				match(T__40);
				setState(396);
				not_test();
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

	public static class Not_testContext extends ParserRuleContext {
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
			setState(405);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__41:
				enterOuterAlt(_localctx, 1);
				{
				setState(402);
				match(T__41);
				setState(403);
				not_test();
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
				setState(404);
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
			setState(407);
			expr();
			setState(413);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__29) | (1L << T__41) | (1L << T__42) | (1L << T__43) | (1L << T__44) | (1L << T__45) | (1L << T__46) | (1L << T__47) | (1L << T__48))) != 0)) {
				{
				{
				setState(408);
				comp_op();
				setState(409);
				expr();
				}
				}
				setState(415);
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
			setState(428);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,38,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(416);
				match(T__42);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(417);
				match(T__43);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(418);
				match(T__44);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(419);
				match(T__45);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(420);
				match(T__46);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(421);
				match(T__47);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(422);
				match(T__29);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(423);
				match(T__41);
				setState(424);
				match(T__29);
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(425);
				match(T__48);
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(426);
				match(T__48);
				setState(427);
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
		public List<Xor_exprContext> xor_expr() {
			return getRuleContexts(Xor_exprContext.class);
		}
		public Xor_exprContext xor_expr(int i) {
			return getRuleContext(Xor_exprContext.class,i);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(430);
			xor_expr();
			setState(435);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__49) {
				{
				{
				setState(431);
				match(T__49);
				setState(432);
				xor_expr();
				}
				}
				setState(437);
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
		enterRule(_localctx, 72, RULE_xor_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(438);
			and_expr();
			setState(443);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__50) {
				{
				{
				setState(439);
				match(T__50);
				setState(440);
				and_expr();
				}
				}
				setState(445);
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
		enterRule(_localctx, 74, RULE_and_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(446);
			shift_expr();
			setState(451);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__51) {
				{
				{
				setState(447);
				match(T__51);
				setState(448);
				shift_expr();
				}
				}
				setState(453);
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
		public List<Arith_exprContext> arith_expr() {
			return getRuleContexts(Arith_exprContext.class);
		}
		public Arith_exprContext arith_expr(int i) {
			return getRuleContext(Arith_exprContext.class,i);
		}
		public Shift_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shift_expr; }
	}

	public final Shift_exprContext shift_expr() throws RecognitionException {
		Shift_exprContext _localctx = new Shift_exprContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_shift_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(454);
			arith_expr();
			setState(459);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__52 || _la==T__53) {
				{
				{
				setState(455);
				_la = _input.LA(1);
				if ( !(_la==T__52 || _la==T__53) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(456);
				arith_expr();
				}
				}
				setState(461);
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

	public static class Arith_exprContext extends ParserRuleContext {
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public Arith_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arith_expr; }
	}

	public final Arith_exprContext arith_expr() throws RecognitionException {
		Arith_exprContext _localctx = new Arith_exprContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_arith_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(462);
			term();
			setState(467);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__54 || _la==T__55) {
				{
				{
				setState(463);
				_la = _input.LA(1);
				if ( !(_la==T__54 || _la==T__55) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(464);
				term();
				}
				}
				setState(469);
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

	public static class TermContext extends ParserRuleContext {
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(470);
			factor();
			setState(475);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__37) | (1L << T__56) | (1L << T__57) | (1L << T__58) | (1L << T__59))) != 0)) {
				{
				{
				setState(471);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__37) | (1L << T__56) | (1L << T__57) | (1L << T__58) | (1L << T__59))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(472);
				factor();
				}
				}
				setState(477);
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

	public static class FactorContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
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
		enterRule(_localctx, 82, RULE_factor);
		int _la;
		try {
			setState(481);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__54:
			case T__55:
			case T__60:
				enterOuterAlt(_localctx, 1);
				{
				setState(478);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__54) | (1L << T__55) | (1L << T__60))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(479);
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
				setState(480);
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

	public static class PowerContext extends ParserRuleContext {
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
		enterRule(_localctx, 84, RULE_power);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(483);
			atom_expr();
			setState(486);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__61) {
				{
				setState(484);
				match(T__61);
				setState(485);
				factor();
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
		enterRule(_localctx, 86, RULE_atom_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(488);
			atom();
			setState(492);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 32)) & ~0x3f) == 0 && ((1L << (_la - 32)) & ((1L << (T__31 - 32)) | (1L << (T__65 - 32)) | (1L << (T__67 - 32)))) != 0)) {
				{
				{
				setState(489);
				trailer();
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

	public static class AtomContext extends ParserRuleContext {
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
		enterRule(_localctx, 88, RULE_atom);
		try {
			setState(502);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NAME:
				enterOuterAlt(_localctx, 1);
				{
				setState(495);
				name();
				}
				break;
			case NUMBER:
				enterOuterAlt(_localctx, 2);
				{
				setState(496);
				match(NUMBER);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 3);
				{
				setState(497);
				match(STRING);
				}
				break;
			case T__62:
				enterOuterAlt(_localctx, 4);
				{
				setState(498);
				match(T__62);
				}
				break;
			case T__63:
				enterOuterAlt(_localctx, 5);
				{
				setState(499);
				match(T__63);
				}
				break;
			case T__64:
				enterOuterAlt(_localctx, 6);
				{
				setState(500);
				match(T__64);
				}
				break;
			case T__35:
				enterOuterAlt(_localctx, 7);
				{
				setState(501);
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
		enterRule(_localctx, 90, RULE_trailer);
		int _la;
		try {
			setState(515);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__31:
				enterOuterAlt(_localctx, 1);
				{
				setState(504);
				match(T__31);
				setState(506);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 36)) & ~0x3f) == 0 && ((1L << (_la - 36)) & ((1L << (T__35 - 36)) | (1L << (T__41 - 36)) | (1L << (T__54 - 36)) | (1L << (T__55 - 36)) | (1L << (T__60 - 36)) | (1L << (T__62 - 36)) | (1L << (T__63 - 36)) | (1L << (T__64 - 36)) | (1L << (NUMBER - 36)) | (1L << (STRING - 36)) | (1L << (NAME - 36)))) != 0)) {
					{
					setState(505);
					argument_list();
					}
				}

				setState(508);
				match(T__32);
				}
				break;
			case T__65:
				enterOuterAlt(_localctx, 2);
				{
				setState(509);
				match(T__65);
				setState(510);
				subscriptlist();
				setState(511);
				match(T__66);
				}
				break;
			case T__67:
				enterOuterAlt(_localctx, 3);
				{
				setState(513);
				match(T__67);
				setState(514);
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
		enterRule(_localctx, 92, RULE_subscriptlist);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(517);
			subscript();
			setState(522);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,51,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(518);
					match(T__4);
					setState(519);
					subscript();
					}
					} 
				}
				setState(524);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,51,_ctx);
			}
			setState(526);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(525);
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
		enterRule(_localctx, 94, RULE_subscript);
		int _la;
		try {
			setState(539);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,56,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(528);
				test();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(530);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 36)) & ~0x3f) == 0 && ((1L << (_la - 36)) & ((1L << (T__35 - 36)) | (1L << (T__41 - 36)) | (1L << (T__54 - 36)) | (1L << (T__55 - 36)) | (1L << (T__60 - 36)) | (1L << (T__62 - 36)) | (1L << (T__63 - 36)) | (1L << (T__64 - 36)) | (1L << (NUMBER - 36)) | (1L << (STRING - 36)) | (1L << (NAME - 36)))) != 0)) {
					{
					setState(529);
					test();
					}
				}

				setState(532);
				match(T__1);
				setState(534);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 36)) & ~0x3f) == 0 && ((1L << (_la - 36)) & ((1L << (T__35 - 36)) | (1L << (T__41 - 36)) | (1L << (T__54 - 36)) | (1L << (T__55 - 36)) | (1L << (T__60 - 36)) | (1L << (T__62 - 36)) | (1L << (T__63 - 36)) | (1L << (T__64 - 36)) | (1L << (NUMBER - 36)) | (1L << (STRING - 36)) | (1L << (NAME - 36)))) != 0)) {
					{
					setState(533);
					test();
					}
				}

				setState(537);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__1) {
					{
					setState(536);
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
		enterRule(_localctx, 96, RULE_sliceop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(541);
			match(T__1);
			setState(543);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 36)) & ~0x3f) == 0 && ((1L << (_la - 36)) & ((1L << (T__35 - 36)) | (1L << (T__41 - 36)) | (1L << (T__54 - 36)) | (1L << (T__55 - 36)) | (1L << (T__60 - 36)) | (1L << (T__62 - 36)) | (1L << (T__63 - 36)) | (1L << (T__64 - 36)) | (1L << (NUMBER - 36)) | (1L << (STRING - 36)) | (1L << (NAME - 36)))) != 0)) {
				{
				setState(542);
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
		enterRule(_localctx, 98, RULE_exprlist);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(545);
			expr();
			setState(550);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,58,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(546);
					match(T__4);
					setState(547);
					expr();
					}
					} 
				}
				setState(552);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,58,_ctx);
			}
			setState(554);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(553);
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
		enterRule(_localctx, 100, RULE_testlist);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(556);
			test();
			setState(561);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,60,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(557);
					match(T__4);
					setState(558);
					test();
					}
					} 
				}
				setState(563);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,60,_ctx);
			}
			setState(565);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(564);
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
		enterRule(_localctx, 102, RULE_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(567);
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

	public static class ValueContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(TyptParser.NUMBER, 0); }
		public TerminalNode STRING() { return getToken(TyptParser.STRING, 0); }
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_value);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(569);
			_la = _input.LA(1);
			if ( !(((((_la - 63)) & ~0x3f) == 0 && ((1L << (_la - 63)) & ((1L << (T__62 - 63)) | (1L << (T__63 - 63)) | (1L << (T__64 - 63)) | (1L << (NUMBER - 63)) | (1L << (STRING - 63)))) != 0)) ) {
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

	public static class Typt_typeContext extends ParserRuleContext {
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
		int _startState = 106;
		enterRecursionRule(_localctx, 106, RULE_typt_type, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(639);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,66,_ctx) ) {
			case 1:
				{
				setState(572);
				match(T__62);
				}
				break;
			case 2:
				{
				setState(573);
				match(T__68);
				}
				break;
			case 3:
				{
				setState(574);
				match(T__69);
				}
				break;
			case 4:
				{
				setState(575);
				match(T__70);
				}
				break;
			case 5:
				{
				setState(576);
				match(T__71);
				}
				break;
			case 6:
				{
				setState(577);
				match(T__72);
				}
				break;
			case 7:
				{
				setState(578);
				match(T__72);
				setState(579);
				match(T__73);
				{
				setState(580);
				name();
				setState(581);
				match(T__1);
				setState(582);
				typt_type(0);
				}
				setState(591);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__4) {
					{
					{
					setState(584);
					match(T__4);
					setState(585);
					name();
					setState(586);
					match(T__1);
					setState(587);
					typt_type(0);
					}
					}
					setState(593);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(594);
				match(T__74);
				}
				break;
			case 8:
				{
				setState(596);
				match(T__42);
				setState(597);
				typt_type(0);
				setState(602);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__4) {
					{
					{
					setState(598);
					match(T__4);
					setState(599);
					typt_type(0);
					}
					}
					setState(604);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(605);
				match(T__43);
				setState(606);
				match(T__33);
				setState(607);
				typt_type(5);
				}
				break;
			case 9:
				{
				setState(609);
				match(T__75);
				setState(610);
				match(T__65);
				setState(611);
				typt_type(0);
				setState(612);
				match(T__66);
				}
				break;
			case 10:
				{
				setState(614);
				match(T__76);
				setState(615);
				match(T__31);
				setState(624);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 43)) & ~0x3f) == 0 && ((1L << (_la - 43)) & ((1L << (T__42 - 43)) | (1L << (T__62 - 43)) | (1L << (T__68 - 43)) | (1L << (T__69 - 43)) | (1L << (T__70 - 43)) | (1L << (T__71 - 43)) | (1L << (T__72 - 43)) | (1L << (T__75 - 43)) | (1L << (T__76 - 43)) | (1L << (T__77 - 43)) | (1L << (T__78 - 43)))) != 0)) {
					{
					setState(616);
					typt_type(0);
					setState(621);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__4) {
						{
						{
						setState(617);
						match(T__4);
						setState(618);
						typt_type(0);
						}
						}
						setState(623);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(626);
				match(T__32);
				}
				break;
			case 11:
				{
				setState(627);
				match(T__77);
				setState(628);
				match(T__31);
				setState(629);
				typt_type(0);
				setState(630);
				match(T__32);
				}
				break;
			case 12:
				{
				setState(632);
				match(T__78);
				setState(633);
				match(T__73);
				setState(634);
				typt_type(0);
				setState(635);
				match(T__4);
				setState(636);
				typt_type(0);
				setState(637);
				match(T__74);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(646);
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
					setState(641);
					if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
					setState(642);
					match(T__33);
					setState(643);
					typt_type(7);
					}
					} 
				}
				setState(648);
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
		case 53:
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3`\u028c\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\7\2q\n\2\f\2\16\2t\13\2\3\2"+
		"\3\2\7\2x\n\2\f\2\16\2{\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\6\3\u0086"+
		"\n\3\r\3\16\3\u0087\3\3\3\3\3\3\3\3\3\3\5\3\u008f\n\3\3\4\3\4\5\4\u0093"+
		"\n\4\3\5\3\5\3\5\7\5\u0098\n\5\f\5\16\5\u009b\13\5\3\6\3\6\3\7\3\7\3\7"+
		"\3\b\3\b\3\b\3\b\3\b\5\b\u00a7\n\b\3\t\3\t\3\t\5\t\u00ac\n\t\3\t\3\t\5"+
		"\t\u00b0\n\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f"+
		"\5\f\u00c0\n\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17\5\17\u00ca\n\17\3"+
		"\20\3\20\3\21\3\21\3\22\3\22\5\22\u00d2\n\22\3\23\3\23\3\23\3\23\3\23"+
		"\5\23\u00d9\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u00e4"+
		"\n\24\f\24\16\24\u00e7\13\24\3\24\3\24\3\24\5\24\u00ec\n\24\3\25\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\5\25\u00f5\n\25\3\26\3\26\3\26\3\26\3\26\3\26"+
		"\3\26\3\26\3\26\5\26\u0100\n\26\3\27\3\27\3\27\3\27\6\27\u0106\n\27\r"+
		"\27\16\27\u0107\3\27\3\27\5\27\u010c\n\27\3\30\3\30\3\30\3\30\3\30\3\31"+
		"\3\31\3\31\5\31\u0116\n\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32"+
		"\3\32\3\32\3\32\7\32\u0124\n\32\f\32\16\32\u0127\13\32\3\32\5\32\u012a"+
		"\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0135\n\33\3\33"+
		"\3\33\7\33\u0139\n\33\f\33\16\33\u013c\13\33\3\33\3\33\3\33\3\33\3\33"+
		"\3\33\5\33\u0144\n\33\3\33\3\33\3\33\5\33\u0149\n\33\3\33\3\33\7\33\u014d"+
		"\n\33\f\33\16\33\u0150\13\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3"+
		"\33\3\33\5\33\u015c\n\33\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0164\n\34"+
		"\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u016c\n\35\3\35\3\35\3\35\3\35\3\35"+
		"\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u017b\n\36\3\36\3\36\3\36"+
		"\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \7 \u0188\n \f \16 \u018b\13 \3!\3!"+
		"\3!\7!\u0190\n!\f!\16!\u0193\13!\3\"\3\"\3\"\5\"\u0198\n\"\3#\3#\3#\3"+
		"#\7#\u019e\n#\f#\16#\u01a1\13#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$"+
		"\u01af\n$\3%\3%\3%\7%\u01b4\n%\f%\16%\u01b7\13%\3&\3&\3&\7&\u01bc\n&\f"+
		"&\16&\u01bf\13&\3\'\3\'\3\'\7\'\u01c4\n\'\f\'\16\'\u01c7\13\'\3(\3(\3"+
		"(\7(\u01cc\n(\f(\16(\u01cf\13(\3)\3)\3)\7)\u01d4\n)\f)\16)\u01d7\13)\3"+
		"*\3*\3*\7*\u01dc\n*\f*\16*\u01df\13*\3+\3+\3+\5+\u01e4\n+\3,\3,\3,\5,"+
		"\u01e9\n,\3-\3-\7-\u01ed\n-\f-\16-\u01f0\13-\3.\3.\3.\3.\3.\3.\3.\5.\u01f9"+
		"\n.\3/\3/\5/\u01fd\n/\3/\3/\3/\3/\3/\3/\3/\5/\u0206\n/\3\60\3\60\3\60"+
		"\7\60\u020b\n\60\f\60\16\60\u020e\13\60\3\60\5\60\u0211\n\60\3\61\3\61"+
		"\5\61\u0215\n\61\3\61\3\61\5\61\u0219\n\61\3\61\5\61\u021c\n\61\5\61\u021e"+
		"\n\61\3\62\3\62\5\62\u0222\n\62\3\63\3\63\3\63\7\63\u0227\n\63\f\63\16"+
		"\63\u022a\13\63\3\63\5\63\u022d\n\63\3\64\3\64\3\64\7\64\u0232\n\64\f"+
		"\64\16\64\u0235\13\64\3\64\5\64\u0238\n\64\3\65\3\65\3\66\3\66\3\67\3"+
		"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3"+
		"\67\3\67\3\67\7\67\u0250\n\67\f\67\16\67\u0253\13\67\3\67\3\67\3\67\3"+
		"\67\3\67\3\67\7\67\u025b\n\67\f\67\16\67\u025e\13\67\3\67\3\67\3\67\3"+
		"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\7\67\u026e\n\67"+
		"\f\67\16\67\u0271\13\67\5\67\u0273\n\67\3\67\3\67\3\67\3\67\3\67\3\67"+
		"\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u0282\n\67\3\67\3\67\3\67\7\67"+
		"\u0287\n\67\f\67\16\67\u028a\13\67\3\67\2\3l8\2\4\6\b\n\f\16\20\22\24"+
		"\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjl\2\b\3"+
		"\2\t\25\3\2\678\3\29:\4\2((;>\4\29:??\4\2ACRS\2\u02b8\2r\3\2\2\2\4~\3"+
		"\2\2\2\6\u0092\3\2\2\2\b\u0094\3\2\2\2\n\u009c\3\2\2\2\f\u009e\3\2\2\2"+
		"\16\u00a6\3\2\2\2\20\u00a8\3\2\2\2\22\u00b1\3\2\2\2\24\u00b3\3\2\2\2\26"+
		"\u00bf\3\2\2\2\30\u00c1\3\2\2\2\32\u00c4\3\2\2\2\34\u00c9\3\2\2\2\36\u00cb"+
		"\3\2\2\2 \u00cd\3\2\2\2\"\u00cf\3\2\2\2$\u00d8\3\2\2\2&\u00da\3\2\2\2"+
		"(\u00ed\3\2\2\2*\u00f6\3\2\2\2,\u010b\3\2\2\2.\u010d\3\2\2\2\60\u0112"+
		"\3\2\2\2\62\u011b\3\2\2\2\64\u015b\3\2\2\2\66\u015d\3\2\2\28\u0165\3\2"+
		"\2\2:\u0173\3\2\2\2<\u0182\3\2\2\2>\u0184\3\2\2\2@\u018c\3\2\2\2B\u0197"+
		"\3\2\2\2D\u0199\3\2\2\2F\u01ae\3\2\2\2H\u01b0\3\2\2\2J\u01b8\3\2\2\2L"+
		"\u01c0\3\2\2\2N\u01c8\3\2\2\2P\u01d0\3\2\2\2R\u01d8\3\2\2\2T\u01e3\3\2"+
		"\2\2V\u01e5\3\2\2\2X\u01ea\3\2\2\2Z\u01f8\3\2\2\2\\\u0205\3\2\2\2^\u0207"+
		"\3\2\2\2`\u021d\3\2\2\2b\u021f\3\2\2\2d\u0223\3\2\2\2f\u022e\3\2\2\2h"+
		"\u0239\3\2\2\2j\u023b\3\2\2\2l\u0281\3\2\2\2nq\7V\2\2oq\5\4\3\2pn\3\2"+
		"\2\2po\3\2\2\2qt\3\2\2\2rp\3\2\2\2rs\3\2\2\2sy\3\2\2\2tr\3\2\2\2ux\7V"+
		"\2\2vx\5\6\4\2wu\3\2\2\2wv\3\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2\2z|\3\2"+
		"\2\2{y\3\2\2\2|}\7\2\2\3}\3\3\2\2\2~\177\7\3\2\2\177\u0080\7\4\2\2\u0080"+
		"\u0081\7V\2\2\u0081\u0085\7_\2\2\u0082\u0083\5\60\31\2\u0083\u0084\7V"+
		"\2\2\u0084\u0086\3\2\2\2\u0085\u0082\3\2\2\2\u0086\u0087\3\2\2\2\u0087"+
		"\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\7`"+
		"\2\2\u008a\u008b\7\5\2\2\u008b\u008e\5h\65\2\u008c\u008d\7\6\2\2\u008d"+
		"\u008f\5h\65\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\5\3\2\2\2"+
		"\u0090\u0093\5\f\7\2\u0091\u0093\5$\23\2\u0092\u0090\3\2\2\2\u0092\u0091"+
		"\3\2\2\2\u0093\7\3\2\2\2\u0094\u0099\5\n\6\2\u0095\u0096\7\7\2\2\u0096"+
		"\u0098\5\n\6\2\u0097\u0095\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2"+
		"\2\2\u0099\u009a\3\2\2\2\u009a\t\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009d"+
		"\5<\37\2\u009d\13\3\2\2\2\u009e\u009f\5\16\b\2\u009f\u00a0\7V\2\2\u00a0"+
		"\r\3\2\2\2\u00a1\u00a7\5\20\t\2\u00a2\u00a7\5\26\f\2\u00a3\u00a7\5\30"+
		"\r\2\u00a4\u00a7\5\32\16\2\u00a5\u00a7\5\34\17\2\u00a6\u00a1\3\2\2\2\u00a6"+
		"\u00a2\3\2\2\2\u00a6\u00a3\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a5\3\2"+
		"\2\2\u00a7\17\3\2\2\2\u00a8\u00af\5<\37\2\u00a9\u00ac\5\22\n\2\u00aa\u00ac"+
		"\5\24\13\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2"+
		"\u00ad\u00ae\5<\37\2\u00ae\u00b0\3\2\2\2\u00af\u00ab\3\2\2\2\u00af\u00b0"+
		"\3\2\2\2\u00b0\21\3\2\2\2\u00b1\u00b2\7\b\2\2\u00b2\23\3\2\2\2\u00b3\u00b4"+
		"\t\2\2\2\u00b4\25\3\2\2\2\u00b5\u00b6\5h\65\2\u00b6\u00b7\7\4\2\2\u00b7"+
		"\u00b8\5l\67\2\u00b8\u00c0\3\2\2\2\u00b9\u00ba\5h\65\2\u00ba\u00bb\7\4"+
		"\2\2\u00bb\u00bc\5l\67\2\u00bc\u00bd\7\b\2\2\u00bd\u00be\5<\37\2\u00be"+
		"\u00c0\3\2\2\2\u00bf\u00b5\3\2\2\2\u00bf\u00b9\3\2\2\2\u00c0\27\3\2\2"+
		"\2\u00c1\u00c2\7\26\2\2\u00c2\u00c3\5d\63\2\u00c3\31\3\2\2\2\u00c4\u00c5"+
		"\7\27\2\2\u00c5\33\3\2\2\2\u00c6\u00ca\5\36\20\2\u00c7\u00ca\5 \21\2\u00c8"+
		"\u00ca\5\"\22\2\u00c9\u00c6\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00c8\3"+
		"\2\2\2\u00ca\35\3\2\2\2\u00cb\u00cc\7\30\2\2\u00cc\37\3\2\2\2\u00cd\u00ce"+
		"\7\31\2\2\u00ce!\3\2\2\2\u00cf\u00d1\7\32\2\2\u00d0\u00d2\5f\64\2\u00d1"+
		"\u00d0\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2#\3\2\2\2\u00d3\u00d9\5&\24\2"+
		"\u00d4\u00d9\5(\25\2\u00d5\u00d9\5*\26\2\u00d6\u00d9\5.\30\2\u00d7\u00d9"+
		"\5\64\33\2\u00d8\u00d3\3\2\2\2\u00d8\u00d4\3\2\2\2\u00d8\u00d5\3\2\2\2"+
		"\u00d8\u00d6\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9%\3\2\2\2\u00da\u00db\7"+
		"\33\2\2\u00db\u00dc\5<\37\2\u00dc\u00dd\7\4\2\2\u00dd\u00e5\5,\27\2\u00de"+
		"\u00df\7\34\2\2\u00df\u00e0\5<\37\2\u00e0\u00e1\7\4\2\2\u00e1\u00e2\5"+
		",\27\2\u00e2\u00e4\3\2\2\2\u00e3\u00de\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5"+
		"\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00eb\3\2\2\2\u00e7\u00e5\3\2"+
		"\2\2\u00e8\u00e9\7\35\2\2\u00e9\u00ea\7\4\2\2\u00ea\u00ec\5,\27\2\u00eb"+
		"\u00e8\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\'\3\2\2\2\u00ed\u00ee\7\36\2"+
		"\2\u00ee\u00ef\5<\37\2\u00ef\u00f0\7\4\2\2\u00f0\u00f4\5,\27\2\u00f1\u00f2"+
		"\7\35\2\2\u00f2\u00f3\7\4\2\2\u00f3\u00f5\5,\27\2\u00f4\u00f1\3\2\2\2"+
		"\u00f4\u00f5\3\2\2\2\u00f5)\3\2\2\2\u00f6\u00f7\7\37\2\2\u00f7\u00f8\5"+
		"d\63\2\u00f8\u00f9\7 \2\2\u00f9\u00fa\5f\64\2\u00fa\u00fb\7\4\2\2\u00fb"+
		"\u00ff\5,\27\2\u00fc\u00fd\7\35\2\2\u00fd\u00fe\7\4\2\2\u00fe\u0100\5"+
		",\27\2\u00ff\u00fc\3\2\2\2\u00ff\u0100\3\2\2\2\u0100+\3\2\2\2\u0101\u010c"+
		"\5\f\7\2\u0102\u0103\7V\2\2\u0103\u0105\7_\2\2\u0104\u0106\5\6\4\2\u0105"+
		"\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0108\3\2"+
		"\2\2\u0108\u0109\3\2\2\2\u0109\u010a\7`\2\2\u010a\u010c\3\2\2\2\u010b"+
		"\u0101\3\2\2\2\u010b\u0102\3\2\2\2\u010c-\3\2\2\2\u010d\u010e\7!\2\2\u010e"+
		"\u010f\5\60\31\2\u010f\u0110\7\4\2\2\u0110\u0111\5,\27\2\u0111/\3\2\2"+
		"\2\u0112\u0113\5h\65\2\u0113\u0115\7\"\2\2\u0114\u0116\5\62\32\2\u0115"+
		"\u0114\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\7#"+
		"\2\2\u0118\u0119\7$\2\2\u0119\u011a\5l\67\2\u011a\61\3\2\2\2\u011b\u011c"+
		"\5h\65\2\u011c\u011d\7\4\2\2\u011d\u0125\5l\67\2\u011e\u011f\7\7\2\2\u011f"+
		"\u0120\5h\65\2\u0120\u0121\7\4\2\2\u0121\u0122\5l\67\2\u0122\u0124\3\2"+
		"\2\2\u0123\u011e\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0125"+
		"\u0126\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u012a\7\7"+
		"\2\2\u0129\u0128\3\2\2\2\u0129\u012a\3\2\2\2\u012a\63\3\2\2\2\u012b\u012c"+
		"\5\66\34\2\u012c\u012d\7\4\2\2\u012d\u012e\7V\2\2\u012e\u013a\7_\2\2\u012f"+
		"\u0130\5h\65\2\u0130\u0131\7\4\2\2\u0131\u0134\5l\67\2\u0132\u0133\7\b"+
		"\2\2\u0133\u0135\5Z.\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136"+
		"\3\2\2\2\u0136\u0137\7V\2\2\u0137\u0139\3\2\2\2\u0138\u012f\3\2\2\2\u0139"+
		"\u013c\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u0148\3\2"+
		"\2\2\u013c\u013a\3\2\2\2\u013d\u013e\7!\2\2\u013e\u013f\7%\2\2\u013f\u0140"+
		"\7\"\2\2\u0140\u0143\7&\2\2\u0141\u0142\7\7\2\2\u0142\u0144\5\62\32\2"+
		"\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0146"+
		"\7#\2\2\u0146\u0147\7\4\2\2\u0147\u0149\5,\27\2\u0148\u013d\3\2\2\2\u0148"+
		"\u0149\3\2\2\2\u0149\u014e\3\2\2\2\u014a\u014d\58\35\2\u014b\u014d\5:"+
		"\36\2\u014c\u014a\3\2\2\2\u014c\u014b\3\2\2\2\u014d\u0150\3\2\2\2\u014e"+
		"\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0151\3\2\2\2\u0150\u014e\3\2"+
		"\2\2\u0151\u0152\7`\2\2\u0152\u015c\3\2\2\2\u0153\u0154\5\66\34\2\u0154"+
		"\u0155\7\4\2\2\u0155\u0156\7V\2\2\u0156\u0157\7_\2\2\u0157\u0158\5\32"+
		"\16\2\u0158\u0159\7V\2\2\u0159\u015a\7`\2\2\u015a\u015c\3\2\2\2\u015b"+
		"\u012b\3\2\2\2\u015b\u0153\3\2\2\2\u015c\65\3\2\2\2\u015d\u015e\7\'\2"+
		"\2\u015e\u0163\5h\65\2\u015f\u0160\7\"\2\2\u0160\u0161\5h\65\2\u0161\u0162"+
		"\7#\2\2\u0162\u0164\3\2\2\2\u0163\u015f\3\2\2\2\u0163\u0164\3\2\2\2\u0164"+
		"\67\3\2\2\2\u0165\u0166\7!\2\2\u0166\u0167\5h\65\2\u0167\u0168\7\"\2\2"+
		"\u0168\u016b\7&\2\2\u0169\u016a\7\7\2\2\u016a\u016c\5\62\32\2\u016b\u0169"+
		"\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016e\7#\2\2\u016e"+
		"\u016f\7$\2\2\u016f\u0170\5l\67\2\u0170\u0171\7\4\2\2\u0171\u0172\5,\27"+
		"\2\u01729\3\2\2\2\u0173\u0174\7(\2\2\u0174\u0175\7)\2\2\u0175\u0176\7"+
		"V\2\2\u0176\u0177\7!\2\2\u0177\u0178\5h\65\2\u0178\u017a\7\"\2\2\u0179"+
		"\u017b\5\62\32\2\u017a\u0179\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c\3"+
		"\2\2\2\u017c\u017d\7#\2\2\u017d\u017e\7$\2\2\u017e\u017f\5l\67\2\u017f"+
		"\u0180\7\4\2\2\u0180\u0181\5,\27\2\u0181;\3\2\2\2\u0182\u0183\5> \2\u0183"+
		"=\3\2\2\2\u0184\u0189\5@!\2\u0185\u0186\7*\2\2\u0186\u0188\5@!\2\u0187"+
		"\u0185\3\2\2\2\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3\2"+
		"\2\2\u018a?\3\2\2\2\u018b\u0189\3\2\2\2\u018c\u0191\5B\"\2\u018d\u018e"+
		"\7+\2\2\u018e\u0190\5B\"\2\u018f\u018d\3\2\2\2\u0190\u0193\3\2\2\2\u0191"+
		"\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192A\3\2\2\2\u0193\u0191\3\2\2\2"+
		"\u0194\u0195\7,\2\2\u0195\u0198\5B\"\2\u0196\u0198\5D#\2\u0197\u0194\3"+
		"\2\2\2\u0197\u0196\3\2\2\2\u0198C\3\2\2\2\u0199\u019f\5H%\2\u019a\u019b"+
		"\5F$\2\u019b\u019c\5H%\2\u019c\u019e\3\2\2\2\u019d\u019a\3\2\2\2\u019e"+
		"\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0E\3\2\2\2"+
		"\u01a1\u019f\3\2\2\2\u01a2\u01af\7-\2\2\u01a3\u01af\7.\2\2\u01a4\u01af"+
		"\7/\2\2\u01a5\u01af\7\60\2\2\u01a6\u01af\7\61\2\2\u01a7\u01af\7\62\2\2"+
		"\u01a8\u01af\7 \2\2\u01a9\u01aa\7,\2\2\u01aa\u01af\7 \2\2\u01ab\u01af"+
		"\7\63\2\2\u01ac\u01ad\7\63\2\2\u01ad\u01af\7,\2\2\u01ae\u01a2\3\2\2\2"+
		"\u01ae\u01a3\3\2\2\2\u01ae\u01a4\3\2\2\2\u01ae\u01a5\3\2\2\2\u01ae\u01a6"+
		"\3\2\2\2\u01ae\u01a7\3\2\2\2\u01ae\u01a8\3\2\2\2\u01ae\u01a9\3\2\2\2\u01ae"+
		"\u01ab\3\2\2\2\u01ae\u01ac\3\2\2\2\u01afG\3\2\2\2\u01b0\u01b5\5J&\2\u01b1"+
		"\u01b2\7\64\2\2\u01b2\u01b4\5J&\2\u01b3\u01b1\3\2\2\2\u01b4\u01b7\3\2"+
		"\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6I\3\2\2\2\u01b7\u01b5"+
		"\3\2\2\2\u01b8\u01bd\5L\'\2\u01b9\u01ba\7\65\2\2\u01ba\u01bc\5L\'\2\u01bb"+
		"\u01b9\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01be\3\2"+
		"\2\2\u01beK\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0\u01c5\5N(\2\u01c1\u01c2"+
		"\7\66\2\2\u01c2\u01c4\5N(\2\u01c3\u01c1\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5"+
		"\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6M\3\2\2\2\u01c7\u01c5\3\2\2\2"+
		"\u01c8\u01cd\5P)\2\u01c9\u01ca\t\3\2\2\u01ca\u01cc\5P)\2\u01cb\u01c9\3"+
		"\2\2\2\u01cc\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce"+
		"O\3\2\2\2\u01cf\u01cd\3\2\2\2\u01d0\u01d5\5R*\2\u01d1\u01d2\t\4\2\2\u01d2"+
		"\u01d4\5R*\2\u01d3\u01d1\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3\3\2\2"+
		"\2\u01d5\u01d6\3\2\2\2\u01d6Q\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d8\u01dd"+
		"\5T+\2\u01d9\u01da\t\5\2\2\u01da\u01dc\5T+\2\u01db\u01d9\3\2\2\2\u01dc"+
		"\u01df\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de\3\2\2\2\u01deS\3\2\2\2"+
		"\u01df\u01dd\3\2\2\2\u01e0\u01e1\t\6\2\2\u01e1\u01e4\5T+\2\u01e2\u01e4"+
		"\5V,\2\u01e3\u01e0\3\2\2\2\u01e3\u01e2\3\2\2\2\u01e4U\3\2\2\2\u01e5\u01e8"+
		"\5X-\2\u01e6\u01e7\7@\2\2\u01e7\u01e9\5T+\2\u01e8\u01e6\3\2\2\2\u01e8"+
		"\u01e9\3\2\2\2\u01e9W\3\2\2\2\u01ea\u01ee\5Z.\2\u01eb\u01ed\5\\/\2\u01ec"+
		"\u01eb\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ef\3\2"+
		"\2\2\u01efY\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f1\u01f9\5h\65\2\u01f2\u01f9"+
		"\7R\2\2\u01f3\u01f9\7S\2\2\u01f4\u01f9\7A\2\2\u01f5\u01f9\7B\2\2\u01f6"+
		"\u01f9\7C\2\2\u01f7\u01f9\7&\2\2\u01f8\u01f1\3\2\2\2\u01f8\u01f2\3\2\2"+
		"\2\u01f8\u01f3\3\2\2\2\u01f8\u01f4\3\2\2\2\u01f8\u01f5\3\2\2\2\u01f8\u01f6"+
		"\3\2\2\2\u01f8\u01f7\3\2\2\2\u01f9[\3\2\2\2\u01fa\u01fc\7\"\2\2\u01fb"+
		"\u01fd\5\b\5\2\u01fc\u01fb\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fe\3\2"+
		"\2\2\u01fe\u0206\7#\2\2\u01ff\u0200\7D\2\2\u0200\u0201\5^\60\2\u0201\u0202"+
		"\7E\2\2\u0202\u0206\3\2\2\2\u0203\u0204\7F\2\2\u0204\u0206\5h\65\2\u0205"+
		"\u01fa\3\2\2\2\u0205\u01ff\3\2\2\2\u0205\u0203\3\2\2\2\u0206]\3\2\2\2"+
		"\u0207\u020c\5`\61\2\u0208\u0209\7\7\2\2\u0209\u020b\5`\61\2\u020a\u0208"+
		"\3\2\2\2\u020b\u020e\3\2\2\2\u020c\u020a\3\2\2\2\u020c\u020d\3\2\2\2\u020d"+
		"\u0210\3\2\2\2\u020e\u020c\3\2\2\2\u020f\u0211\7\7\2\2\u0210\u020f\3\2"+
		"\2\2\u0210\u0211\3\2\2\2\u0211_\3\2\2\2\u0212\u021e\5<\37\2\u0213\u0215"+
		"\5<\37\2\u0214\u0213\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0216\3\2\2\2\u0216"+
		"\u0218\7\4\2\2\u0217\u0219\5<\37\2\u0218\u0217\3\2\2\2\u0218\u0219\3\2"+
		"\2\2\u0219\u021b\3\2\2\2\u021a\u021c\5b\62\2\u021b\u021a\3\2\2\2\u021b"+
		"\u021c\3\2\2\2\u021c\u021e\3\2\2\2\u021d\u0212\3\2\2\2\u021d\u0214\3\2"+
		"\2\2\u021ea\3\2\2\2\u021f\u0221\7\4\2\2\u0220\u0222\5<\37\2\u0221\u0220"+
		"\3\2\2\2\u0221\u0222\3\2\2\2\u0222c\3\2\2\2\u0223\u0228\5H%\2\u0224\u0225"+
		"\7\7\2\2\u0225\u0227\5H%\2\u0226\u0224\3\2\2\2\u0227\u022a\3\2\2\2\u0228"+
		"\u0226\3\2\2\2\u0228\u0229\3\2\2\2\u0229\u022c\3\2\2\2\u022a\u0228\3\2"+
		"\2\2\u022b\u022d\7\7\2\2\u022c\u022b\3\2\2\2\u022c\u022d\3\2\2\2\u022d"+
		"e\3\2\2\2\u022e\u0233\5<\37\2\u022f\u0230\7\7\2\2\u0230\u0232\5<\37\2"+
		"\u0231\u022f\3\2\2\2\u0232\u0235\3\2\2\2\u0233\u0231\3\2\2\2\u0233\u0234"+
		"\3\2\2\2\u0234\u0237\3\2\2\2\u0235\u0233\3\2\2\2\u0236\u0238\7\7\2\2\u0237"+
		"\u0236\3\2\2\2\u0237\u0238\3\2\2\2\u0238g\3\2\2\2\u0239\u023a\7W\2\2\u023a"+
		"i\3\2\2\2\u023b\u023c\t\7\2\2\u023ck\3\2\2\2\u023d\u023e\b\67\1\2\u023e"+
		"\u0282\7A\2\2\u023f\u0282\7G\2\2\u0240\u0282\7H\2\2\u0241\u0282\7I\2\2"+
		"\u0242\u0282\7J\2\2\u0243\u0282\7K\2\2\u0244\u0245\7K\2\2\u0245\u0246"+
		"\7L\2\2\u0246\u0247\5h\65\2\u0247\u0248\7\4\2\2\u0248\u0249\5l\67\2\u0249"+
		"\u0251\3\2\2\2\u024a\u024b\7\7\2\2\u024b\u024c\5h\65\2\u024c\u024d\7\4"+
		"\2\2\u024d\u024e\5l\67\2\u024e\u0250\3\2\2\2\u024f\u024a\3\2\2\2\u0250"+
		"\u0253\3\2\2\2\u0251\u024f\3\2\2\2\u0251\u0252\3\2\2\2\u0252\u0254\3\2"+
		"\2\2\u0253\u0251\3\2\2\2\u0254\u0255\7M\2\2\u0255\u0282\3\2\2\2\u0256"+
		"\u0257\7-\2\2\u0257\u025c\5l\67\2\u0258\u0259\7\7\2\2\u0259\u025b\5l\67"+
		"\2\u025a\u0258\3\2\2\2\u025b\u025e\3\2\2\2\u025c\u025a\3\2\2\2\u025c\u025d"+
		"\3\2\2\2\u025d\u025f\3\2\2\2\u025e\u025c\3\2\2\2\u025f\u0260\7.\2\2\u0260"+
		"\u0261\7$\2\2\u0261\u0262\5l\67\7\u0262\u0282\3\2\2\2\u0263\u0264\7N\2"+
		"\2\u0264\u0265\7D\2\2\u0265\u0266\5l\67\2\u0266\u0267\7E\2\2\u0267\u0282"+
		"\3\2\2\2\u0268\u0269\7O\2\2\u0269\u0272\7\"\2\2\u026a\u026f\5l\67\2\u026b"+
		"\u026c\7\7\2\2\u026c\u026e\5l\67\2\u026d\u026b\3\2\2\2\u026e\u0271\3\2"+
		"\2\2\u026f\u026d\3\2\2\2\u026f\u0270\3\2\2\2\u0270\u0273\3\2\2\2\u0271"+
		"\u026f\3\2\2\2\u0272\u026a\3\2\2\2\u0272\u0273\3\2\2\2\u0273\u0274\3\2"+
		"\2\2\u0274\u0282\7#\2\2\u0275\u0276\7P\2\2\u0276\u0277\7\"\2\2\u0277\u0278"+
		"\5l\67\2\u0278\u0279\7#\2\2\u0279\u0282\3\2\2\2\u027a\u027b\7Q\2\2\u027b"+
		"\u027c\7L\2\2\u027c\u027d\5l\67\2\u027d\u027e\7\7\2\2\u027e\u027f\5l\67"+
		"\2\u027f\u0280\7M\2\2\u0280\u0282\3\2\2\2\u0281\u023d\3\2\2\2\u0281\u023f"+
		"\3\2\2\2\u0281\u0240\3\2\2\2\u0281\u0241\3\2\2\2\u0281\u0242\3\2\2\2\u0281"+
		"\u0243\3\2\2\2\u0281\u0244\3\2\2\2\u0281\u0256\3\2\2\2\u0281\u0263\3\2"+
		"\2\2\u0281\u0268\3\2\2\2\u0281\u0275\3\2\2\2\u0281\u027a\3\2\2\2\u0282"+
		"\u0288\3\2\2\2\u0283\u0284\f\b\2\2\u0284\u0285\7$\2\2\u0285\u0287\5l\67"+
		"\t\u0286\u0283\3\2\2\2\u0287\u028a\3\2\2\2\u0288\u0286\3\2\2\2\u0288\u0289"+
		"\3\2\2\2\u0289m\3\2\2\2\u028a\u0288\3\2\2\2Fprwy\u0087\u008e\u0092\u0099"+
		"\u00a6\u00ab\u00af\u00bf\u00c9\u00d1\u00d8\u00e5\u00eb\u00f4\u00ff\u0107"+
		"\u010b\u0115\u0125\u0129\u0134\u013a\u0143\u0148\u014c\u014e\u015b\u0163"+
		"\u016b\u017a\u0189\u0191\u0197\u019f\u01ae\u01b5\u01bd\u01c5\u01cd\u01d5"+
		"\u01dd\u01e3\u01e8\u01ee\u01f8\u01fc\u0205\u020c\u0210\u0214\u0218\u021b"+
		"\u021d\u0221\u0228\u022c\u0233\u0237\u0251\u025c\u026f\u0272\u0281\u0288";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}