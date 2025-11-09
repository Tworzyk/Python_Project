import hashlib
from traceback import print_tb
from xmlrpc.client import Boolean

from File import saveLoginandPasswordToFile, loadLoginandPasswordFromFile, DestroyData


class Logowanie:

    def __init__(self):
        self.zalogowanie = False
        if not self.check_existing_user():
            print("Brak zarejestrowanego użytkownika. Proszę się zarejestrować.")
            self.singup()
        else:
            print("Znaleziono istniejącego użytkownika. Przechodzę do logowania.")
            self.login()

    def check_existing_user(self):
        loader = loadLoginandPasswordFromFile()
        login, password = loader.load()
        return login is not None and password is not None
    def singup(self):

        print("----Rejestracja nowego użytkownika----")
        while True:
            login = input("Podaj login: ")
            password = input("Podaj haslo: ")
            passwordcheck = input("Potwierdz haslo: ")

            if login == "" or password == "" or passwordcheck == "":
                print("Haslo lub login nie moze byc puste")
                continue
            if password != passwordcheck:
                print("Hasla sie nie zgadzaja")
                continue
            enc =  password.encode()
            hash = hashlib.md5(enc).hexdigest()
            zapiszDoPliku = saveLoginandPasswordToFile()
            zapiszDoPliku.save(login,hash)
            break
        self.zalogowanie = True
        print("----Użytkownik zarejestrowany----")


    def login(self):
        odczytajZPLiku = loadLoginandPasswordFromFile()
        loginzpliki, haslozpliku = odczytajZPLiku.load()

        print("----Logowanie----")

        for attempt in range(3):
            login = input("Podaj login: ")
            password = input("Podaj haslo: ")

            enc = password.encode()
            hashpassword = hashlib.md5(enc).hexdigest()
            if login is None or password is None:
                print("Haslo oraz Login nie moga byc psute")
            if login == loginzpliki and haslozpliku == hashpassword:
                print("Zalogowano pomyslnie")
                self.zalogowanie = True
                return True
            else:
                remaining_attempts = 2 - attempt
                if remaining_attempts > 0:
                    print(f"Błędny login lub hasło. Pozostało prób: {remaining_attempts}")

                else:
                    print("Błędny login lub hasło.")
                print("Haslo lub login niepoprawny")

        print("Za duzo prób logowania")
        print("Ponowna rejestracja! - Twoje dane zostana utracone! Przerwij Program aby nie utracic danych")
        self.singup()
        usunieciepliku = DestroyData()
        usunieciepliku.delete()
        return  self.zalogowanie




