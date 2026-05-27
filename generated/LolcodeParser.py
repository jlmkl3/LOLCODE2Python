# Generated from Lolcode.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,57,213,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,3,0,41,
        8,0,1,0,3,0,44,8,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,
        3,5,3,58,8,3,10,3,12,3,61,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,3,4,74,8,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,83,8,6,1,7,
        1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,3,9,94,8,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,3,9,104,8,9,1,9,3,9,107,8,9,1,9,1,9,1,10,1,10,3,10,113,
        8,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,122,8,10,10,10,12,10,
        125,9,10,1,10,1,10,1,10,3,10,130,8,10,1,10,3,10,133,8,10,1,10,1,
        10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,143,8,11,1,11,3,11,146,8,11,
        1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,5,12,157,8,12,10,12,
        12,12,160,9,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,5,13,169,8,13,
        10,13,12,13,172,9,13,1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,192,8,15,1,16,
        1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,5,18,206,
        8,18,10,18,12,18,209,9,18,1,18,1,18,1,18,0,0,19,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,0,4,1,0,38,39,1,0,41,42,2,0,
        11,20,24,25,1,0,22,23,229,0,38,1,0,0,0,2,49,1,0,0,0,4,51,1,0,0,0,
        6,59,1,0,0,0,8,73,1,0,0,0,10,75,1,0,0,0,12,78,1,0,0,0,14,84,1,0,
        0,0,16,88,1,0,0,0,18,91,1,0,0,0,20,110,1,0,0,0,22,136,1,0,0,0,24,
        152,1,0,0,0,26,164,1,0,0,0,28,175,1,0,0,0,30,191,1,0,0,0,32,193,
        1,0,0,0,34,198,1,0,0,0,36,201,1,0,0,0,38,40,5,4,0,0,39,41,3,2,1,
        0,40,39,1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,0,42,44,3,4,2,0,43,42,
        1,0,0,0,43,44,1,0,0,0,44,45,1,0,0,0,45,46,5,56,0,0,46,47,3,6,3,0,
        47,48,5,5,0,0,48,1,1,0,0,0,49,50,5,51,0,0,50,3,1,0,0,0,51,52,5,49,
        0,0,52,53,5,50,0,0,53,54,5,1,0,0,54,5,1,0,0,0,55,58,3,8,4,0,56,58,
        5,56,0,0,57,55,1,0,0,0,57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,
        59,60,1,0,0,0,60,7,1,0,0,0,61,59,1,0,0,0,62,74,3,10,5,0,63,74,3,
        12,6,0,64,74,3,14,7,0,65,74,3,16,8,0,66,74,3,18,9,0,67,74,3,20,10,
        0,68,74,3,22,11,0,69,74,3,24,12,0,70,74,3,26,13,0,71,74,3,28,14,
        0,72,74,5,35,0,0,73,62,1,0,0,0,73,63,1,0,0,0,73,64,1,0,0,0,73,65,
        1,0,0,0,73,66,1,0,0,0,73,67,1,0,0,0,73,68,1,0,0,0,73,69,1,0,0,0,
        73,70,1,0,0,0,73,71,1,0,0,0,73,72,1,0,0,0,74,9,1,0,0,0,75,76,5,6,
        0,0,76,77,3,30,15,0,77,11,1,0,0,0,78,79,5,8,0,0,79,82,5,52,0,0,80,
        81,5,9,0,0,81,83,3,30,15,0,82,80,1,0,0,0,82,83,1,0,0,0,83,13,1,0,
        0,0,84,85,5,52,0,0,85,86,5,10,0,0,86,87,3,30,15,0,87,15,1,0,0,0,
        88,89,5,7,0,0,89,90,5,52,0,0,90,17,1,0,0,0,91,93,3,30,15,0,92,94,
        5,56,0,0,93,92,1,0,0,0,93,94,1,0,0,0,94,95,1,0,0,0,95,96,5,28,0,
        0,96,97,5,56,0,0,97,98,5,29,0,0,98,99,5,56,0,0,99,103,3,6,3,0,100,
        101,5,30,0,0,101,102,5,56,0,0,102,104,3,6,3,0,103,100,1,0,0,0,103,
        104,1,0,0,0,104,106,1,0,0,0,105,107,5,56,0,0,106,105,1,0,0,0,106,
        107,1,0,0,0,107,108,1,0,0,0,108,109,5,31,0,0,109,19,1,0,0,0,110,
        112,3,30,15,0,111,113,5,56,0,0,112,111,1,0,0,0,112,113,1,0,0,0,113,
        114,1,0,0,0,114,115,5,32,0,0,115,123,5,56,0,0,116,117,5,33,0,0,117,
        118,3,30,15,0,118,119,5,56,0,0,119,120,3,6,3,0,120,122,1,0,0,0,121,
        116,1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,
        129,1,0,0,0,125,123,1,0,0,0,126,127,5,34,0,0,127,128,5,56,0,0,128,
        130,3,6,3,0,129,126,1,0,0,0,129,130,1,0,0,0,130,132,1,0,0,0,131,
        133,5,56,0,0,132,131,1,0,0,0,132,133,1,0,0,0,133,134,1,0,0,0,134,
        135,5,31,0,0,135,21,1,0,0,0,136,137,5,36,0,0,137,138,5,52,0,0,138,
        139,7,0,0,0,139,140,5,40,0,0,140,145,5,52,0,0,141,143,7,1,0,0,142,
        141,1,0,0,0,142,143,1,0,0,0,143,144,1,0,0,0,144,146,3,30,15,0,145,
        142,1,0,0,0,145,146,1,0,0,0,146,147,1,0,0,0,147,148,5,56,0,0,148,
        149,3,6,3,0,149,150,5,37,0,0,150,151,5,52,0,0,151,23,1,0,0,0,152,
        153,5,43,0,0,153,158,5,52,0,0,154,155,5,26,0,0,155,157,5,52,0,0,
        156,154,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,158,159,1,0,0,0,
        159,161,1,0,0,0,160,158,1,0,0,0,161,162,3,6,3,0,162,163,5,44,0,0,
        163,25,1,0,0,0,164,165,5,46,0,0,165,170,5,52,0,0,166,167,5,26,0,
        0,167,169,3,30,15,0,168,166,1,0,0,0,169,172,1,0,0,0,170,168,1,0,
        0,0,170,171,1,0,0,0,171,173,1,0,0,0,172,170,1,0,0,0,173,174,5,27,
        0,0,174,27,1,0,0,0,175,176,5,45,0,0,176,177,3,30,15,0,177,29,1,0,
        0,0,178,192,5,51,0,0,179,192,5,53,0,0,180,192,5,52,0,0,181,192,5,
        47,0,0,182,192,5,48,0,0,183,192,3,32,16,0,184,192,3,34,17,0,185,
        192,3,36,18,0,186,192,3,26,13,0,187,188,5,2,0,0,188,189,3,30,15,
        0,189,190,5,3,0,0,190,192,1,0,0,0,191,178,1,0,0,0,191,179,1,0,0,
        0,191,180,1,0,0,0,191,181,1,0,0,0,191,182,1,0,0,0,191,183,1,0,0,
        0,191,184,1,0,0,0,191,185,1,0,0,0,191,186,1,0,0,0,191,187,1,0,0,
        0,192,31,1,0,0,0,193,194,7,2,0,0,194,195,3,30,15,0,195,196,5,26,
        0,0,196,197,3,30,15,0,197,33,1,0,0,0,198,199,5,21,0,0,199,200,3,
        30,15,0,200,35,1,0,0,0,201,202,7,3,0,0,202,207,3,30,15,0,203,204,
        5,26,0,0,204,206,3,30,15,0,205,203,1,0,0,0,206,209,1,0,0,0,207,205,
        1,0,0,0,207,208,1,0,0,0,208,210,1,0,0,0,209,207,1,0,0,0,210,211,
        5,27,0,0,211,37,1,0,0,0,19,40,43,57,59,73,82,93,103,106,112,123,
        129,132,142,145,158,170,191,207
    ]

class LolcodeParser ( Parser ):

    grammarFileName = "Lolcode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'?'", "'('", "')'", "'HAI'", "'KTHXBYE'", 
                     "'VISIBLE'", "'GIMMEH'", "'I HAS A'", "'ITZ'", "'R'", 
                     "'SUM OF'", "'DIFF OF'", "'PRODUKT OF'", "'QUOSHUNT OF'", 
                     "'MOD OF'", "'BIGGR OF'", "'SMALLR OF'", "'BOTH OF'", 
                     "'EITHER OF'", "'WON OF'", "'NOT'", "'ALL OF'", "'ANY OF'", 
                     "'BOTH SAEM'", "'DIFFRINT'", "'AN'", "'MKAY'", "'O RLY?'", 
                     "'YA RLY'", "'NO WAI'", "'OIC'", "'WTF?'", "'OMG'", 
                     "'OMGWTF'", "'GTFO'", "'IM IN YR'", "'IM OUTTA YR'", 
                     "'UPPIN'", "'NERFIN'", "'YR'", "'TIL'", "'WILE'", "'HOW IZ I'", 
                     "'IF U SAY SO'", "'FOUND YR'", "'I IZ'", "'WIN'", "'FAIL'", 
                     "'CAN HAS'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "HAI", "KTHXBYE", "VISIBLE", "GIMMEH", "IHASA", "ITZ", 
                      "R", "SUM_OF", "DIFF_OF", "PRODUKT_OF", "QUOSHUNT_OF", 
                      "MOD_OF", "BIGGR_OF", "SMALLR_OF", "BOTH_OF", "EITHER_OF", 
                      "WON_OF", "NOT", "ALL_OF", "ANY_OF", "BOTH_SAEM", 
                      "DIFFRINT", "AN", "MKAY", "O_RLY", "YA_RLY", "NO_WAI", 
                      "OIC", "WTF", "OMG", "OMGWTF", "GTFO", "IM_IN_YR", 
                      "IM_OUTTA_YR", "UPPIN", "NERFIN", "YR", "TIL", "WILE", 
                      "HOW_IZ_I", "IF_U_SAY_SO", "FOUND_YR", "I_IZ", "WIN", 
                      "FAIL", "CANHAS", "LIBRARY_NAME", "NUMBER", "ID", 
                      "STRING", "COMMENT", "BLOCK_COMMENT", "NL", "WS" ]

    RULE_program = 0
    RULE_version = 1
    RULE_includes = 2
    RULE_body = 3
    RULE_statement = 4
    RULE_print_stmt = 5
    RULE_var_decl = 6
    RULE_assign_stmt = 7
    RULE_input_stmt = 8
    RULE_if_stmt = 9
    RULE_switch_stmt = 10
    RULE_loop_stmt = 11
    RULE_func_decl = 12
    RULE_func_call = 13
    RULE_return_stmt = 14
    RULE_expression = 15
    RULE_binary_op = 16
    RULE_unary_op = 17
    RULE_multi_op = 18

    ruleNames =  [ "program", "version", "includes", "body", "statement", 
                   "print_stmt", "var_decl", "assign_stmt", "input_stmt", 
                   "if_stmt", "switch_stmt", "loop_stmt", "func_decl", "func_call", 
                   "return_stmt", "expression", "binary_op", "unary_op", 
                   "multi_op" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    HAI=4
    KTHXBYE=5
    VISIBLE=6
    GIMMEH=7
    IHASA=8
    ITZ=9
    R=10
    SUM_OF=11
    DIFF_OF=12
    PRODUKT_OF=13
    QUOSHUNT_OF=14
    MOD_OF=15
    BIGGR_OF=16
    SMALLR_OF=17
    BOTH_OF=18
    EITHER_OF=19
    WON_OF=20
    NOT=21
    ALL_OF=22
    ANY_OF=23
    BOTH_SAEM=24
    DIFFRINT=25
    AN=26
    MKAY=27
    O_RLY=28
    YA_RLY=29
    NO_WAI=30
    OIC=31
    WTF=32
    OMG=33
    OMGWTF=34
    GTFO=35
    IM_IN_YR=36
    IM_OUTTA_YR=37
    UPPIN=38
    NERFIN=39
    YR=40
    TIL=41
    WILE=42
    HOW_IZ_I=43
    IF_U_SAY_SO=44
    FOUND_YR=45
    I_IZ=46
    WIN=47
    FAIL=48
    CANHAS=49
    LIBRARY_NAME=50
    NUMBER=51
    ID=52
    STRING=53
    COMMENT=54
    BLOCK_COMMENT=55
    NL=56
    WS=57

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HAI(self):
            return self.getToken(LolcodeParser.HAI, 0)

        def NL(self):
            return self.getToken(LolcodeParser.NL, 0)

        def body(self):
            return self.getTypedRuleContext(LolcodeParser.BodyContext,0)


        def KTHXBYE(self):
            return self.getToken(LolcodeParser.KTHXBYE, 0)

        def version(self):
            return self.getTypedRuleContext(LolcodeParser.VersionContext,0)


        def includes(self):
            return self.getTypedRuleContext(LolcodeParser.IncludesContext,0)


        def getRuleIndex(self):
            return LolcodeParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = LolcodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(LolcodeParser.HAI)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 39
                self.version()


            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 42
                self.includes()


            self.state = 45
            self.match(LolcodeParser.NL)
            self.state = 46
            self.body()
            self.state = 47
            self.match(LolcodeParser.KTHXBYE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VersionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(LolcodeParser.NUMBER, 0)

        def getRuleIndex(self):
            return LolcodeParser.RULE_version

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVersion" ):
                listener.enterVersion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVersion" ):
                listener.exitVersion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVersion" ):
                return visitor.visitVersion(self)
            else:
                return visitor.visitChildren(self)




    def version(self):

        localctx = LolcodeParser.VersionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_version)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(LolcodeParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncludesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CANHAS(self):
            return self.getToken(LolcodeParser.CANHAS, 0)

        def LIBRARY_NAME(self):
            return self.getToken(LolcodeParser.LIBRARY_NAME, 0)

        def getRuleIndex(self):
            return LolcodeParser.RULE_includes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncludes" ):
                listener.enterIncludes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncludes" ):
                listener.exitIncludes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncludes" ):
                return visitor.visitIncludes(self)
            else:
                return visitor.visitChildren(self)




    def includes(self):

        localctx = LolcodeParser.IncludesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_includes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(LolcodeParser.CANHAS)
            self.state = 52
            self.match(LolcodeParser.LIBRARY_NAME)
            self.state = 53
            self.match(LolcodeParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LolcodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(LolcodeParser.StatementContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(LolcodeParser.NL)
            else:
                return self.getToken(LolcodeParser.NL, i)

        def getRuleIndex(self):
            return LolcodeParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = LolcodeParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 57
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [2, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 35, 36, 43, 45, 46, 47, 48, 51, 52, 53]:
                        self.state = 55
                        self.statement()
                        pass
                    elif token in [56]:
                        self.state = 56
                        self.match(LolcodeParser.NL)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def print_stmt(self):
            return self.getTypedRuleContext(LolcodeParser.Print_stmtContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(LolcodeParser.Var_declContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(LolcodeParser.Assign_stmtContext,0)


        def input_stmt(self):
            return self.getTypedRuleContext(LolcodeParser.Input_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(LolcodeParser.If_stmtContext,0)


        def switch_stmt(self):
            return self.getTypedRuleContext(LolcodeParser.Switch_stmtContext,0)


        def loop_stmt(self):
            return self.getTypedRuleContext(LolcodeParser.Loop_stmtContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(LolcodeParser.Func_declContext,0)


        def func_call(self):
            return self.getTypedRuleContext(LolcodeParser.Func_callContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(LolcodeParser.Return_stmtContext,0)


        def GTFO(self):
            return self.getToken(LolcodeParser.GTFO, 0)

        def getRuleIndex(self):
            return LolcodeParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = LolcodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.print_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.var_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.assign_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.input_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 66
                self.if_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 67
                self.switch_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 68
                self.loop_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 69
                self.func_decl()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 70
                self.func_call()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 71
                self.return_stmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 72
                self.match(LolcodeParser.GTFO)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VISIBLE(self):
            return self.getToken(LolcodeParser.VISIBLE, 0)

        def expression(self):
            return self.getTypedRuleContext(LolcodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LolcodeParser.RULE_print_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stmt" ):
                listener.enterPrint_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stmt" ):
                listener.exitPrint_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_stmt" ):
                return visitor.visitPrint_stmt(self)
            else:
                return visitor.visitChildren(self)




    def print_stmt(self):

        localctx = LolcodeParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_print_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(LolcodeParser.VISIBLE)
            self.state = 76
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IHASA(self):
            return self.getToken(LolcodeParser.IHASA, 0)

        def ID(self):
            return self.getToken(LolcodeParser.ID, 0)

        def ITZ(self):
            return self.getToken(LolcodeParser.ITZ, 0)

        def expression(self):
            return self.getTypedRuleContext(LolcodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LolcodeParser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = LolcodeParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(LolcodeParser.IHASA)
            self.state = 79
            self.match(LolcodeParser.ID)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 80
                self.match(LolcodeParser.ITZ)
                self.state = 81
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LolcodeParser.ID, 0)

        def R(self):
            return self.getToken(LolcodeParser.R, 0)

        def expression(self):
            return self.getTypedRuleContext(LolcodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LolcodeParser.RULE_assign_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_stmt" ):
                listener.enterAssign_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_stmt" ):
                listener.exitAssign_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = LolcodeParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(LolcodeParser.ID)
            self.state = 85
            self.match(LolcodeParser.R)
            self.state = 86
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Input_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GIMMEH(self):
            return self.getToken(LolcodeParser.GIMMEH, 0)

        def ID(self):
            return self.getToken(LolcodeParser.ID, 0)

        def getRuleIndex(self):
            return LolcodeParser.RULE_input_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput_stmt" ):
                listener.enterInput_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput_stmt" ):
                listener.exitInput_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput_stmt" ):
                return visitor.visitInput_stmt(self)
            else:
                return visitor.visitChildren(self)




    def input_stmt(self):

        localctx = LolcodeParser.Input_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_input_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(LolcodeParser.GIMMEH)
            self.state = 89
            self.match(LolcodeParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LolcodeParser.ExpressionContext,0)


        def O_RLY(self):
            return self.getToken(LolcodeParser.O_RLY, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(LolcodeParser.NL)
            else:
                return self.getToken(LolcodeParser.NL, i)

        def YA_RLY(self):
            return self.getToken(LolcodeParser.YA_RLY, 0)

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LolcodeParser.BodyContext)
            else:
                return self.getTypedRuleContext(LolcodeParser.BodyContext,i)


        def OIC(self):
            return self.getToken(LolcodeParser.OIC, 0)

        def NO_WAI(self):
            return self.getToken(LolcodeParser.NO_WAI, 0)

        def getRuleIndex(self):
            return LolcodeParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = LolcodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.expression()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56:
                self.state = 92
                self.match(LolcodeParser.NL)


            self.state = 95
            self.match(LolcodeParser.O_RLY)
            self.state = 96
            self.match(LolcodeParser.NL)
            self.state = 97
            self.match(LolcodeParser.YA_RLY)
            self.state = 98
            self.match(LolcodeParser.NL)
            self.state = 99
            self.body()
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 100
                self.match(LolcodeParser.NO_WAI)
                self.state = 101
                self.match(LolcodeParser.NL)
                self.state = 102
                self.body()


            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56:
                self.state = 105
                self.match(LolcodeParser.NL)


            self.state = 108
            self.match(LolcodeParser.OIC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LolcodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LolcodeParser.ExpressionContext,i)


        def WTF(self):
            return self.getToken(LolcodeParser.WTF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(LolcodeParser.NL)
            else:
                return self.getToken(LolcodeParser.NL, i)

        def OIC(self):
            return self.getToken(LolcodeParser.OIC, 0)

        def OMG(self, i:int=None):
            if i is None:
                return self.getTokens(LolcodeParser.OMG)
            else:
                return self.getToken(LolcodeParser.OMG, i)

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LolcodeParser.BodyContext)
            else:
                return self.getTypedRuleContext(LolcodeParser.BodyContext,i)


        def OMGWTF(self):
            return self.getToken(LolcodeParser.OMGWTF, 0)

        def getRuleIndex(self):
            return LolcodeParser.RULE_switch_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_stmt" ):
                listener.enterSwitch_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_stmt" ):
                listener.exitSwitch_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitch_stmt" ):
                return visitor.visitSwitch_stmt(self)
            else:
                return visitor.visitChildren(self)




    def switch_stmt(self):

        localctx = LolcodeParser.Switch_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_switch_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.expression()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56:
                self.state = 111
                self.match(LolcodeParser.NL)


            self.state = 114
            self.match(LolcodeParser.WTF)
            self.state = 115
            self.match(LolcodeParser.NL)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 116
                self.match(LolcodeParser.OMG)
                self.state = 117
                self.expression()
                self.state = 118
                self.match(LolcodeParser.NL)
                self.state = 119
                self.body()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 126
                self.match(LolcodeParser.OMGWTF)
                self.state = 127
                self.match(LolcodeParser.NL)
                self.state = 128
                self.body()


            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56:
                self.state = 131
                self.match(LolcodeParser.NL)


            self.state = 134
            self.match(LolcodeParser.OIC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IM_IN_YR(self):
            return self.getToken(LolcodeParser.IM_IN_YR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LolcodeParser.ID)
            else:
                return self.getToken(LolcodeParser.ID, i)

        def YR(self):
            return self.getToken(LolcodeParser.YR, 0)

        def NL(self):
            return self.getToken(LolcodeParser.NL, 0)

        def body(self):
            return self.getTypedRuleContext(LolcodeParser.BodyContext,0)


        def IM_OUTTA_YR(self):
            return self.getToken(LolcodeParser.IM_OUTTA_YR, 0)

        def UPPIN(self):
            return self.getToken(LolcodeParser.UPPIN, 0)

        def NERFIN(self):
            return self.getToken(LolcodeParser.NERFIN, 0)

        def expression(self):
            return self.getTypedRuleContext(LolcodeParser.ExpressionContext,0)


        def TIL(self):
            return self.getToken(LolcodeParser.TIL, 0)

        def WILE(self):
            return self.getToken(LolcodeParser.WILE, 0)

        def getRuleIndex(self):
            return LolcodeParser.RULE_loop_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_stmt" ):
                listener.enterLoop_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_stmt" ):
                listener.exitLoop_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_stmt" ):
                return visitor.visitLoop_stmt(self)
            else:
                return visitor.visitChildren(self)




    def loop_stmt(self):

        localctx = LolcodeParser.Loop_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_loop_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(LolcodeParser.IM_IN_YR)
            self.state = 137
            self.match(LolcodeParser.ID)
            self.state = 138
            _la = self._input.LA(1)
            if not(_la==38 or _la==39):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 139
            self.match(LolcodeParser.YR)
            self.state = 140
            self.match(LolcodeParser.ID)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 16261777041913860) != 0):
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==41 or _la==42:
                    self.state = 141
                    _la = self._input.LA(1)
                    if not(_la==41 or _la==42):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 144
                self.expression()


            self.state = 147
            self.match(LolcodeParser.NL)
            self.state = 148
            self.body()
            self.state = 149
            self.match(LolcodeParser.IM_OUTTA_YR)
            self.state = 150
            self.match(LolcodeParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HOW_IZ_I(self):
            return self.getToken(LolcodeParser.HOW_IZ_I, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LolcodeParser.ID)
            else:
                return self.getToken(LolcodeParser.ID, i)

        def body(self):
            return self.getTypedRuleContext(LolcodeParser.BodyContext,0)


        def IF_U_SAY_SO(self):
            return self.getToken(LolcodeParser.IF_U_SAY_SO, 0)

        def AN(self, i:int=None):
            if i is None:
                return self.getTokens(LolcodeParser.AN)
            else:
                return self.getToken(LolcodeParser.AN, i)

        def getRuleIndex(self):
            return LolcodeParser.RULE_func_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_decl" ):
                listener.enterFunc_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_decl" ):
                listener.exitFunc_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = LolcodeParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(LolcodeParser.HOW_IZ_I)
            self.state = 153
            self.match(LolcodeParser.ID)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 154
                self.match(LolcodeParser.AN)
                self.state = 155
                self.match(LolcodeParser.ID)
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 161
            self.body()
            self.state = 162
            self.match(LolcodeParser.IF_U_SAY_SO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def I_IZ(self):
            return self.getToken(LolcodeParser.I_IZ, 0)

        def ID(self):
            return self.getToken(LolcodeParser.ID, 0)

        def MKAY(self):
            return self.getToken(LolcodeParser.MKAY, 0)

        def AN(self, i:int=None):
            if i is None:
                return self.getTokens(LolcodeParser.AN)
            else:
                return self.getToken(LolcodeParser.AN, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LolcodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LolcodeParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LolcodeParser.RULE_func_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_call" ):
                listener.enterFunc_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_call" ):
                listener.exitFunc_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = LolcodeParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(LolcodeParser.I_IZ)
            self.state = 165
            self.match(LolcodeParser.ID)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 166
                self.match(LolcodeParser.AN)
                self.state = 167
                self.expression()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 173
            self.match(LolcodeParser.MKAY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOUND_YR(self):
            return self.getToken(LolcodeParser.FOUND_YR, 0)

        def expression(self):
            return self.getTypedRuleContext(LolcodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LolcodeParser.RULE_return_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stmt" ):
                listener.enterReturn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stmt" ):
                listener.exitReturn_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = LolcodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(LolcodeParser.FOUND_YR)
            self.state = 176
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(LolcodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(LolcodeParser.STRING, 0)

        def ID(self):
            return self.getToken(LolcodeParser.ID, 0)

        def WIN(self):
            return self.getToken(LolcodeParser.WIN, 0)

        def FAIL(self):
            return self.getToken(LolcodeParser.FAIL, 0)

        def binary_op(self):
            return self.getTypedRuleContext(LolcodeParser.Binary_opContext,0)


        def unary_op(self):
            return self.getTypedRuleContext(LolcodeParser.Unary_opContext,0)


        def multi_op(self):
            return self.getTypedRuleContext(LolcodeParser.Multi_opContext,0)


        def func_call(self):
            return self.getTypedRuleContext(LolcodeParser.Func_callContext,0)


        def expression(self):
            return self.getTypedRuleContext(LolcodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LolcodeParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = LolcodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression)
        try:
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(LolcodeParser.NUMBER)
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.match(LolcodeParser.STRING)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.match(LolcodeParser.ID)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 4)
                self.state = 181
                self.match(LolcodeParser.WIN)
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 5)
                self.state = 182
                self.match(LolcodeParser.FAIL)
                pass
            elif token in [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 24, 25]:
                self.enterOuterAlt(localctx, 6)
                self.state = 183
                self.binary_op()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 7)
                self.state = 184
                self.unary_op()
                pass
            elif token in [22, 23]:
                self.enterOuterAlt(localctx, 8)
                self.state = 185
                self.multi_op()
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 9)
                self.state = 186
                self.func_call()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 10)
                self.state = 187
                self.match(LolcodeParser.T__1)
                self.state = 188
                self.expression()
                self.state = 189
                self.match(LolcodeParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Binary_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LolcodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LolcodeParser.ExpressionContext,i)


        def AN(self):
            return self.getToken(LolcodeParser.AN, 0)

        def SUM_OF(self):
            return self.getToken(LolcodeParser.SUM_OF, 0)

        def DIFF_OF(self):
            return self.getToken(LolcodeParser.DIFF_OF, 0)

        def PRODUKT_OF(self):
            return self.getToken(LolcodeParser.PRODUKT_OF, 0)

        def QUOSHUNT_OF(self):
            return self.getToken(LolcodeParser.QUOSHUNT_OF, 0)

        def MOD_OF(self):
            return self.getToken(LolcodeParser.MOD_OF, 0)

        def BIGGR_OF(self):
            return self.getToken(LolcodeParser.BIGGR_OF, 0)

        def SMALLR_OF(self):
            return self.getToken(LolcodeParser.SMALLR_OF, 0)

        def BOTH_OF(self):
            return self.getToken(LolcodeParser.BOTH_OF, 0)

        def EITHER_OF(self):
            return self.getToken(LolcodeParser.EITHER_OF, 0)

        def WON_OF(self):
            return self.getToken(LolcodeParser.WON_OF, 0)

        def BOTH_SAEM(self):
            return self.getToken(LolcodeParser.BOTH_SAEM, 0)

        def DIFFRINT(self):
            return self.getToken(LolcodeParser.DIFFRINT, 0)

        def getRuleIndex(self):
            return LolcodeParser.RULE_binary_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_op" ):
                listener.enterBinary_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_op" ):
                listener.exitBinary_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary_op" ):
                return visitor.visitBinary_op(self)
            else:
                return visitor.visitChildren(self)




    def binary_op(self):

        localctx = LolcodeParser.Binary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_binary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 52426752) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 194
            self.expression()
            self.state = 195
            self.match(LolcodeParser.AN)
            self.state = 196
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(LolcodeParser.NOT, 0)

        def expression(self):
            return self.getTypedRuleContext(LolcodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LolcodeParser.RULE_unary_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_op" ):
                listener.enterUnary_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_op" ):
                listener.exitUnary_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_op" ):
                return visitor.visitUnary_op(self)
            else:
                return visitor.visitChildren(self)




    def unary_op(self):

        localctx = LolcodeParser.Unary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_unary_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(LolcodeParser.NOT)
            self.state = 199
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LolcodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LolcodeParser.ExpressionContext,i)


        def MKAY(self):
            return self.getToken(LolcodeParser.MKAY, 0)

        def ALL_OF(self):
            return self.getToken(LolcodeParser.ALL_OF, 0)

        def ANY_OF(self):
            return self.getToken(LolcodeParser.ANY_OF, 0)

        def AN(self, i:int=None):
            if i is None:
                return self.getTokens(LolcodeParser.AN)
            else:
                return self.getToken(LolcodeParser.AN, i)

        def getRuleIndex(self):
            return LolcodeParser.RULE_multi_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulti_op" ):
                listener.enterMulti_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulti_op" ):
                listener.exitMulti_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulti_op" ):
                return visitor.visitMulti_op(self)
            else:
                return visitor.visitChildren(self)




    def multi_op(self):

        localctx = LolcodeParser.Multi_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_multi_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 202
            self.expression()
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 203
                self.match(LolcodeParser.AN)
                self.state = 204
                self.expression()
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 210
            self.match(LolcodeParser.MKAY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





