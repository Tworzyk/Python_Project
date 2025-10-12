from warnings import catch_warnings

from models import Kontakt, Kontakt_id, id_manager

class KsiazkaAdresowa:

    def __init__(self,dane):
        self.dane = dane

    def dodajKontakt(self, name, surname, phone, email):
        uzytkownik = Kontakt(name, surname, phone, email)
        self.dane.append(uzytkownik)

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



    def usunKontakt(self, id):
        for data in self.dane:
            if data.id == id:
                print(data)
                data.delete()


    def wyswietl(self):
        for data in self.dane:
            print(data)
            #print(id_manager)


test = KsiazkaAdresowa([])

test.dodajKontakt("kac","asd","asd","asd")
test.dodajKontakt("test","test","test","tests")
test.dodajKontakt("tesfsdfsadfasfsdt","tesfasdfsdft","te","testsadfdsa")
test.dodajKontakt("kacer","tworzydlo","2423432423","skjblad")
test.dodajKontakt("oliwia","sgfs5rt","43456783214","blad")
#test.usunKontakt(1)
#test.usunKontakt(4)
test.dodajKontakt("kac","asd","asd","asd")
test.wyszukajKontakt("")
#test.wyswietl()





