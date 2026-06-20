from antlr4.error.ErrorListener import ErrorListener

class LolcodeErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if offendingSymbol and offendingSymbol.text and offendingSymbol.text.strip():
            token = offendingSymbol.text
        else:
            token = "koniec"

        previous_token = ""
        try:
            if recognizer and hasattr(recognizer, "getInputStream"):
                tokens = recognizer.getInputStream()
                if hasattr(offendingSymbol, "tokenIndex") and offendingSymbol.tokenIndex > 0:
                    prev_symbol = tokens.get(offendingSymbol.tokenIndex - 1)
                    if prev_symbol and prev_symbol.text:
                        previous_token = prev_symbol.text.strip().upper()
        except Exception:
            previous_token = ""

        expected_set = None
        if e is not None:
            expected_set = e.getExpectedTokens()
        elif recognizer is not None:
            expected_set = recognizer.getExpectedTokens()

        expected_str = ""
        if expected_set and recognizer:
            try:
                token_ids = list(expected_set)
            except Exception:
                token_ids = []

            if token_ids:
                if hasattr(recognizer, "getVocabulary"):
                    vocab = recognizer.getVocabulary()
                    expected_str = ", ".join([vocab.getDisplayName(t) for t in token_ids])
                elif hasattr(recognizer, "symbolicNames"):
                    names = recognizer.symbolicNames
                    expected_str = ", ".join([names[t] for t in token_ids if t < len(names)])

        message = self.build_message(token, line, column, msg, expected_str, previous_token)
        raise SyntaxError(message)

    def build_message(self, token, line, column, msg, expected="", previous_token=""):
        base = (
            f"\n[BŁĄD SKŁADNIOWY]\n"
            f"Linia: {line}, Kolumna: {column}\n"
        )
        
        exp = expected.upper() or ""
        msg_lower = msg.lower()

        if "VISIBLE" in exp or "visible" in msg_lower or previous_token == "VISIBLE":
            return base + "Błąd: Brak argumentu dla instrukcji wypisywania 'VISIBLE'."

        if "ITZ" in exp or ("missing" in msg_lower and "itz" in msg_lower) or previous_token == "ITZ":
            return base + "Błąd: Brak wartości inicjalizującej po słowie kluczowym 'ITZ'."

        if "YR" in exp or previous_token == "YR":
            return base + "Błąd: Oczekiwano słowa kluczowego 'YR' przed nazwą zmiennej lub wyrażeniem."

        if "YA RLY" in exp:
            return base + "Błąd: Brak bloku 'YA RLY' po instrukcji warunkowej 'O RLY?'."

        if any(x in exp for x in ["NUMBER", "ID", "STRING", "YARN", "NUMBR", "NUMBAR"]):
            return (base + f"Błąd: Oczekiwano wartości, zmiennej lub wyrażenia, a napotkano '{token}'.\n"
            f"Szczegóły techniczne ANTLR: {msg}")

        if "missing" in msg_lower:
            missing_token = msg.split()[-1] if msg.split() else ""
            return base + f"Błąd: Brakuje elementu {missing_token} w tym miejscu."

        return (
            base +
            f"Napotkano niepoprawny token: '{token}'\n"
            f"Co powinno tu być: {expected if expected else 'Nieokreślone'}\n"
            f"Szczegóły techniczne ANTLR: {msg}"
        )