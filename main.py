import csv

from logic import KsiazkaAdresowa

name = input("Cześć jak się nazywasz? ")
again = True

ksiazkaAdresowa = KsiazkaAdresowa()
while again:

    print(f"--- Kontakty ---\nWitaj {name} w programie zarządzania kontaktami, wybierz zadanie do wykonania:")
    print("1) Dodaj nowy kontakt\n2) Usuń kontakt\n3) Wyszukaj kontakt\n4) Edytuj kontakt\n5) Wyświetl pełną listę kontaktów\n"
          "6) Nie wiesz do jakiego znajomego zadzwonić? Wybierz mnie\n7) Zakończ program")

    user = int(input("Podaj numer: "))

    if user == 1:
      ksiazkaAdresowa.dodajKontakt()
    elif user == 2:
        ksiazkaAdresowa.usunKontakt()
    elif user == 3:
        ##ksiazkaAdresowa.wyszukajKontakt()
        pass
    elif user == 4:
        pass
    elif user == 5:
        ksiazkaAdresowa.wyswietl()
    elif user == 6:
        ksiazkaAdresowa.imFeelingLucky()
    elif user == 7:
        print(f"Dziękujemy za skorzystanie z naszego programu! Do zobaczenia {name}!")
        ksiazkaAdresowa.zapiszDoPliku()
        again = False
    else:
        print("Prosze podać poprawną wartość! ")

