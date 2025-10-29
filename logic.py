import csv
import random
from warnings import catch_warnings
from models import Kontakt, Kontakt_id, id_manager

class KsiazkaAdresowa:

    def __init__(self, file="KsiazkaTelefoniczna.csv"):
        self.file = file
        self.dane = []
        self.wczytajZPliku()
#powinno byc git juz
    #trzeba dopisac aby nie potwarzaly sie numery oraz maila, chyba najprosciej  dodatkowa metode ktora  bedzie leciec po liscie i sprawdzac i po sprawie
    def dodajKontakt(self):
        name = input("Podaj imię: ")
        surname = input("Podaj nazwisko: ")
        phone = input("Podaj numer telefonu: ")
        email = input("Podaj adres email: ")

        kontakt = Kontakt(name, surname, phone, email)
        self.dane.append(kontakt)
        self.zapiszDoPliku()
        print("Konktakt dodany poprawnie!")


#nie tykalam sie ale napewno do zmiany przynajmnij z zapisem
    def wyszukajKontakt(self,ciag_znakow_szukanych):
        lista_znalezionych = []
        szukany = str(ciag_znakow_szukanych)
        if szukany is None or szukany == "":
            self.wyswietl()
            return
        for data in self.dane:
            for ciag_znakow in [data.name,data.surname,data.phone,data.email]:
                if ciag_znakow is not None and szukany in str(ciag_znakow):
                    lista_znalezionych.append(data)
        if lista_znalezionych is not None:
            for data in lista_znalezionych:
                print(data)


#chyba ok nie mialam czsu testowac (ale nie wywala)
    def usunKontakt(self):
        self.wyswietl()
        row_to_delete = input("Wpisz id kontaktu do usunięcia: ")

        if row_to_delete.isdigit():
            int_row_to_delete = int(row_to_delete) #samo int(row_to_delete) nie dzialalo, trzeba zapisac do nowej zmiennej
            kontakt = None
            for i in self.dane:
                if i.id == int_row_to_delete:
                    kontakt = i
                    print(kontakt)
                    break

            if kontakt is not None:
                kontakt.delete()
                self.dane.remove(kontakt)
                self.zapiszDoPliku()
                print("Kontakty został usunięty poprawnie!")
            else:
                print("Wybrany kontakt o podanym id nie istnieje!")
        else:
            print("Podaj poprawną wartość w postaci numerycznej!")

#nie skonczylam, chcialam dac edytowanie wybranych czesci np tylko imie itp lub calosci, nie wiem na ile pierdolenia
    #bedziemy myslec na zajeciach, ja bym sprobowal napisac dodadtkowa metode do tego szukac danych ktore chce user zmienic
    def edytujKontakt(self):
        self.wyswietl()

        row_to_edit = input("Podaj id kontaktu który chcesz edytować: ")

        if row_to_edit.isdigit():
            int(row_to_edit)
            kontakt = None
            for i in self.dane:
                if i.id == row_to_edit:
                    kontakt = i
                    break

            if kontakt is not None:
                pass
            else:
                print("Kontakt o podanym id nie istnieje!")
        else:
            print("Podaj poprawną wartość w postaci numerycznej!")

    #nie testowalam czy poprawnie wyswietla jeszcze
    def wyswietl(self):
        if not self.dane:
            print("Brak dostępnych danych")
            return
        for kontakt in self.dane:
            print(kontakt)
# za ulepszenia poza wymagania sa dod punkty....... chce ta pierdole zrobic ze randomowo ci daje kontakt cos jak googlowskie im feeling lucky
    def imFeelingLucky(self):
        size = len(self.dane)
        random_number = random.randrange(1,size)

        for kontakt in self.dane:
            if kontakt.id == random_number:
                print(kontakt)


    def wczytajZPliku(self):
        try:
            with open("KsiazkaTelefoniczna.csv","r") as file:
                reader = csv.reader(file)
                for row in reader:
                    name = row[0]
                    surname = row[1]
                    phone = row[2]
                    email = row[3]
                    kontakt = Kontakt(name,surname,phone,email)
                    self.dane.append(kontakt)
        except FileNotFoundError:
            pass


    def zapiszDoPliku(self):
        with open("KsiazkaTelefoniczna.csv","w") as file:
            writer = csv.writer(file)
            for i in self.dane:
                writer.writerow([i.name,i.surname,i.phone,i.email]) #id czy konieczny tez zapis id?raczej


# test = KsiazkaAdresowa([])

# test.dodajKontakt("kac","asd","asd","asd")
# test.dodajKontakt("test","test","test","tests")
# test.dodajKontakt("tesfsdfsadfasfsdt","tesfasdfsdft","te","testsadfdsa")
# test.dodajKontakt("kacer","tworzydlo","2423432423","skjblad")
# test.dodajKontakt("oliwia","sgfs5rt","43456783214","blad")
# #test.usunKontakt(1)
# #test.usunKontakt(4)
# test.dodajKontakt("kac","asd","asd","asd")
# test.wyszukajKontakt("")
#test.wyswietl()





