# Generated from Lolcode.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LolcodeParser import LolcodeParser
else:
    from generated.LolcodeParser import LolcodeParser

# This class defines a complete generic visitor for a parse tree produced by LolcodeParser.

class LolcodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LolcodeParser#program.
    def visitProgram(self, ctx:LolcodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LolcodeParser#version.
    def visitVersion(self, ctx:LolcodeParser.VersionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LolcodeParser#includes.
    def visitIncludes(self, ctx:LolcodeParser.IncludesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LolcodeParser#body.
    def visitBody(self, ctx:LolcodeParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LolcodeParser#statement.
    def visitStatement(self, ctx:LolcodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LolcodeParser#print_stmt.
    def visitPrint_stmt(self, ctx:LolcodeParser.Print_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LolcodeParser#var_decl.
    def visitVar_decl(self, ctx:LolcodeParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LolcodeParser#assign_stmt.
    def visitAssign_stmt(self, ctx:LolcodeParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LolcodeParser#input_stmt.
    def visitInput_stmt(self, ctx:LolcodeParser.Input_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LolcodeParser#if_stmt.
    def visitIf_stmt(self, ctx:LolcodeParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LolcodeParser#switch_stmt.
    def visitSwitch_stmt(self, ctx:LolcodeParser.Switch_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LolcodeParser#loop_stmt.
    def visitLoop_stmt(self, ctx:LolcodeParser.Loop_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LolcodeParser#func_decl.
    def visitFunc_decl(self, ctx:LolcodeParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LolcodeParser#func_call.
    def visitFunc_call(self, ctx:LolcodeParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LolcodeParser#return_stmt.
    def visitReturn_stmt(self, ctx:LolcodeParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LolcodeParser#expression.
    def visitExpression(self, ctx:LolcodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LolcodeParser#binary_op.
    def visitBinary_op(self, ctx:LolcodeParser.Binary_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LolcodeParser#unary_op.
    def visitUnary_op(self, ctx:LolcodeParser.Unary_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LolcodeParser#multi_op.
    def visitMulti_op(self, ctx:LolcodeParser.Multi_opContext):
        return self.visitChildren(ctx)



del LolcodeParser