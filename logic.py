import csv
import random
from warnings import catch_warnings
from models import Kontakt, Kontakt_id, id_manager
from logicdata import emailValidator, numberValidator, phoneUnique, emailUnique
from File import saveToFile, loadFromFile

class KsiazkaAdresowa:


    def __init__(self):
        wczytaj = loadFromFile()
        self.zapisz = saveToFile()
        self.dane = wczytaj.load()



    def dodajKontakt(self):
        name = input("Podaj imię: ")
        surname = input("Podaj nazwisko: ")
        phone = input("Podaj numer telefonu: ")
        email = input("Podaj adres email: ")
        checkphone = numberValidator()
        checkemail = emailValidator()

        if (checkphone.checkifisvalid(phone) and checkemail.checkifisvalid(email)) is False:
            print("Email lub nr telefonu jest bledny")
            return

        checkphoneunique = phoneUnique(phone,self.dane)
        checkemailunique = emailUnique(email,self.dane)
        if not (checkphoneunique.checkIsUnique() and checkemailunique.checkIsUnique()):
            print("Ten email lub nr telefonu istnieje w bazie")
            return

        kontakt = Kontakt(name, surname, phone, email)
        self.dane.append(kontakt)
        self.zapisz.save(self.dane)
        print("Konktakt dodany poprawnie!")



    def wyszukajKontakt(self):
        ciag_znakow_szukanych = input("Podaj fragment szukanego kontaktu: ")
        szukany = str(ciag_znakow_szukanych)
        if szukany is None or szukany == "":
            self.wyswietl()
            return
        for ciag_znakow in self.dane:
            txt=repr(ciag_znakow).lower()
            if txt is not None and szukany in str(ciag_znakow):
                print(ciag_znakow)




    def usunKontakt(self):
        self.wyswietl()
        row_to_delete = input("Wpisz id kontaktu do usunięcia: ")

        if row_to_delete.isdigit():
            int_row_to_delete = int(row_to_delete)
            kontakt = None
            for i in self.dane:
                if i.id == int_row_to_delete:
                    kontakt = i
                    print(kontakt)
                    break

            if kontakt is not None:
                kontakt.delete()
                self.dane.remove(kontakt)
                self.zapisz.save(self.dane)
                print("Kontakty został usunięty poprawnie!")
            else:
                print("Wybrany kontakt o podanym id nie istnieje!")
        else:
            print("Podaj poprawną wartość w postaci numerycznej!")


    def edytujKontakt(self):
        self.wyswietl()

        row_to_edit = input("Podaj id kontaktu który chcesz edytować: ")

        if row_to_edit.isdigit():
            int_row_to_edit = int(row_to_edit)
            kontakt = None
            for i in self.dane:
                if i.id == int_row_to_edit:
                    kontakt = i
                    print(kontakt)
                    name = input("Podaj imię: ")
                    surname = input("Podaj nazwisko: ")
                    phone = input("Podaj numer telefonu: ")
                    email = input("Podaj adres email: ")

                    if name != "" and name is not None:
                        kontakt.name = name
                    if surname != "" and surname is not None:
                        kontakt.surname = surname
                    if phone != "" and phone is not None:
                        kontakt.phone = phone
                    if email != "" and email is not None:
                        kontakt.email = email
                    self.zapisz.save(self.dane)
                    return

            if kontakt is not None:
                pass
            else:
                print("Kontakt o podanym id nie istnieje!")
        else:
            print("Podaj poprawną wartość w postaci numerycznej!")


    def wyswietl(self):
        if not self.dane:
            print("Brak dostępnych danych")
            return
        for kontakt in self.dane:
            print(kontakt)

    def imFeelingLucky(self):
        ListofFreeIds = id_manager.freeid ## ta funkcje trzeba jakos naprawić
        print(ListofFreeIds)
        size = len(self.dane) + len(ListofFreeIds)
        random_number = random.randrange(1,size+1)
        while random_number in ListofFreeIds:
            random_number = random.randrange(1, size + 1)
            if random_number not in ListofFreeIds:
                break
        for kontakt in self.dane:
            if kontakt.id == random_number:
                print(size)
                print(ListofFreeIds)
                print(random_number)
                print(kontakt)

    def saveToFile(self):
        self.zapisz.save(self.dane)






