# Generated from Lolcode.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LolcodeParser import LolcodeParser
else:
    from generated.LolcodeParser import LolcodeParser

# This class defines a complete listener for a parse tree produced by LolcodeParser.
class LolcodeListener(ParseTreeListener):

    # Enter a parse tree produced by LolcodeParser#program.
    def enterProgram(self, ctx:LolcodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by LolcodeParser#program.
    def exitProgram(self, ctx:LolcodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by LolcodeParser#version.
    def enterVersion(self, ctx:LolcodeParser.VersionContext):
        pass

    # Exit a parse tree produced by LolcodeParser#version.
    def exitVersion(self, ctx:LolcodeParser.VersionContext):
        pass


    # Enter a parse tree produced by LolcodeParser#includes.
    def enterIncludes(self, ctx:LolcodeParser.IncludesContext):
        pass

    # Exit a parse tree produced by LolcodeParser#includes.
    def exitIncludes(self, ctx:LolcodeParser.IncludesContext):
        pass


    # Enter a parse tree produced by LolcodeParser#body.
    def enterBody(self, ctx:LolcodeParser.BodyContext):
        pass

    # Exit a parse tree produced by LolcodeParser#body.
    def exitBody(self, ctx:LolcodeParser.BodyContext):
        pass


    # Enter a parse tree produced by LolcodeParser#statement.
    def enterStatement(self, ctx:LolcodeParser.StatementContext):
        pass

    # Exit a parse tree produced by LolcodeParser#statement.
    def exitStatement(self, ctx:LolcodeParser.StatementContext):
        pass


    # Enter a parse tree produced by LolcodeParser#print_stmt.
    def enterPrint_stmt(self, ctx:LolcodeParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by LolcodeParser#print_stmt.
    def exitPrint_stmt(self, ctx:LolcodeParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by LolcodeParser#var_decl.
    def enterVar_decl(self, ctx:LolcodeParser.Var_declContext):
        pass

    # Exit a parse tree produced by LolcodeParser#var_decl.
    def exitVar_decl(self, ctx:LolcodeParser.Var_declContext):
        pass


    # Enter a parse tree produced by LolcodeParser#assign_stmt.
    def enterAssign_stmt(self, ctx:LolcodeParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by LolcodeParser#assign_stmt.
    def exitAssign_stmt(self, ctx:LolcodeParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by LolcodeParser#input_stmt.
    def enterInput_stmt(self, ctx:LolcodeParser.Input_stmtContext):
        pass

    # Exit a parse tree produced by LolcodeParser#input_stmt.
    def exitInput_stmt(self, ctx:LolcodeParser.Input_stmtContext):
        pass


    # Enter a parse tree produced by LolcodeParser#if_stmt.
    def enterIf_stmt(self, ctx:LolcodeParser.If_stmtContext):
        pass

    # Exit a parse tree produced by LolcodeParser#if_stmt.
    def exitIf_stmt(self, ctx:LolcodeParser.If_stmtContext):
        pass


    # Enter a parse tree produced by LolcodeParser#switch_stmt.
    def enterSwitch_stmt(self, ctx:LolcodeParser.Switch_stmtContext):
        pass

    # Exit a parse tree produced by LolcodeParser#switch_stmt.
    def exitSwitch_stmt(self, ctx:LolcodeParser.Switch_stmtContext):
        pass


    # Enter a parse tree produced by LolcodeParser#loop_stmt.
    def enterLoop_stmt(self, ctx:LolcodeParser.Loop_stmtContext):
        pass

    # Exit a parse tree produced by LolcodeParser#loop_stmt.
    def exitLoop_stmt(self, ctx:LolcodeParser.Loop_stmtContext):
        pass


    # Enter a parse tree produced by LolcodeParser#func_decl.
    def enterFunc_decl(self, ctx:LolcodeParser.Func_declContext):
        pass

    # Exit a parse tree produced by LolcodeParser#func_decl.
    def exitFunc_decl(self, ctx:LolcodeParser.Func_declContext):
        pass


    # Enter a parse tree produced by LolcodeParser#func_call.
    def enterFunc_call(self, ctx:LolcodeParser.Func_callContext):
        pass

    # Exit a parse tree produced by LolcodeParser#func_call.
    def exitFunc_call(self, ctx:LolcodeParser.Func_callContext):
        pass


    # Enter a parse tree produced by LolcodeParser#return_stmt.
    def enterReturn_stmt(self, ctx:LolcodeParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by LolcodeParser#return_stmt.
    def exitReturn_stmt(self, ctx:LolcodeParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by LolcodeParser#expression.
    def enterExpression(self, ctx:LolcodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LolcodeParser#expression.
    def exitExpression(self, ctx:LolcodeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LolcodeParser#binary_op.
    def enterBinary_op(self, ctx:LolcodeParser.Binary_opContext):
        pass

    # Exit a parse tree produced by LolcodeParser#binary_op.
    def exitBinary_op(self, ctx:LolcodeParser.Binary_opContext):
        pass


    # Enter a parse tree produced by LolcodeParser#unary_op.
    def enterUnary_op(self, ctx:LolcodeParser.Unary_opContext):
        pass

    # Exit a parse tree produced by LolcodeParser#unary_op.
    def exitUnary_op(self, ctx:LolcodeParser.Unary_opContext):
        pass


    # Enter a parse tree produced by LolcodeParser#multi_op.
    def enterMulti_op(self, ctx:LolcodeParser.Multi_opContext):
        pass

    # Exit a parse tree produced by LolcodeParser#multi_op.
    def exitMulti_op(self, ctx:LolcodeParser.Multi_opContext):
        pass



del LolcodeParser