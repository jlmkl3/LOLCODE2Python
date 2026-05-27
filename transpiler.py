from generated.LolcodeVisitor import LolcodeVisitor
from generated.LolcodeParser import LolcodeParser

class Lolcode2Python(LolcodeVisitor):
    def __init__(self, tokeny=None):
        super().__init__()
        self.tokeny = tokeny
        self.indent_level = 0

    def get_indent(self):
        return "    " * self.indent_level
    
    def visitProgram(self, ctx: LolcodeParser.ProgramContext):
        header = "it = None\n"
        body_code = self.visit(ctx.body())
        return header + body_code
    
    def visitBody(self, ctx: LolcodeParser.BodyContext):
        lines = []
        tokeny = self.tokeny
        if not tokeny:
            return ""

        start_idx = ctx.start.tokenIndex
        stop_idx = ctx.stop.tokenIndex
        
        all_tokens = tokeny.getTokens(start_idx, stop_idx)
        for st in ctx.statement():
            hidden = tokeny.getHiddenTokensToLeft(st.start.tokenIndex, -1)
            if hidden:
                for h in hidden:
                    c_text = h.text.strip()
                    if c_text.startswith("BTW"):
                        lines.append(f"{self.get_indent()}# {c_text[3:].strip()}")
                    elif c_text.startswith("OBTW"):
                        inner = c_text.replace("OBTW", "").replace("TLDR", "").strip()
                        for l in inner.split('\n'):
                            lines.append(f"{self.get_indent()}# {l.strip()}")

   
            code = self.visit(st)
            if code:
                for fragment in str(code).split('\n'):
                    if fragment.strip():
                        if fragment.startswith("    "):
                            lines.append(fragment)
                        else:
                            lines.append(f"{self.get_indent()}{fragment}")
                    else:
                        lines.append("")
        
        last_hidden = tokeny.getHiddenTokensToRight(ctx.stop.tokenIndex, -1)
        if last_hidden:
            for h in last_hidden:
                if h.text.strip().startswith("BTW"):
                    lines.append(f"{self.get_indent()}# {h.text.strip()[3:].strip()}")

        return "\n".join(lines)
    
    def visitStatement(self, ctx: LolcodeParser.StatementContext):
        if ctx.GTFO():
            parent = ctx.parentCtx
            while parent is not None:
                if isinstance(parent, LolcodeParser.Loop_stmtContext):
                    return "break"
                if isinstance(parent, LolcodeParser.Switch_stmtContext):
                    return "pass  # GTFO"
                parent = parent.parentCtx
            return "pass"
        return self.visitChildren(ctx)
    
    def visitExpression(self, ctx: LolcodeParser.ExpressionContext):
        if ctx.NUMBER(): return ctx.NUMBER().getText()
        if ctx.STRING(): return ctx.STRING().getText()
        if ctx.ID(): return ctx.ID().getText()
        if ctx.binary_op(): return self.visit(ctx.binary_op())
        if ctx.getText() == "WIN": return "True"
        if ctx.getText() == "FAIL": return "False"
        if ctx.func_call(): return self.visit(ctx.func_call())
        if ctx.multi_op(): return self.visit(ctx.multi_op())
        if ctx.unary_op(): return self.visit(ctx.unary_op())
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return f"({self.visit(ctx.expression(0))})"
        return self.visitChildren(ctx)
    
    #instrukcje podstawowe
    def visitPrint_stmt(self, ctx:LolcodeParser.Print_stmtContext):
        code = self.visit(ctx.expression())
        return f"print({code})"
    
    def visitVar_decl(self, ctx:LolcodeParser.Var_declContext):
        name = ctx.ID().getText()
        if ctx.ITZ():
            value = self.visit(ctx.expression())
            return f"{name} = {value}"
        return f"{name} = None"
    
    def visitAssign_stmt(self, ctx:LolcodeParser.Assign_stmtContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        return f"{name} = {value}"
    
    def visitInput_stmt(self, ctx:LolcodeParser.Input_stmtContext):
        name = ctx.ID().getText()
        return f"{name} = input(); {name} = int({name}) if {name}.isnumeric() else {name}"
    
    #Instrukcja warunkowa
    def visitIf_stmt(self, ctx: LolcodeParser.If_stmtContext):
        condition = self.visit(ctx.expression())
        res = [f"if {condition}:"]
        
        self.indent_level += 1
        res.append(self.visit(ctx.body(0)))
        self.indent_level -= 1

        if ctx.NO_WAI():
            res.append("else:")
            self.indent_level += 1
            res.append(self.visit(ctx.body(1)))
            self.indent_level -= 1
        return "\n".join(res)

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
        if ctx.WON_OF(): return f"({left} ^ {right})"
        if ctx.BOTH_SAEM(): return f"({left} == {right})"
        if ctx.DIFFRINT(): return f"({left} != {right})"
        return ""
    
    def visitLoop_stmt(self, ctx: LolcodeParser.Loop_stmtContext):
        var_name = ctx.ID(1).getText()
        condition = self.visit(ctx.expression())
        head = f"while not ({condition}):" if ctx.TIL() else f"while {condition}:"
        
        res = [head]
        self.indent_level += 1
        res.append(self.visit(ctx.body()))
        op = "+= 1" if ctx.UPPIN() else "-= 1"
        res.append(f"{var_name} {op}")
        self.indent_level -= 1
        return "\n".join(res)
    
    def visitSwitch_stmt(self, ctx: LolcodeParser.Switch_stmtContext):
        condition_val = self.visit(ctx.expression(0))
        res = [f"it = {condition_val}", "match it:"]
        
        self.indent_level += 1
        for i in range(len(ctx.OMG())):
            val = self.visit(ctx.expression(i+1))
            res.append(f"{self.get_indent()}case {val}:")
            self.indent_level += 1
            res.append(self.visit(ctx.body(i)))
            self.indent_level -= 1
            
        if ctx.OMGWTF():
            res.append(f"{self.get_indent()}case _:")
            self.indent_level += 1
            res.append(self.visit(ctx.body(len(ctx.body())-1)))
            self.indent_level -= 1
        self.indent_level -= 1
        return "\n".join(res)
    
    def visitFunc_decl(self, ctx: LolcodeParser.Func_declContext):
        name = ctx.ID(0).getText()
        args = [ctx.ID(i).getText() for i in range(1, len(ctx.ID()))]
        arg_str = ", ".join(args)
        
        res = [f"def {name}({arg_str}):"]
        self.indent_level += 1
        res.append(self.visit(ctx.body()))
        self.indent_level -= 1
        return "\n".join(res)

    def visitFunc_call(self, ctx: LolcodeParser.Func_callContext):
        name = ctx.ID().getText()
        args = [self.visit(exp) for exp in ctx.expression()]
        return f"{name}({', '.join(args)})"

    def visitReturn_stmt(self, ctx: LolcodeParser.Return_stmtContext):
        val = self.visit(ctx.expression())
        return f"return {val}"
    
    def visitMulti_op(self, ctx: LolcodeParser.Multi_opContext):
        args = [self.visit(exp) for exp in ctx.expression()]
        func = "all" if ctx.ALL_OF() else "any"
        return f"{func}([{', '.join(args)}])"
    
    def visitUnary_op(self, ctx: LolcodeParser.Unary_opContext):
        val = self.visit(ctx.expression())
        return f"(not {val})"