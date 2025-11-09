from abc import ABC
from typing import Hashable
import os
from urllib3.filepost import writer

from models import Kontakt
import csv

class file(ABC):
    def __init__(self,file):
        self.file = file


class saveToFile(file):
    def __init__(self):
        super().__init__("KsiazkaTelefoniczna.csv")

    def save(self,list):
        with open(self.file,"w") as file:
            writer = csv.writer(file)
            for i in list:
                writer.writerow([i.name,i.surname,i.phone,i.email])

class loadFromFile(file):
    def __init__(self):
        super().__init__("KsiazkaTelefoniczna.csv")

    def load(self):
        dane = []
        try:
            with open(self.file,"r") as file:
                reader = csv.reader(file)
                for row in reader:
                    name = row[0]
                    surname = row[1]
                    phone = row[2]
                    email = row[3]
                    kontakt = Kontakt(name,surname,phone,email)
                    dane.append(kontakt)
        except FileNotFoundError:
            pass
        return dane
class saveLoginandPasswordToFile(file):
    def __init__(self):
        super().__init__(".LoginData.csv")

    def save(self,login,password):
        with open(self.file, "w") as file:
            writer = csv.writer(file)
            writer.writerow([login,password])
class loadLoginandPasswordFromFile(file):
    def __init__(self):
        super().__init__(".LoginData.csv")

    def load(self):
        try:
            with open(self.file, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    login = row[0]
                    password = row[1]
                    return login,password
        except FileNotFoundError:
            print("Brak Pliku z danymi")
            return None,None

class DestroyData(file):
    def __init__(self):
        super().__init__()

    def delete(self):
        os.remove("KsiazkaTelefoniczna.csv")


