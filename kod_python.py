it = None
def funkcja(liczba):
    wynik = (liczba + 10)
    return wynik
kod = True
licznik = 0
text = "Testowanie"
licznik = input(); licznik = int(licznik) if licznik.isnumeric() else licznik
print(text)
print((5 + (4 * 3)))
if True:
    print("Warunek spelniony")
else:
    print("Cos nie tak")
it = licznik
match it:
    case 1:
        print("Jedynka")
        pass  # GTFO
    case 2:
        print("Dwojka")
        pass  # GTFO
    case _:
        print("Cos innego")
while (licznik != 5):
    print(licznik)
    test_funkcji = funkcja(licznik)
    print(test_funkcji)
licznik += 1
print(all([(licznik == 5), True, (not False)]))