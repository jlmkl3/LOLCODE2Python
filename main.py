from antlr4 import *
from LolcodeErrorListener import LolcodeErrorListener
from generated.LolcodeLexer import LolcodeLexer
from generated.LolcodeParser import LolcodeParser
from transpiler import Lolcode2Python
import sys
import os

def main():
    if len(sys.argv)<2:
        print("Przy wywoływaniu programu dodaj nazwę pliku wejściowego!")
        sys.exit()

    file_path=sys.argv[1]

    strumien=FileStream(file_path,encoding='utf-8')

    lekser=LolcodeLexer(strumien)
    tokeny=CommonTokenStream(lekser)
    parser=LolcodeParser(tokeny)
    parser.removeErrorListeners()
    parser.addErrorListener(LolcodeErrorListener())

    tree=parser.program()

    transpiler = Lolcode2Python()
    kod_python = transpiler.visit(tree)

    sciezka_bez_rozszerzenia, _ = os.path.splitext(file_path)
    wyjsciowy_plik = sciezka_bez_rozszerzenia + ".py"


    if transpiler.errors:
        for error in transpiler.errors:
            print(error)
        with open(wyjsciowy_plik, "w", encoding="utf-8") as f:
            f.write("")
        print(f"Wygenerowano pusty plik: '{wyjsciowy_plik}'")
    else:
        with open(wyjsciowy_plik, "w", encoding="utf-8") as f:
            f.write(kod_python)
        print("Zapisano plik test.py")

if __name__=='__main__':
    main()