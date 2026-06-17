# LOLCODE version 1.2
import sys
import math
it = None

# To jest zwykły komentarz jednolinijkowy
kod = True
# To jest komentarz blokowy.
# Powinien zachować swoje linie,
# a w Pythonie stać się serią komentarzy ze znakiem #.
it = (1 + 10)
# VISIBLE it
def funkcja(liczba):
    wynik = (liczba + 10)
    return wynik
licznik = -1.0
text = "Testowanie zagniezdzen"
licznik = input()
licznik = int(licznik) if licznik.isnumeric() else licznik
print(text)
if kod:
    print("Pierwszy poziom (If)")
    while (licznik != 3):
        print("Drugi poziom (Petla wewnatrz If):")
        print(licznik)
        it = licznik
        match it:
            case 1:
                print("  Trzeci poziom: Jeden!")
                pass  # GTFO
            case _:
                print("  Trzeci poziom: Cos innego!")
        licznik += 1
else:
    print("Cos nie tak")