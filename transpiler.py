from generated.LolcodeVisitor import LolcodeVisitor
from generated.LolcodeParser import LolcodeParser

class Lolcode2Python(LolcodeVisitor):
    indent_level: int 
    def __init__(self, token_stream=None):
        super().__init__()
        self.token_stream = token_stream
        self.indent_level = 0

    def get_indent(self):
        return "    " * self.indent_level
    
    def visitProgram(self, ctx: LolcodeParser.ProgramContext):
        header = "it = None\n"
        body_code = self.visit(ctx.body())
        return header + body_code
    
    def visitBody(self, ctx:LolcodeParser.BodyContext):
        lines = []
        for st in ctx.statement():
            code = self.visit(st)
            if code:
                lines.append(str(code))
        return "\n".join(lines)
    
    def visitStatement(self, ctx: LolcodeParser.StatementContext):
        if ctx.GTFO():
            return "{self.get_indent()}break"
        return self.visitChildren(ctx)
    
    def visitExpression(self, ctx: LolcodeParser.ExpressionContext):
        if ctx.NUMBER():
            return ctx.NUMBER().getText()
        if ctx.STRING():
            return ctx.STRING().getText()
        if ctx.ID():
            return ctx.ID().getText()
        if ctx.binary_op():
            return self.visit(ctx.binary_op())
        if ctx.getText() == "WIN": return "True"
        if ctx.getText() == "FAIL": return "False"
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return f"({self.visit(ctx.expression(0))})"
        return self.visitChildren(ctx)
    
    #instrukcje podstawowe
    def visitPrint_stmt(self, ctx:LolcodeParser.Print_stmtContext):
        code = self.visit(ctx.expression())
        txt = f"{self.get_indent()}print({code})"
        return txt
    
    def visitVar_decl(self, ctx:LolcodeParser.Var_declContext):
        name = ctx.ID().getText()
        if ctx.ITZ():
            value = self.visit(ctx.expression())
            return f"{self.get_indent()}{name} = {value}"
        return f"{self.get_indent()}{name} = None"
    
    def visitAssign_stmt(self, ctx:LolcodeParser.Assign_stmtContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        return f"{self.get_indent()}{name} = {value}"
    
    def visitInput_stmt(self, ctx:LolcodeParser.Input_stmtContext):
        name = ctx.ID().getText()
        txt = f"{self.get_indent()}{name} = input()"
        return txt
    
    #Instrukcja warunkowa
    def visitIf_stmt(self, ctx:LolcodeParser.If_stmtContext):
        lines = []
        condition = self.visit(ctx.expression())
        lines = [f"if {condition}:"]
        
        self.indent_level+=1
        if_body = self.visit(ctx.body(0))
        lines.append(if_body)

        self.indent_level-=1

        if ctx.NO_WAI():
            lines.append(f"{self.get_indent()}else:")
            self.indent_level+=1
            else_body = self.visit(ctx.body(1))
            lines.append(else_body)
            self.indent_level-=1
        return "\n".join(lines)

    def visitBinary_op(self, ctx: LolcodeParser.Binary_opContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        
        if ctx.SUM_OF(): return f"({left} + {right})"
        if ctx.DIFF_OF(): return f"({left} - {right})"
        if ctx.PRODUKT_OF(): return f"({left} * {right})"
        if ctx.QUOSHUNT_OF(): return f"({left} / {right})"
        if ctx.MOD_OF(): return f"({left} % {right})"
        if ctx.BIGGR_OF(): return f"max({left}, {right})"
        if ctx.SMALLR_OF(): return f"min({left}, {right})"
        if ctx.BOTH_OF(): return f"({left} and {right})"
        if ctx.EITHER_OF(): return f"({left} or {right})"
        if ctx.WON_OF(): return f"({left} ^ {right})" # XOR
        if ctx.BOTH_SAEM(): return f"({left} == {right})"
        if ctx.DIFFRINT(): return f"({left} != {right})"
        return ""
    
    def visitLoop_stmt(self, ctx: LolcodeParser.Loop_stmtContext):
        var_name = ctx.ID(1).getText()
        condition = self.visit(ctx.expression())
        
        if ctx.TIL():
            loop_head = f"while not ({condition}):"
        else:
            loop_head = f"while {condition}:"
        
        lines = [loop_head]
        self.indent_level += 1
        
        lines.append(self.visit(ctx.body()))
        
        op = "+= 1" if ctx.UPPIN() else "-= 1"
        lines.append(f"{self.get_indent()}{var_name} {op}")
        
        self.indent_level -= 1
        return "\n".join(lines)
    
    def visitSwitch_stmt(self, ctx: LolcodeParser.Switch_stmtContext):
        condition_val = self.visit(ctx.expression(0)) # To co przed WTF?
        lines = [f"it = {condition_val}", f"{self.get_indent()}match it:"]
        self.indent_level += 1
        
        for i in range(len(ctx.OMG())):
            val = self.visit(ctx.expression(i+1))
            lines.append(f"{self.get_indent()}case {val}:")
            self.indent_level += 1
            lines.append(self.visit(ctx.body(i)))
            self.indent_level -= 1
            
        if ctx.OMGWTF():
            lines.append(f"{self.get_indent()}case _:")
            self.indent_level += 1
            lines.append(self.visit(ctx.body(len(ctx.body())-1)))
            self.indent_level -= 1
            
        self.indent_level -= 1
        return "\n".join(lines)
    
    def visitFunc_decl(self, ctx: LolcodeParser.Func_declContext):
        name = ctx.ID(0).getText()
        args = [ctx.ID(i).getText() for i in range(1, len(ctx.ID()))]
        arg_str = ", ".join(args)

        func_header = f"{self.get_indent()}def {name}({arg_str}):"
        
        self.indent_level += 1
        body_code=self.visit(ctx.body())
        self.indent_level -= 1
        return f"{func_header}\n{body_code}"

    def visitFunc_call(self, ctx: LolcodeParser.Func_callContext):
        name = ctx.ID().getText()
        args = [self.visit(exp) for exp in ctx.expression()]
        return f"{name}({', '.join(args)})"

    def visitReturn_stmt(self, ctx: LolcodeParser.Return_stmtContext):
        val = self.visit(ctx.expression())
        return f"{self.get_indent()}return {val}"
    
    def visitMulti_op(self, ctx: LolcodeParser.Multi_opContext):
        args = [self.visit(exp) for exp in ctx.expression()]
        func = "all" if ctx.ALL_OF() else "any"
        return f"{func}([{', '.join(args)}])"
    
    def visitUnary_op(self, ctx: LolcodeParser.Unary_opContext):
        val = self.visit(ctx.expression())
        return f"(not {val})"
    