import csv

from logic import KsiazkaAdresowa

name = input("Cześć jak się nazywasz?")
again = True

while again:

    print(f"--- Kontakty ---\nWitaj {name} w programie zarządzania kontaktami, wybierz zadanie do wykonania:")
    print("1) Dodaj nowy kontakt\n2) Usuń kontakt\n3) Wyszukaj kontakt\n4) Edytuj kontakt\n5) Wyświetl pełną listę kontaktów\n"
          "6) Nie wiesz do jakiego znajomego zadzwonić? Wybierz mnie\n7) Zakończ program")

    user = int(input("Podaj numer: "))

    if user == 1:
        dodajKontakt()
    elif user == 2:
        usunKontakt()
    elif user == 3:
        wyszukajKontakt()
    elif user == 4:
        edytujKontakt()
    elif user == 5:
        wyswietlKontakt()
    elif user == 6:
        imFeelingLucky()
    elif user == 7:
        print(f"Dziękujemy za skorzystanie z naszego programu! Do zobaczenia {name}!")
        again = False
    else:
        print("Prosze podać poprawną wartość! ")

