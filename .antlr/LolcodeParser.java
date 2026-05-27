// Generated from /Users/mariapichor/Desktop/LOLCODE2Python/Lolcode.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class LolcodeParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, HAI=4, KTHXBYE=5, VISIBLE=6, GIMMEH=7, IHASA=8, 
		ITZ=9, R=10, SUM_OF=11, DIFF_OF=12, PRODUKT_OF=13, QUOSHUNT_OF=14, MOD_OF=15, 
		BIGGR_OF=16, SMALLR_OF=17, BOTH_OF=18, EITHER_OF=19, WON_OF=20, NOT=21, 
		ALL_OF=22, ANY_OF=23, BOTH_SAEM=24, DIFFRINT=25, AN=26, MKAY=27, O_RLY=28, 
		YA_RLY=29, NO_WAI=30, OIC=31, WTF=32, OMG=33, OMGWTF=34, GTFO=35, IM_IN_YR=36, 
		IM_OUTTA_YR=37, UPPIN=38, NERFIN=39, YR=40, TIL=41, WILE=42, HOW_IZ_I=43, 
		IF_U_SAY_SO=44, FOUND_YR=45, I_IZ=46, WIN=47, FAIL=48, CANHAS=49, LIBRARY_NAME=50, 
		NUMBER=51, ID=52, STRING=53, COMMENT=54, BLOCK_COMMENT=55, NL=56, WS=57;
	public static final int
		RULE_program = 0, RULE_version = 1, RULE_includes = 2, RULE_body = 3, 
		RULE_statement = 4, RULE_print_stmt = 5, RULE_var_decl = 6, RULE_assign_stmt = 7, 
		RULE_input_stmt = 8, RULE_if_stmt = 9, RULE_switch_stmt = 10, RULE_loop_stmt = 11, 
		RULE_func_decl = 12, RULE_func_call = 13, RULE_return_stmt = 14, RULE_expression = 15, 
		RULE_binary_op = 16, RULE_unary_op = 17, RULE_multi_op = 18;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "version", "includes", "body", "statement", "print_stmt", 
			"var_decl", "assign_stmt", "input_stmt", "if_stmt", "switch_stmt", "loop_stmt", 
			"func_decl", "func_call", "return_stmt", "expression", "binary_op", "unary_op", 
			"multi_op"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'?'", "'('", "')'", "'HAI'", "'KTHXBYE'", "'VISIBLE'", "'GIMMEH'", 
			"'I HAS A'", "'ITZ'", "'R'", "'SUM OF'", "'DIFF OF'", "'PRODUKT OF'", 
			"'QUOSHUNT OF'", "'MOD OF'", "'BIGGR OF'", "'SMALLR OF'", "'BOTH OF'", 
			"'EITHER OF'", "'WON OF'", "'NOT'", "'ALL OF'", "'ANY OF'", "'BOTH SAEM'", 
			"'DIFFRINT'", "'AN'", "'MKAY'", "'O RLY?'", "'YA RLY'", "'NO WAI'", "'OIC'", 
			"'WTF?'", "'OMG'", "'OMGWTF'", "'GTFO'", "'IM IN YR'", "'IM OUTTA YR'", 
			"'UPPIN'", "'NERFIN'", "'YR'", "'TIL'", "'WILE'", "'HOW IZ I'", "'IF U SAY SO'", 
			"'FOUND YR'", "'I IZ'", "'WIN'", "'FAIL'", "'CAN HAS'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, "HAI", "KTHXBYE", "VISIBLE", "GIMMEH", "IHASA", 
			"ITZ", "R", "SUM_OF", "DIFF_OF", "PRODUKT_OF", "QUOSHUNT_OF", "MOD_OF", 
			"BIGGR_OF", "SMALLR_OF", "BOTH_OF", "EITHER_OF", "WON_OF", "NOT", "ALL_OF", 
			"ANY_OF", "BOTH_SAEM", "DIFFRINT", "AN", "MKAY", "O_RLY", "YA_RLY", "NO_WAI", 
			"OIC", "WTF", "OMG", "OMGWTF", "GTFO", "IM_IN_YR", "IM_OUTTA_YR", "UPPIN", 
			"NERFIN", "YR", "TIL", "WILE", "HOW_IZ_I", "IF_U_SAY_SO", "FOUND_YR", 
			"I_IZ", "WIN", "FAIL", "CANHAS", "LIBRARY_NAME", "NUMBER", "ID", "STRING", 
			"COMMENT", "BLOCK_COMMENT", "NL", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
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
	public String getGrammarFileName() { return "Lolcode.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public LolcodeParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode HAI() { return getToken(LolcodeParser.HAI, 0); }
		public TerminalNode NL() { return getToken(LolcodeParser.NL, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode KTHXBYE() { return getToken(LolcodeParser.KTHXBYE, 0); }
		public VersionContext version() {
			return getRuleContext(VersionContext.class,0);
		}
		public IncludesContext includes() {
			return getRuleContext(IncludesContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			match(HAI);
			setState(40);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NUMBER) {
				{
				setState(39);
				version();
				}
			}

			setState(43);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==CANHAS) {
				{
				setState(42);
				includes();
				}
			}

			setState(45);
			match(NL);
			setState(46);
			body();
			setState(47);
			match(KTHXBYE);
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

	@SuppressWarnings("CheckReturnValue")
	public static class VersionContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(LolcodeParser.NUMBER, 0); }
		public VersionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_version; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).enterVersion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).exitVersion(this);
		}
	}

	public final VersionContext version() throws RecognitionException {
		VersionContext _localctx = new VersionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_version);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(49);
			match(NUMBER);
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

	@SuppressWarnings("CheckReturnValue")
	public static class IncludesContext extends ParserRuleContext {
		public TerminalNode CANHAS() { return getToken(LolcodeParser.CANHAS, 0); }
		public TerminalNode LIBRARY_NAME() { return getToken(LolcodeParser.LIBRARY_NAME, 0); }
		public IncludesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_includes; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).enterIncludes(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).exitIncludes(this);
		}
	}

	public final IncludesContext includes() throws RecognitionException {
		IncludesContext _localctx = new IncludesContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_includes);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			match(CANHAS);
			setState(52);
			match(LIBRARY_NAME);
			setState(53);
			match(T__0);
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

	@SuppressWarnings("CheckReturnValue")
	public static class BodyContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public List<TerminalNode> NL() { return getTokens(LolcodeParser.NL); }
		public TerminalNode NL(int i) {
			return getToken(LolcodeParser.NL, i);
		}
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).enterBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).exitBody(this);
		}
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_body);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(57);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case T__1:
					case VISIBLE:
					case GIMMEH:
					case IHASA:
					case SUM_OF:
					case DIFF_OF:
					case PRODUKT_OF:
					case QUOSHUNT_OF:
					case MOD_OF:
					case BIGGR_OF:
					case SMALLR_OF:
					case BOTH_OF:
					case EITHER_OF:
					case WON_OF:
					case NOT:
					case ALL_OF:
					case ANY_OF:
					case BOTH_SAEM:
					case DIFFRINT:
					case GTFO:
					case IM_IN_YR:
					case HOW_IZ_I:
					case FOUND_YR:
					case I_IZ:
					case WIN:
					case FAIL:
					case NUMBER:
					case ID:
					case STRING:
						{
						setState(55);
						statement();
						}
						break;
					case NL:
						{
						setState(56);
						match(NL);
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					} 
				}
				setState(61);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
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

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public Print_stmtContext print_stmt() {
			return getRuleContext(Print_stmtContext.class,0);
		}
		public Var_declContext var_decl() {
			return getRuleContext(Var_declContext.class,0);
		}
		public Assign_stmtContext assign_stmt() {
			return getRuleContext(Assign_stmtContext.class,0);
		}
		public Input_stmtContext input_stmt() {
			return getRuleContext(Input_stmtContext.class,0);
		}
		public If_stmtContext if_stmt() {
			return getRuleContext(If_stmtContext.class,0);
		}
		public Switch_stmtContext switch_stmt() {
			return getRuleContext(Switch_stmtContext.class,0);
		}
		public Loop_stmtContext loop_stmt() {
			return getRuleContext(Loop_stmtContext.class,0);
		}
		public Func_declContext func_decl() {
			return getRuleContext(Func_declContext.class,0);
		}
		public Func_callContext func_call() {
			return getRuleContext(Func_callContext.class,0);
		}
		public Return_stmtContext return_stmt() {
			return getRuleContext(Return_stmtContext.class,0);
		}
		public TerminalNode GTFO() { return getToken(LolcodeParser.GTFO, 0); }
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_statement);
		try {
			setState(73);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(62);
				print_stmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(63);
				var_decl();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(64);
				assign_stmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(65);
				input_stmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(66);
				if_stmt();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(67);
				switch_stmt();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(68);
				loop_stmt();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(69);
				func_decl();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(70);
				func_call();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(71);
				return_stmt();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(72);
				match(GTFO);
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

	@SuppressWarnings("CheckReturnValue")
	public static class Print_stmtContext extends ParserRuleContext {
		public TerminalNode VISIBLE() { return getToken(LolcodeParser.VISIBLE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Print_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).enterPrint_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).exitPrint_stmt(this);
		}
	}

	public final Print_stmtContext print_stmt() throws RecognitionException {
		Print_stmtContext _localctx = new Print_stmtContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_print_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(VISIBLE);
			setState(76);
			expression();
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

	@SuppressWarnings("CheckReturnValue")
	public static class Var_declContext extends ParserRuleContext {
		public TerminalNode IHASA() { return getToken(LolcodeParser.IHASA, 0); }
		public TerminalNode ID() { return getToken(LolcodeParser.ID, 0); }
		public TerminalNode ITZ() { return getToken(LolcodeParser.ITZ, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Var_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_decl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).enterVar_decl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).exitVar_decl(this);
		}
	}

	public final Var_declContext var_decl() throws RecognitionException {
		Var_declContext _localctx = new Var_declContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_var_decl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			match(IHASA);
			setState(79);
			match(ID);
			setState(82);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ITZ) {
				{
				setState(80);
				match(ITZ);
				setState(81);
				expression();
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

	@SuppressWarnings("CheckReturnValue")
	public static class Assign_stmtContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LolcodeParser.ID, 0); }
		public TerminalNode R() { return getToken(LolcodeParser.R, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Assign_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).enterAssign_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).exitAssign_stmt(this);
		}
	}

	public final Assign_stmtContext assign_stmt() throws RecognitionException {
		Assign_stmtContext _localctx = new Assign_stmtContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_assign_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			match(ID);
			setState(85);
			match(R);
			setState(86);
			expression();
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

	@SuppressWarnings("CheckReturnValue")
	public static class Input_stmtContext extends ParserRuleContext {
		public TerminalNode GIMMEH() { return getToken(LolcodeParser.GIMMEH, 0); }
		public TerminalNode ID() { return getToken(LolcodeParser.ID, 0); }
		public Input_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_input_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).enterInput_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).exitInput_stmt(this);
		}
	}

	public final Input_stmtContext input_stmt() throws RecognitionException {
		Input_stmtContext _localctx = new Input_stmtContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_input_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			match(GIMMEH);
			setState(89);
			match(ID);
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

	@SuppressWarnings("CheckReturnValue")
	public static class If_stmtContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode O_RLY() { return getToken(LolcodeParser.O_RLY, 0); }
		public List<TerminalNode> NL() { return getTokens(LolcodeParser.NL); }
		public TerminalNode NL(int i) {
			return getToken(LolcodeParser.NL, i);
		}
		public TerminalNode YA_RLY() { return getToken(LolcodeParser.YA_RLY, 0); }
		public List<BodyContext> body() {
			return getRuleContexts(BodyContext.class);
		}
		public BodyContext body(int i) {
			return getRuleContext(BodyContext.class,i);
		}
		public TerminalNode OIC() { return getToken(LolcodeParser.OIC, 0); }
		public TerminalNode NO_WAI() { return getToken(LolcodeParser.NO_WAI, 0); }
		public If_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).enterIf_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).exitIf_stmt(this);
		}
	}

	public final If_stmtContext if_stmt() throws RecognitionException {
		If_stmtContext _localctx = new If_stmtContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_if_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			expression();
			setState(93);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(92);
				match(NL);
				}
			}

			setState(95);
			match(O_RLY);
			setState(96);
			match(NL);
			setState(97);
			match(YA_RLY);
			setState(98);
			match(NL);
			setState(99);
			body();
			setState(103);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NO_WAI) {
				{
				setState(100);
				match(NO_WAI);
				setState(101);
				match(NL);
				setState(102);
				body();
				}
			}

			setState(106);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(105);
				match(NL);
				}
			}

			setState(108);
			match(OIC);
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

	@SuppressWarnings("CheckReturnValue")
	public static class Switch_stmtContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode WTF() { return getToken(LolcodeParser.WTF, 0); }
		public List<TerminalNode> NL() { return getTokens(LolcodeParser.NL); }
		public TerminalNode NL(int i) {
			return getToken(LolcodeParser.NL, i);
		}
		public TerminalNode OIC() { return getToken(LolcodeParser.OIC, 0); }
		public List<TerminalNode> OMG() { return getTokens(LolcodeParser.OMG); }
		public TerminalNode OMG(int i) {
			return getToken(LolcodeParser.OMG, i);
		}
		public List<BodyContext> body() {
			return getRuleContexts(BodyContext.class);
		}
		public BodyContext body(int i) {
			return getRuleContext(BodyContext.class,i);
		}
		public TerminalNode OMGWTF() { return getToken(LolcodeParser.OMGWTF, 0); }
		public Switch_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_switch_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).enterSwitch_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).exitSwitch_stmt(this);
		}
	}

	public final Switch_stmtContext switch_stmt() throws RecognitionException {
		Switch_stmtContext _localctx = new Switch_stmtContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_switch_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(110);
			expression();
			setState(112);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(111);
				match(NL);
				}
			}

			setState(114);
			match(WTF);
			setState(115);
			match(NL);
			setState(123);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OMG) {
				{
				{
				setState(116);
				match(OMG);
				setState(117);
				expression();
				setState(118);
				match(NL);
				setState(119);
				body();
				}
				}
				setState(125);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(129);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OMGWTF) {
				{
				setState(126);
				match(OMGWTF);
				setState(127);
				match(NL);
				setState(128);
				body();
				}
			}

			setState(132);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(131);
				match(NL);
				}
			}

			setState(134);
			match(OIC);
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

	@SuppressWarnings("CheckReturnValue")
	public static class Loop_stmtContext extends ParserRuleContext {
		public TerminalNode IM_IN_YR() { return getToken(LolcodeParser.IM_IN_YR, 0); }
		public List<TerminalNode> ID() { return getTokens(LolcodeParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(LolcodeParser.ID, i);
		}
		public TerminalNode YR() { return getToken(LolcodeParser.YR, 0); }
		public TerminalNode NL() { return getToken(LolcodeParser.NL, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode IM_OUTTA_YR() { return getToken(LolcodeParser.IM_OUTTA_YR, 0); }
		public TerminalNode UPPIN() { return getToken(LolcodeParser.UPPIN, 0); }
		public TerminalNode NERFIN() { return getToken(LolcodeParser.NERFIN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode TIL() { return getToken(LolcodeParser.TIL, 0); }
		public TerminalNode WILE() { return getToken(LolcodeParser.WILE, 0); }
		public Loop_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loop_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).enterLoop_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).exitLoop_stmt(this);
		}
	}

	public final Loop_stmtContext loop_stmt() throws RecognitionException {
		Loop_stmtContext _localctx = new Loop_stmtContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_loop_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(136);
			match(IM_IN_YR);
			setState(137);
			match(ID);
			setState(138);
			_la = _input.LA(1);
			if ( !(_la==UPPIN || _la==NERFIN) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(139);
			match(YR);
			setState(140);
			match(ID);
			setState(145);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 16261777041913860L) != 0)) {
				{
				setState(142);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==TIL || _la==WILE) {
					{
					setState(141);
					_la = _input.LA(1);
					if ( !(_la==TIL || _la==WILE) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
				}

				setState(144);
				expression();
				}
			}

			setState(147);
			match(NL);
			setState(148);
			body();
			setState(149);
			match(IM_OUTTA_YR);
			setState(150);
			match(ID);
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

	@SuppressWarnings("CheckReturnValue")
	public static class Func_declContext extends ParserRuleContext {
		public TerminalNode HOW_IZ_I() { return getToken(LolcodeParser.HOW_IZ_I, 0); }
		public List<TerminalNode> ID() { return getTokens(LolcodeParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(LolcodeParser.ID, i);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode IF_U_SAY_SO() { return getToken(LolcodeParser.IF_U_SAY_SO, 0); }
		public List<TerminalNode> AN() { return getTokens(LolcodeParser.AN); }
		public TerminalNode AN(int i) {
			return getToken(LolcodeParser.AN, i);
		}
		public Func_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_decl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).enterFunc_decl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).exitFunc_decl(this);
		}
	}

	public final Func_declContext func_decl() throws RecognitionException {
		Func_declContext _localctx = new Func_declContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_func_decl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(152);
			match(HOW_IZ_I);
			setState(153);
			match(ID);
			setState(158);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AN) {
				{
				{
				setState(154);
				match(AN);
				setState(155);
				match(ID);
				}
				}
				setState(160);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(161);
			body();
			setState(162);
			match(IF_U_SAY_SO);
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

	@SuppressWarnings("CheckReturnValue")
	public static class Func_callContext extends ParserRuleContext {
		public TerminalNode I_IZ() { return getToken(LolcodeParser.I_IZ, 0); }
		public TerminalNode ID() { return getToken(LolcodeParser.ID, 0); }
		public TerminalNode MKAY() { return getToken(LolcodeParser.MKAY, 0); }
		public List<TerminalNode> AN() { return getTokens(LolcodeParser.AN); }
		public TerminalNode AN(int i) {
			return getToken(LolcodeParser.AN, i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Func_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_call; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).enterFunc_call(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).exitFunc_call(this);
		}
	}

	public final Func_callContext func_call() throws RecognitionException {
		Func_callContext _localctx = new Func_callContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_func_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(164);
			match(I_IZ);
			setState(165);
			match(ID);
			setState(170);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AN) {
				{
				{
				setState(166);
				match(AN);
				setState(167);
				expression();
				}
				}
				setState(172);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(173);
			match(MKAY);
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

	@SuppressWarnings("CheckReturnValue")
	public static class Return_stmtContext extends ParserRuleContext {
		public TerminalNode FOUND_YR() { return getToken(LolcodeParser.FOUND_YR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Return_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).enterReturn_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).exitReturn_stmt(this);
		}
	}

	public final Return_stmtContext return_stmt() throws RecognitionException {
		Return_stmtContext _localctx = new Return_stmtContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_return_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			match(FOUND_YR);
			setState(176);
			expression();
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

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(LolcodeParser.NUMBER, 0); }
		public TerminalNode STRING() { return getToken(LolcodeParser.STRING, 0); }
		public TerminalNode ID() { return getToken(LolcodeParser.ID, 0); }
		public TerminalNode WIN() { return getToken(LolcodeParser.WIN, 0); }
		public TerminalNode FAIL() { return getToken(LolcodeParser.FAIL, 0); }
		public Binary_opContext binary_op() {
			return getRuleContext(Binary_opContext.class,0);
		}
		public Unary_opContext unary_op() {
			return getRuleContext(Unary_opContext.class,0);
		}
		public Multi_opContext multi_op() {
			return getRuleContext(Multi_opContext.class,0);
		}
		public Func_callContext func_call() {
			return getRuleContext(Func_callContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).exitExpression(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_expression);
		try {
			setState(191);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(178);
				match(NUMBER);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(179);
				match(STRING);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 3);
				{
				setState(180);
				match(ID);
				}
				break;
			case WIN:
				enterOuterAlt(_localctx, 4);
				{
				setState(181);
				match(WIN);
				}
				break;
			case FAIL:
				enterOuterAlt(_localctx, 5);
				{
				setState(182);
				match(FAIL);
				}
				break;
			case SUM_OF:
			case DIFF_OF:
			case PRODUKT_OF:
			case QUOSHUNT_OF:
			case MOD_OF:
			case BIGGR_OF:
			case SMALLR_OF:
			case BOTH_OF:
			case EITHER_OF:
			case WON_OF:
			case BOTH_SAEM:
			case DIFFRINT:
				enterOuterAlt(_localctx, 6);
				{
				setState(183);
				binary_op();
				}
				break;
			case NOT:
				enterOuterAlt(_localctx, 7);
				{
				setState(184);
				unary_op();
				}
				break;
			case ALL_OF:
			case ANY_OF:
				enterOuterAlt(_localctx, 8);
				{
				setState(185);
				multi_op();
				}
				break;
			case I_IZ:
				enterOuterAlt(_localctx, 9);
				{
				setState(186);
				func_call();
				}
				break;
			case T__1:
				enterOuterAlt(_localctx, 10);
				{
				setState(187);
				match(T__1);
				setState(188);
				expression();
				setState(189);
				match(T__2);
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

	@SuppressWarnings("CheckReturnValue")
	public static class Binary_opContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode AN() { return getToken(LolcodeParser.AN, 0); }
		public TerminalNode SUM_OF() { return getToken(LolcodeParser.SUM_OF, 0); }
		public TerminalNode DIFF_OF() { return getToken(LolcodeParser.DIFF_OF, 0); }
		public TerminalNode PRODUKT_OF() { return getToken(LolcodeParser.PRODUKT_OF, 0); }
		public TerminalNode QUOSHUNT_OF() { return getToken(LolcodeParser.QUOSHUNT_OF, 0); }
		public TerminalNode MOD_OF() { return getToken(LolcodeParser.MOD_OF, 0); }
		public TerminalNode BIGGR_OF() { return getToken(LolcodeParser.BIGGR_OF, 0); }
		public TerminalNode SMALLR_OF() { return getToken(LolcodeParser.SMALLR_OF, 0); }
		public TerminalNode BOTH_OF() { return getToken(LolcodeParser.BOTH_OF, 0); }
		public TerminalNode EITHER_OF() { return getToken(LolcodeParser.EITHER_OF, 0); }
		public TerminalNode WON_OF() { return getToken(LolcodeParser.WON_OF, 0); }
		public TerminalNode BOTH_SAEM() { return getToken(LolcodeParser.BOTH_SAEM, 0); }
		public TerminalNode DIFFRINT() { return getToken(LolcodeParser.DIFFRINT, 0); }
		public Binary_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binary_op; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).enterBinary_op(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).exitBinary_op(this);
		}
	}

	public final Binary_opContext binary_op() throws RecognitionException {
		Binary_opContext _localctx = new Binary_opContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_binary_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 52426752L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(194);
			expression();
			setState(195);
			match(AN);
			setState(196);
			expression();
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

	@SuppressWarnings("CheckReturnValue")
	public static class Unary_opContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(LolcodeParser.NOT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Unary_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unary_op; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).enterUnary_op(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).exitUnary_op(this);
		}
	}

	public final Unary_opContext unary_op() throws RecognitionException {
		Unary_opContext _localctx = new Unary_opContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_unary_op);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(198);
			match(NOT);
			setState(199);
			expression();
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

	@SuppressWarnings("CheckReturnValue")
	public static class Multi_opContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode MKAY() { return getToken(LolcodeParser.MKAY, 0); }
		public TerminalNode ALL_OF() { return getToken(LolcodeParser.ALL_OF, 0); }
		public TerminalNode ANY_OF() { return getToken(LolcodeParser.ANY_OF, 0); }
		public List<TerminalNode> AN() { return getTokens(LolcodeParser.AN); }
		public TerminalNode AN(int i) {
			return getToken(LolcodeParser.AN, i);
		}
		public Multi_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multi_op; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).enterMulti_op(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LolcodeListener ) ((LolcodeListener)listener).exitMulti_op(this);
		}
	}

	public final Multi_opContext multi_op() throws RecognitionException {
		Multi_opContext _localctx = new Multi_opContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_multi_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(201);
			_la = _input.LA(1);
			if ( !(_la==ALL_OF || _la==ANY_OF) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(202);
			expression();
			setState(207);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AN) {
				{
				{
				setState(203);
				match(AN);
				setState(204);
				expression();
				}
				}
				setState(209);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(210);
			match(MKAY);
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
		"\u0004\u00019\u00d5\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0001\u0000\u0001\u0000\u0003\u0000)\b\u0000\u0001\u0000\u0003\u0000"+
		",\b\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0005\u0003:\b\u0003\n\u0003\f\u0003=\t\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004J\b\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0003\u0006S\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0003\t^\b\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003\th\b"+
		"\t\u0001\t\u0003\tk\b\t\u0001\t\u0001\t\u0001\n\u0001\n\u0003\nq\b\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0005\nz\b\n\n\n\f"+
		"\n}\t\n\u0001\n\u0001\n\u0001\n\u0003\n\u0082\b\n\u0001\n\u0003\n\u0085"+
		"\b\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0003\u000b\u008f\b\u000b\u0001\u000b\u0003\u000b\u0092"+
		"\b\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0005\f\u009d\b\f\n\f\f\f\u00a0\t\f\u0001\f"+
		"\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0005\r\u00a9\b\r\n\r"+
		"\f\r\u00ac\t\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0003\u000f\u00c0\b\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0005\u0012\u00ce\b\u0012\n\u0012\f\u0012"+
		"\u00d1\t\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0000\u0000\u0013\u0000"+
		"\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c"+
		"\u001e \"$\u0000\u0004\u0001\u0000&\'\u0001\u0000)*\u0002\u0000\u000b"+
		"\u0014\u0018\u0019\u0001\u0000\u0016\u0017\u00e5\u0000&\u0001\u0000\u0000"+
		"\u0000\u00021\u0001\u0000\u0000\u0000\u00043\u0001\u0000\u0000\u0000\u0006"+
		";\u0001\u0000\u0000\u0000\bI\u0001\u0000\u0000\u0000\nK\u0001\u0000\u0000"+
		"\u0000\fN\u0001\u0000\u0000\u0000\u000eT\u0001\u0000\u0000\u0000\u0010"+
		"X\u0001\u0000\u0000\u0000\u0012[\u0001\u0000\u0000\u0000\u0014n\u0001"+
		"\u0000\u0000\u0000\u0016\u0088\u0001\u0000\u0000\u0000\u0018\u0098\u0001"+
		"\u0000\u0000\u0000\u001a\u00a4\u0001\u0000\u0000\u0000\u001c\u00af\u0001"+
		"\u0000\u0000\u0000\u001e\u00bf\u0001\u0000\u0000\u0000 \u00c1\u0001\u0000"+
		"\u0000\u0000\"\u00c6\u0001\u0000\u0000\u0000$\u00c9\u0001\u0000\u0000"+
		"\u0000&(\u0005\u0004\u0000\u0000\')\u0003\u0002\u0001\u0000(\'\u0001\u0000"+
		"\u0000\u0000()\u0001\u0000\u0000\u0000)+\u0001\u0000\u0000\u0000*,\u0003"+
		"\u0004\u0002\u0000+*\u0001\u0000\u0000\u0000+,\u0001\u0000\u0000\u0000"+
		",-\u0001\u0000\u0000\u0000-.\u00058\u0000\u0000./\u0003\u0006\u0003\u0000"+
		"/0\u0005\u0005\u0000\u00000\u0001\u0001\u0000\u0000\u000012\u00053\u0000"+
		"\u00002\u0003\u0001\u0000\u0000\u000034\u00051\u0000\u000045\u00052\u0000"+
		"\u000056\u0005\u0001\u0000\u00006\u0005\u0001\u0000\u0000\u00007:\u0003"+
		"\b\u0004\u00008:\u00058\u0000\u000097\u0001\u0000\u0000\u000098\u0001"+
		"\u0000\u0000\u0000:=\u0001\u0000\u0000\u0000;9\u0001\u0000\u0000\u0000"+
		";<\u0001\u0000\u0000\u0000<\u0007\u0001\u0000\u0000\u0000=;\u0001\u0000"+
		"\u0000\u0000>J\u0003\n\u0005\u0000?J\u0003\f\u0006\u0000@J\u0003\u000e"+
		"\u0007\u0000AJ\u0003\u0010\b\u0000BJ\u0003\u0012\t\u0000CJ\u0003\u0014"+
		"\n\u0000DJ\u0003\u0016\u000b\u0000EJ\u0003\u0018\f\u0000FJ\u0003\u001a"+
		"\r\u0000GJ\u0003\u001c\u000e\u0000HJ\u0005#\u0000\u0000I>\u0001\u0000"+
		"\u0000\u0000I?\u0001\u0000\u0000\u0000I@\u0001\u0000\u0000\u0000IA\u0001"+
		"\u0000\u0000\u0000IB\u0001\u0000\u0000\u0000IC\u0001\u0000\u0000\u0000"+
		"ID\u0001\u0000\u0000\u0000IE\u0001\u0000\u0000\u0000IF\u0001\u0000\u0000"+
		"\u0000IG\u0001\u0000\u0000\u0000IH\u0001\u0000\u0000\u0000J\t\u0001\u0000"+
		"\u0000\u0000KL\u0005\u0006\u0000\u0000LM\u0003\u001e\u000f\u0000M\u000b"+
		"\u0001\u0000\u0000\u0000NO\u0005\b\u0000\u0000OR\u00054\u0000\u0000PQ"+
		"\u0005\t\u0000\u0000QS\u0003\u001e\u000f\u0000RP\u0001\u0000\u0000\u0000"+
		"RS\u0001\u0000\u0000\u0000S\r\u0001\u0000\u0000\u0000TU\u00054\u0000\u0000"+
		"UV\u0005\n\u0000\u0000VW\u0003\u001e\u000f\u0000W\u000f\u0001\u0000\u0000"+
		"\u0000XY\u0005\u0007\u0000\u0000YZ\u00054\u0000\u0000Z\u0011\u0001\u0000"+
		"\u0000\u0000[]\u0003\u001e\u000f\u0000\\^\u00058\u0000\u0000]\\\u0001"+
		"\u0000\u0000\u0000]^\u0001\u0000\u0000\u0000^_\u0001\u0000\u0000\u0000"+
		"_`\u0005\u001c\u0000\u0000`a\u00058\u0000\u0000ab\u0005\u001d\u0000\u0000"+
		"bc\u00058\u0000\u0000cg\u0003\u0006\u0003\u0000de\u0005\u001e\u0000\u0000"+
		"ef\u00058\u0000\u0000fh\u0003\u0006\u0003\u0000gd\u0001\u0000\u0000\u0000"+
		"gh\u0001\u0000\u0000\u0000hj\u0001\u0000\u0000\u0000ik\u00058\u0000\u0000"+
		"ji\u0001\u0000\u0000\u0000jk\u0001\u0000\u0000\u0000kl\u0001\u0000\u0000"+
		"\u0000lm\u0005\u001f\u0000\u0000m\u0013\u0001\u0000\u0000\u0000np\u0003"+
		"\u001e\u000f\u0000oq\u00058\u0000\u0000po\u0001\u0000\u0000\u0000pq\u0001"+
		"\u0000\u0000\u0000qr\u0001\u0000\u0000\u0000rs\u0005 \u0000\u0000s{\u0005"+
		"8\u0000\u0000tu\u0005!\u0000\u0000uv\u0003\u001e\u000f\u0000vw\u00058"+
		"\u0000\u0000wx\u0003\u0006\u0003\u0000xz\u0001\u0000\u0000\u0000yt\u0001"+
		"\u0000\u0000\u0000z}\u0001\u0000\u0000\u0000{y\u0001\u0000\u0000\u0000"+
		"{|\u0001\u0000\u0000\u0000|\u0081\u0001\u0000\u0000\u0000}{\u0001\u0000"+
		"\u0000\u0000~\u007f\u0005\"\u0000\u0000\u007f\u0080\u00058\u0000\u0000"+
		"\u0080\u0082\u0003\u0006\u0003\u0000\u0081~\u0001\u0000\u0000\u0000\u0081"+
		"\u0082\u0001\u0000\u0000\u0000\u0082\u0084\u0001\u0000\u0000\u0000\u0083"+
		"\u0085\u00058\u0000\u0000\u0084\u0083\u0001\u0000\u0000\u0000\u0084\u0085"+
		"\u0001\u0000\u0000\u0000\u0085\u0086\u0001\u0000\u0000\u0000\u0086\u0087"+
		"\u0005\u001f\u0000\u0000\u0087\u0015\u0001\u0000\u0000\u0000\u0088\u0089"+
		"\u0005$\u0000\u0000\u0089\u008a\u00054\u0000\u0000\u008a\u008b\u0007\u0000"+
		"\u0000\u0000\u008b\u008c\u0005(\u0000\u0000\u008c\u0091\u00054\u0000\u0000"+
		"\u008d\u008f\u0007\u0001\u0000\u0000\u008e\u008d\u0001\u0000\u0000\u0000"+
		"\u008e\u008f\u0001\u0000\u0000\u0000\u008f\u0090\u0001\u0000\u0000\u0000"+
		"\u0090\u0092\u0003\u001e\u000f\u0000\u0091\u008e\u0001\u0000\u0000\u0000"+
		"\u0091\u0092\u0001\u0000\u0000\u0000\u0092\u0093\u0001\u0000\u0000\u0000"+
		"\u0093\u0094\u00058\u0000\u0000\u0094\u0095\u0003\u0006\u0003\u0000\u0095"+
		"\u0096\u0005%\u0000\u0000\u0096\u0097\u00054\u0000\u0000\u0097\u0017\u0001"+
		"\u0000\u0000\u0000\u0098\u0099\u0005+\u0000\u0000\u0099\u009e\u00054\u0000"+
		"\u0000\u009a\u009b\u0005\u001a\u0000\u0000\u009b\u009d\u00054\u0000\u0000"+
		"\u009c\u009a\u0001\u0000\u0000\u0000\u009d\u00a0\u0001\u0000\u0000\u0000"+
		"\u009e\u009c\u0001\u0000\u0000\u0000\u009e\u009f\u0001\u0000\u0000\u0000"+
		"\u009f\u00a1\u0001\u0000\u0000\u0000\u00a0\u009e\u0001\u0000\u0000\u0000"+
		"\u00a1\u00a2\u0003\u0006\u0003\u0000\u00a2\u00a3\u0005,\u0000\u0000\u00a3"+
		"\u0019\u0001\u0000\u0000\u0000\u00a4\u00a5\u0005.\u0000\u0000\u00a5\u00aa"+
		"\u00054\u0000\u0000\u00a6\u00a7\u0005\u001a\u0000\u0000\u00a7\u00a9\u0003"+
		"\u001e\u000f\u0000\u00a8\u00a6\u0001\u0000\u0000\u0000\u00a9\u00ac\u0001"+
		"\u0000\u0000\u0000\u00aa\u00a8\u0001\u0000\u0000\u0000\u00aa\u00ab\u0001"+
		"\u0000\u0000\u0000\u00ab\u00ad\u0001\u0000\u0000\u0000\u00ac\u00aa\u0001"+
		"\u0000\u0000\u0000\u00ad\u00ae\u0005\u001b\u0000\u0000\u00ae\u001b\u0001"+
		"\u0000\u0000\u0000\u00af\u00b0\u0005-\u0000\u0000\u00b0\u00b1\u0003\u001e"+
		"\u000f\u0000\u00b1\u001d\u0001\u0000\u0000\u0000\u00b2\u00c0\u00053\u0000"+
		"\u0000\u00b3\u00c0\u00055\u0000\u0000\u00b4\u00c0\u00054\u0000\u0000\u00b5"+
		"\u00c0\u0005/\u0000\u0000\u00b6\u00c0\u00050\u0000\u0000\u00b7\u00c0\u0003"+
		" \u0010\u0000\u00b8\u00c0\u0003\"\u0011\u0000\u00b9\u00c0\u0003$\u0012"+
		"\u0000\u00ba\u00c0\u0003\u001a\r\u0000\u00bb\u00bc\u0005\u0002\u0000\u0000"+
		"\u00bc\u00bd\u0003\u001e\u000f\u0000\u00bd\u00be\u0005\u0003\u0000\u0000"+
		"\u00be\u00c0\u0001\u0000\u0000\u0000\u00bf\u00b2\u0001\u0000\u0000\u0000"+
		"\u00bf\u00b3\u0001\u0000\u0000\u0000\u00bf\u00b4\u0001\u0000\u0000\u0000"+
		"\u00bf\u00b5\u0001\u0000\u0000\u0000\u00bf\u00b6\u0001\u0000\u0000\u0000"+
		"\u00bf\u00b7\u0001\u0000\u0000\u0000\u00bf\u00b8\u0001\u0000\u0000\u0000"+
		"\u00bf\u00b9\u0001\u0000\u0000\u0000\u00bf\u00ba\u0001\u0000\u0000\u0000"+
		"\u00bf\u00bb\u0001\u0000\u0000\u0000\u00c0\u001f\u0001\u0000\u0000\u0000"+
		"\u00c1\u00c2\u0007\u0002\u0000\u0000\u00c2\u00c3\u0003\u001e\u000f\u0000"+
		"\u00c3\u00c4\u0005\u001a\u0000\u0000\u00c4\u00c5\u0003\u001e\u000f\u0000"+
		"\u00c5!\u0001\u0000\u0000\u0000\u00c6\u00c7\u0005\u0015\u0000\u0000\u00c7"+
		"\u00c8\u0003\u001e\u000f\u0000\u00c8#\u0001\u0000\u0000\u0000\u00c9\u00ca"+
		"\u0007\u0003\u0000\u0000\u00ca\u00cf\u0003\u001e\u000f\u0000\u00cb\u00cc"+
		"\u0005\u001a\u0000\u0000\u00cc\u00ce\u0003\u001e\u000f\u0000\u00cd\u00cb"+
		"\u0001\u0000\u0000\u0000\u00ce\u00d1\u0001\u0000\u0000\u0000\u00cf\u00cd"+
		"\u0001\u0000\u0000\u0000\u00cf\u00d0\u0001\u0000\u0000\u0000\u00d0\u00d2"+
		"\u0001\u0000\u0000\u0000\u00d1\u00cf\u0001\u0000\u0000\u0000\u00d2\u00d3"+
		"\u0005\u001b\u0000\u0000\u00d3%\u0001\u0000\u0000\u0000\u0013(+9;IR]g"+
		"jp{\u0081\u0084\u008e\u0091\u009e\u00aa\u00bf\u00cf";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}