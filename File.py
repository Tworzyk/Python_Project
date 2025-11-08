from abc import ABC
from models import Kontakt
import csv
class file(ABC):
    def __init__(self,file = "KsiazkaTelefonicz.csv"):
        self.file = file


class saveToFile(file):
    def __init__(self):
        super().__init__()

    def save(self,list):
        with open("KsiazkaTelefoniczna.csv","w") as file:
            writer = csv.writer(file)
            for i in list:
                writer.writerow([i.name,i.surname,i.phone,i.email])

class loadFromFile(file):
    def __init__(self):
        super().__init__()

    def load(self):
        dane = []
        try:
            with open("KsiazkaTelefoniczna.csv","r") as file:
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
