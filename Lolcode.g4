grammar Lolcode;

//Parser
program: HAI version? includes? NL body KTHXBYE;

version: NUMBER;

includes: CANHAS LIBRARY_NAME '?';

body: (statement | NL)*;

statement:
	print_stmt
	| var_decl
	| assign_stmt
	| input_stmt
	| if_stmt
	| switch_stmt
	| loop_stmt
	| func_decl
	| func_call
	| return_stmt
	| GTFO;

//Instrukcje podstawowe
print_stmt: VISIBLE expression;
var_decl: IHASA ID (ITZ expression)?;
assign_stmt: ID R expression;
input_stmt: GIMMEH ID;

//Instrukcja warunkowa
if_stmt:
	expression NL? O_RLY NL YA_RLY NL body (NO_WAI NL body)? NL? OIC;

//Instrukcja wyboru
switch_stmt:
	expression NL? WTF NL (OMG expression NL body)* (
		OMGWTF NL body
	)? NL? OIC;

//Pętla
loop_stmt:
	IM_IN_YR ID (UPPIN | NERFIN) YR ID ((TIL | WILE)? expression)? NL body IM_OUTTA_YR ID;

//Funkcje
func_decl: HOW_IZ_I ID (AN ID)* NL body IF_U_SAY_SO;
func_call: I_IZ ID (AN expression)* MKAY;
return_stmt: FOUND_YR expression;

//Wyrażenia
expression:
	NUMBER
	| STRING
	| ID
	| WIN
	| FAIL
	| binary_op
	| unary_op
	| multi_op
	| func_call
	| '(' expression ')';

//Operatory dwuargumentowe
binary_op: (
		SUM_OF
		| DIFF_OF
		| PRODUKT_OF
		| QUOSHUNT_OF
		| MOD_OF
		| BIGGR_OF
		| SMALLR_OF
		| BOTH_OF
		| EITHER_OF
		| WON_OF
		| BOTH_SAEM
		| DIFFRINT
	) expression AN expression;

//Operatory jednoargumentowe
unary_op: NOT expression;

//Operatory wieloargumentowe
multi_op: ( ALL_OF | ANY_OF) expression (AN expression)* MKAY;

//Lekser
HAI: 'HAI';
KTHXBYE: 'KTHXBYE';
VISIBLE: 'VISIBLE';
GIMMEH: 'GIMMEH';
IHASA: 'I HAS A';
ITZ: 'ITZ';
R: 'R';
SUM_OF: 'SUM OF';
DIFF_OF: 'DIFF OF';
PRODUKT_OF: 'PRODUKT OF';
QUOSHUNT_OF: 'QUOSHUNT OF';
MOD_OF: 'MOD OF';
BIGGR_OF: 'BIGGR OF';
SMALLR_OF: 'SMALLR OF';
BOTH_OF: 'BOTH OF';
EITHER_OF: 'EITHER OF';
WON_OF: 'WON OF';
NOT: 'NOT';
ALL_OF: 'ALL OF';
ANY_OF: 'ANY OF';
BOTH_SAEM: 'BOTH SAEM';
DIFFRINT: 'DIFFRINT';
AN: 'AN';
MKAY: 'MKAY';
O_RLY: 'O RLY?';
YA_RLY: 'YA RLY';
NO_WAI: 'NO WAI';
OIC: 'OIC';
WTF: 'WTF?';
OMG: 'OMG';
OMGWTF: 'OMGWTF';
GTFO: 'GTFO';
IM_IN_YR: 'IM IN YR';
IM_OUTTA_YR: 'IM OUTTA YR';
UPPIN: 'UPPIN';
NERFIN: 'NERFIN';
YR: 'YR';
TIL: 'TIL';
WILE: 'WILE';
HOW_IZ_I: 'HOW IZ I';
IF_U_SAY_SO: 'IF U SAY SO';
FOUND_YR: 'FOUND YR';
I_IZ: 'I IZ';
WIN: 'WIN';
FAIL: 'FAIL';

//Dodatkowe
CANHAS: 'CAN HAS';
LIBRARY_NAME: [A-Z]+;
NUMBER: [0-9]+ ('.' [0-9]+)?;
ID: [a-zA-Z][a-zA-Z0-9_]*;
STRING: '"' .*? '"';

//Komentarze i białe znaki
COMMENT: 'BTW' ~[\r\n]* -> channel(HIDDEN);
BLOCK_COMMENT: 'OBTW' .*? 'TLDR' -> channel(HIDDEN);
NL: '\r'? '\n';
WS: [ \t]+ -> skip;