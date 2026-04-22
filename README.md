# LOLCODE to Python transpiler
# Dane kontaktowe 
### Maria Pichór: mpichor@student.agh.edu.pl
### Julia Mikuła: jmikula@student.agh.edu.pl

# Założenia

### Cel programu:
Program ma na celu zamianę kodu w LOLCODE na kod w Python na podstawie dokumentacji: https://lolcode.org/

### Rodzaj translatora:
Transpiler

### Planowany wynik działania programu:
Kod w Python

### Planowany język implementacji:
Python

# Tabela tokenów
| Nazwa tokenu   | Regex        | Opis |
|----------------|-------------|------|
| HAI            | HAI         | Początek programu (odpowiednik main) |
| KTHXBYE        | KTHXBYE     | Koniec programu |
| VISIBLE        | VISIBLE     | Wyświetla wartość na ekranie (print) |
| GIMMEH         | GIMMEH      | Wczytuje dane od użytkownika |
| I_HAS_A        | I HAS A     | Deklaracja zmiennej |
| ITZ            | ITZ         | Inicjalizacja wartości zmiennej |
| R              | R           | Przypisanie wartości |
| SUM_OF         | SUM OF      | Dodawanie |
| DIFF_OF        | DIFF OF     | Odejmowanie |
| PRODUKT_OF     | PRODUKT OF  | Mnożenie |
| QUOSHUNT_OF    | QUOSHUNT OF | Dzielenie |
| MOD_OF         | MOD OF      | Reszta z dzielenia |
| BIGGR_OF       | BIGGR OF    | Maksimum z dwóch wartości |
| SMALLR_OF      | SMALLR OF   | Minimum z dwóch wartości |
| BOTH_OF        | BOTH OF     | AND logiczne (2 wartości) |
| EITHER_OF      | EITHER OF   | OR logiczne (2 wartości) |
| WON_OF         | WON OF      | XOR logiczne |
| NOT            | NOT         | Negacja logiczna |
| ALL_OF         | ALL OF      | AND dla wielu argumentów |
| ANY_OF         | ANY OF      | OR dla wielu argumentów |
| BOTH_SAEM      | BOTH SAEM   | Porównanie równości (==) |
| DIFFRINT       | DIFFRINT    | Porównanie nierówności (!=) |
| AN             | AN          | Separator argumentów |
| MKAY           | MKAY        | Zamyka listę ALL OF / ANY OF |
| O_RLY?         | O RLY?      | Instrukcja warunkowa (if) |
| YA_RLY         | YA RLY      | Blok if (true) |
| NO_WAI         | NO WAI      | Blok else (false) |
| OIC            | OIC         | Koniec warunku |
| WTF?           | WTF?        | Switch |
| OMG            | OMG         | Case |
| OMGWTF         | OMGWTF      | Default case |
| GTFO           | GTFO        | Wyjście z bloku (break) |
| IM_IN_YR       | IM IN YR    | Początek pętli |
| IM_OUTTA_YR    | IM OUTTA YR | Koniec pętli |
| UPPIN          | UPPIN       | Inkrementacja |
| NERFIN         | NERFIN      | Dekrementacja |
| YR             | YR          | Parametr pętli/funkcji |
| TIL            | TIL         | Warunek UNTIL (dopóki FAŁSZ) |
| WILE           | WILE        | Warunek WHILE (dopóki PRAWDA) |
| HOW_IZ_I       | HOW IZ I    | Definicja funkcji |
| IF_U_SAY_SO    | IF U SAY SO | Koniec funkcji |
| FOUND_YR       | FOUND YR    | Zwrócenie wartości (return) |
| I_IZ           | I IZ        | Wywołanie funkcji |
| BTW            | BTW         | Komentarz jednoliniowy |
| OBTW           | OBTW        | Początek komentarza blokowego |
| TLDR           | TLDR        | Koniec komentarza blokowego |
|WIN|WIN|Wartość logiczna TRUE|
|FAIL|FAIL|Wartość logiczna FALSE|
| IDENTIFIER | [a-zA-Z][a-zA-Z0-9_]* | Nazwa zmiennej |
| STRING | "[^"]*"| Literał tekstowy |
| NUMBER | [0-9]+ | Liczba całkowita |
| WHITESPACE | [ \t]+ | Separatory składni (spacje, tabulatory, nowe linie) |
| NEWLINE | \n | Koniec instrukcji / separator linii |
| EOF | EOF | Oznacza koniec pliku / końca wejścia |


## Gramatyka ANTLR4
```antlr
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
func_decl: HOW_IZ_I ID (AN ID)* body IF_U_SAY_SO;
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
COMMENT: 'BTW' ~[\r\n]* -> skip;
BLOCK_COMMENT: 'OBTW' .*? 'TLDR' -> skip;
NL: '\r'? '\n';
WS: [ \t]+ -> skip;
```