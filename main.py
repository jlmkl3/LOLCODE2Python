from antlr4 import *
from generated.LolcodeLexer import LolcodeLexer
from generated.LolcodeParser import LolcodeParser
from transpiler import Lolcode2Python
import sys

def main():
    if len(sys.argv)<2:
        print("Przy wywoływaniu programu dodaj nazwę pliku wejściowego!")
        sys.exit()

    file_path=sys.argv[1]

    strumien=FileStream(file_path,encoding='utf-8')

    lekser=LolcodeLexer(strumien)
    tokeny=CommonTokenStream(lekser)
    parser=LolcodeParser(tokeny)

    tree=parser.program()

    kod_python=Lolcode2Python().visit(tree)

    with open("kod_python.py","w", encoding="utf-8") as f:
        f.write(kod_python)

if __name__=='__main__':
    main()