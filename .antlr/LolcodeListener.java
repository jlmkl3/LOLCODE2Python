// Generated from /Users/mariapichor/Desktop/LOLCODE2Python/Lolcode.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link LolcodeParser}.
 */
public interface LolcodeListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link LolcodeParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(LolcodeParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link LolcodeParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(LolcodeParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link LolcodeParser#version}.
	 * @param ctx the parse tree
	 */
	void enterVersion(LolcodeParser.VersionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LolcodeParser#version}.
	 * @param ctx the parse tree
	 */
	void exitVersion(LolcodeParser.VersionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LolcodeParser#includes}.
	 * @param ctx the parse tree
	 */
	void enterIncludes(LolcodeParser.IncludesContext ctx);
	/**
	 * Exit a parse tree produced by {@link LolcodeParser#includes}.
	 * @param ctx the parse tree
	 */
	void exitIncludes(LolcodeParser.IncludesContext ctx);
	/**
	 * Enter a parse tree produced by {@link LolcodeParser#body}.
	 * @param ctx the parse tree
	 */
	void enterBody(LolcodeParser.BodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link LolcodeParser#body}.
	 * @param ctx the parse tree
	 */
	void exitBody(LolcodeParser.BodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link LolcodeParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(LolcodeParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LolcodeParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(LolcodeParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LolcodeParser#print_stmt}.
	 * @param ctx the parse tree
	 */
	void enterPrint_stmt(LolcodeParser.Print_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link LolcodeParser#print_stmt}.
	 * @param ctx the parse tree
	 */
	void exitPrint_stmt(LolcodeParser.Print_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link LolcodeParser#var_decl}.
	 * @param ctx the parse tree
	 */
	void enterVar_decl(LolcodeParser.Var_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link LolcodeParser#var_decl}.
	 * @param ctx the parse tree
	 */
	void exitVar_decl(LolcodeParser.Var_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link LolcodeParser#assign_stmt}.
	 * @param ctx the parse tree
	 */
	void enterAssign_stmt(LolcodeParser.Assign_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link LolcodeParser#assign_stmt}.
	 * @param ctx the parse tree
	 */
	void exitAssign_stmt(LolcodeParser.Assign_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link LolcodeParser#input_stmt}.
	 * @param ctx the parse tree
	 */
	void enterInput_stmt(LolcodeParser.Input_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link LolcodeParser#input_stmt}.
	 * @param ctx the parse tree
	 */
	void exitInput_stmt(LolcodeParser.Input_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link LolcodeParser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void enterIf_stmt(LolcodeParser.If_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link LolcodeParser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void exitIf_stmt(LolcodeParser.If_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link LolcodeParser#switch_stmt}.
	 * @param ctx the parse tree
	 */
	void enterSwitch_stmt(LolcodeParser.Switch_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link LolcodeParser#switch_stmt}.
	 * @param ctx the parse tree
	 */
	void exitSwitch_stmt(LolcodeParser.Switch_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link LolcodeParser#loop_stmt}.
	 * @param ctx the parse tree
	 */
	void enterLoop_stmt(LolcodeParser.Loop_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link LolcodeParser#loop_stmt}.
	 * @param ctx the parse tree
	 */
	void exitLoop_stmt(LolcodeParser.Loop_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link LolcodeParser#func_decl}.
	 * @param ctx the parse tree
	 */
	void enterFunc_decl(LolcodeParser.Func_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link LolcodeParser#func_decl}.
	 * @param ctx the parse tree
	 */
	void exitFunc_decl(LolcodeParser.Func_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link LolcodeParser#func_call}.
	 * @param ctx the parse tree
	 */
	void enterFunc_call(LolcodeParser.Func_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link LolcodeParser#func_call}.
	 * @param ctx the parse tree
	 */
	void exitFunc_call(LolcodeParser.Func_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link LolcodeParser#return_stmt}.
	 * @param ctx the parse tree
	 */
	void enterReturn_stmt(LolcodeParser.Return_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link LolcodeParser#return_stmt}.
	 * @param ctx the parse tree
	 */
	void exitReturn_stmt(LolcodeParser.Return_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link LolcodeParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(LolcodeParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LolcodeParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(LolcodeParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LolcodeParser#binary_op}.
	 * @param ctx the parse tree
	 */
	void enterBinary_op(LolcodeParser.Binary_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link LolcodeParser#binary_op}.
	 * @param ctx the parse tree
	 */
	void exitBinary_op(LolcodeParser.Binary_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link LolcodeParser#unary_op}.
	 * @param ctx the parse tree
	 */
	void enterUnary_op(LolcodeParser.Unary_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link LolcodeParser#unary_op}.
	 * @param ctx the parse tree
	 */
	void exitUnary_op(LolcodeParser.Unary_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link LolcodeParser#multi_op}.
	 * @param ctx the parse tree
	 */
	void enterMulti_op(LolcodeParser.Multi_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link LolcodeParser#multi_op}.
	 * @param ctx the parse tree
	 */
	void exitMulti_op(LolcodeParser.Multi_opContext ctx);
}