from generated.LolcodeVisitor import LolcodeVisitor
from generated.LolcodeParser import LolcodeParser

class Lolcode2Python(LolcodeVisitor):
    def __init__(self):
        super().__init__()
        self.indent_level = 0
        self.errors = []
        self.variables = set()
        self.functions = set()
    
    def addError(self, ctx, msg):
        line = ctx.start.line
        self.errors.append(f"[Error] Linia {line}: {msg}")

    def get_indent(self):
        return "    " * self.indent_level
    
    def visitVersion(self, ctx:LolcodeParser.VersionContext):
        return f"# LOLCODE version {ctx.NUMBER().getText()}"
    
    def visitIncludes(self, ctx:LolcodeParser.IncludesContext):
        library_map = {
            "STDIO": "import sys",
            "MATH": "import math",
            "RANDOM": "import random",
            "TIME": "import time",
            "OS": "import os"
        }
        imports = []

        for lib_token in ctx.LIBRARY_NAME():
            lib = lib_token.getText()
            imports.append(
                library_map.get(lib, f"# unknown library {lib}")
            )

        return "\n".join(imports)

    
    def visitProgram(self, ctx: LolcodeParser.ProgramContext):
        lines = []
        if ctx.version():
            lines.append(self.visit(ctx.version()))
        if ctx.includes():
            lines.append(self.visit(ctx.includes()))
        lines.append("it = None\n")
        lines.append(self.visit(ctx.body()))
        return "\n".join(lines)
    
    def visitBody(self, ctx: LolcodeParser.BodyContext):
        lines = []
        if not ctx or not ctx.children:
            return ""

        for st in ctx.children:
            if isinstance(st, LolcodeParser.StatementContext):
                if st.expression():
                    expr_code = self.visit(st.expression())
                    lines.append(f"{self.get_indent()}it = {expr_code}")
                    continue
            code = self.visit(st)
            if code:
                for fragment in str(code).split('\n'):
                    line_content = fragment.rstrip()
                    if line_content:
                        if not line_content.startswith("    "):
                            lines.append(f"{self.get_indent()}{line_content}")
                        else:
                            lines.append(line_content)
        return "\n".join(lines)
    
    def ensure_body(self, body_code):
        if not body_code.strip():
            return f"{self.get_indent()}pass"
        return body_code
    
    def visitComment(self, ctx: LolcodeParser.CommentContext):
        text = ctx.getText()
        
        if text.startswith("BTW"):
            content = text[3:].strip()
            return f"# {content}"
    
        if text.startswith("OBTW"):
            inner = text[4:-4].strip()
            lines = inner.splitlines()
            
            processed_lines = []
            for line in lines:
                if line.strip():
                    processed_lines.append(f"# {line.strip()}")
                else:
                    processed_lines.append("#")
            
            return "\n".join(processed_lines)
            
        return ""
    
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
        if ctx.ID(): 
            name = ctx.ID().getText()
            if name not in self.variables:
                self.addError(ctx, f"Uzycie niezadeklarowanej zmiennej {name}")
            return name
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
        if name in self.variables:
            self.addError(ctx, f"Zmienna {name} została wcześniej zadeklarowana")
        else:
            self.variables.add(name)
        if ctx.ITZ():
            value = self.visit(ctx.expression())
            return f"{name} = {value}"
        return f"{name} = None"
    
    def visitAssign_stmt(self, ctx:LolcodeParser.Assign_stmtContext):
        name = ctx.ID().getText()
        if name not in self.variables:
            self.addError(ctx, f"Próba przypisania wartości do zmiennej {name}, która nie została wcześniej zadeklarowana")
        value = self.visit(ctx.expression())
        return f"{name} = {value}"
    
    def visitInput_stmt(self, ctx: LolcodeParser.Input_stmtContext):
        name = ctx.ID().getText()
        if name not in self.variables:
            self.addError(ctx, f"Próba wczytania danych do niezadeklarowanej zmiennej {name}")
        line1 = f"{name} = input()"
        line2 = f"{self.get_indent()}{name} = int({name}) if {name}.isnumeric() else {name}"
        return f"{line1}\n{line2}"
    
    #Instrukcja warunkowa
    def visitIf_stmt(self, ctx: LolcodeParser.If_stmtContext):
        if ctx.expression():
            condition = self.visit(ctx.expression())
        else: 
            condition = "it"
        res = [f"if {condition}:"]
        
        self.indent_level += 1

        body = self.visit(ctx.body(0))
        res.append(self.ensure_body(body))

        self.indent_level -= 1

        if ctx.NO_WAI():
            res.append("else:")
            self.indent_level += 1

            body = self.visit(ctx.body(1))
            res.append(self.ensure_body(body))

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
        if ctx.WON_OF(): return f"(bool({left}) != bool({right}))"
        if ctx.BOTH_SAEM(): return f"({left} == {right})"
        if ctx.DIFFRINT(): return f"({left} != {right})"
        return self.visitChildren(ctx)
    
    def visitLoop_stmt(self, ctx: LolcodeParser.Loop_stmtContext):
        var_name = ctx.ID(1).getText()
        if ctx.expression():
            condition = self.visit(ctx.expression())

            if ctx.TIL():
                head = f"while not {condition}:"

            elif ctx.WILE():
                head = f"while {condition}:"

            else:
                head = "while True:"
        else:
            head = "while True:"

        start = ctx.ID(0).getText()
        end = ctx.ID(2).getText()

        if start != end:
            self.addError(ctx, f"Niezgodność etykiet pętli: {start} nie równa się {end}")
        
        res = [head]
        self.indent_level += 1
        body = self.visit(ctx.body())
        res.append(self.ensure_body(body))
        op = "+= 1" if ctx.UPPIN() else "-= 1"
        res.append(f"{self.get_indent()}{var_name} {op}")
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
            body = self.visit(ctx.body(i))
            res.append(self.ensure_body(body))
            self.indent_level -= 1
            
        if ctx.OMGWTF():
            res.append(f"{self.get_indent()}case _:")
            self.indent_level += 1
            body = self.visit(ctx.body(len(ctx.body())-1))
            res.append(self.ensure_body(body))
            self.indent_level -= 1
        self.indent_level -= 1
        return "\n".join(res)
    
    def visitFunc_decl(self, ctx: LolcodeParser.Func_declContext):
        name = ctx.ID(0).getText()
        if name in self.functions:
            self.addError(ctx, f"Funkcja o nazwie {name} juz istnieje")
        else:
            self.functions.add(name)
        args = [ctx.ID(i).getText() for i in range(1, len(ctx.ID()))]
        for arg in args:
            self.variables.add(arg)
        arg_str = ", ".join(args)
        
        res = [f"def {name}({arg_str}):"]
        self.indent_level += 1
        body = self.visit(ctx.body())
        res.append(self.ensure_body(body))
        self.indent_level -= 1
        return "\n".join(res)

    def visitFunc_call(self, ctx: LolcodeParser.Func_callContext):
        name = ctx.ID().getText()
        if name not in self.functions:
            self.addError(ctx, f"Wywołanie niezdefiniowanej funkcji {name}")
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