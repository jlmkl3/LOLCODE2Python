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
| VISIBLE        | VISIBLE     | Wyświetla argument na ekranie (odpowiednik print) |
| GIMMEH         | GIMMEH      | Wczytuje dane od użytkownika |
| I_HAS_A        | I HAS A     | Deklaracja zmiennej |
| ITZ            | ITZ         | Przypisanie wartości przy deklaracji |
| R              | R           | Operator przypisania |
| SUM_OF         | SUM OF      | Operator dodawania |
| DIFF_OF        | DIFF OF     | Operator odejmowania |
| PRODUKT_OF     | PRODUKT OF  | Operator mnożenia |
| QUOSHUNT_OF    | QUOSHUNT OF | Operator dzielenia |
| MOD_OF         | MOD OF      | Operator reszty z dzielenia |
| BIGGR_OF       | BIGGR OF    | Operator maximum|
| SMALLR_OF      | SMALLR OF   | Operator minimum |
| BOTH_OF   | BOTH OF   | AND logiczne (obie wartości muszą być TRUE) |
| EITHER_OF | EITHER OF | OR logiczne (co najmniej jedna wartość TRUE) |
| WON_OF         | WON OF      | Operator XOR |
| NOT            | NOT         | Negacja |
| ALL_OF         | ALL OF      | Operator AND dla wielu argumentów |
| ANY_OF         | ANY OF      | Operator OR dla wielu argumentów |
| BOTH_SAEM | BOTH SAEM | Operator porównania równości (==) |
| DIFFRINT  | DIFFRINT  | Operator nierówności (!=) |
| AN         | AN          | Separator argumentów w wyrażeniach (oddziela kolejne operandy) |
| MKAY       | MKAY        | Zamyka listę argumentów w ALL OF / ANY OF |
| O_RLY?     | O RLY?      | Rozpoczyna instrukcję warunkową (if) |
| YA_RLY     | YA RLY      | Blok wykonywany, gdy warunek jest prawdziwy|
| NO_WAI     | NO WAI      | Blok alternatywny |
| OIC        | OIC         | Kończy instrukcję warunkową |
| WTF?       | WTF?        | Rozpoczyna instrukcję wyboru (switch) |
| OMG        | OMG         | Sekcja case w switch |
| OMGWTF     | OMGWTF      | Domyślny przypadek w switch (default) |
| GTFO       | GTFO        | Przerywa wykonanie bloku (break) |
| IM_IN_YR   | IM IN YR    | Rozpoczyna pętlę |
| IM_OUTTA_YR| IM OUTTA YR | Kończy pętlę |
| UPPIN      | UPPIN       | Zwiększa wartość zmiennej (inkrementacja) |
| NERFIN         | NERFIN      | Dekrementacja |
| YR             | YR          | Argument pętli |
| TIL            | TIL         | Warunek UNTIL |
| WILE           | WILE        | Warunek WHILE |
| HOW_IZ_I       | HOW IZ I    | Definicja funkcji |
| IF_U_SAY_SO    | IF U SAY SO | Koniec funkcji |
| FOUND_YR       | FOUND YR    | Return |
| I_IZ           | I IZ        | Wywołanie funkcji |
| BTW            | BTW         | Komentarz jednoliniowy |
| OBTW           | OBTW        | Początek komentarza blokowego |
| TLDR           | TLDR        | Koniec komentarza blokowego |