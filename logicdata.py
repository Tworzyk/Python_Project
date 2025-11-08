#tutaj dodałbym obsluge danych w lisice
#w klasie logic mamy troche za duzo rzeczy
#trzeba tez odzielic zapis/wczytywanie do innej klasy/klas....

from abc import ABC, abstractmethod
import re


class validator(ABC):
    @abstractmethod
    def checkifisvalid(self,data):
        pass


class emailValidator(validator):
    def __init__(self):
        pass

    def checkifisvalid(self,email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern,email))

class numberValidator(validator):
    def __init__(self):
        pass
    def checkifisvalid(self,phone):

        normalized = re.sub(r'[^\d+]', '', phone)
        pattern = r'^\+?\d{7,15}$'
        return bool(re.match(pattern,normalized))
