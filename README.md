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