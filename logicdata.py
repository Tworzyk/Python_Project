
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
        if email == "":
            return True
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        return bool(re.match(pattern,email))

class numberValidator(validator):
    def __init__(self):
        pass
    def checkifisvalid(self,phone):

        normalized = re.sub(r'[^\d+]', '', phone)
        pattern = r'^\+?\d{7,15}$'
        return bool(re.match(pattern,normalized))


class unique(ABC):
    def __init__(self, value, data):
        self.value = value
        self.data = data
    @abstractmethod
    def checkIsUnique(self):
        pass

class phoneUnique(unique):

    def checkIsUnique(self):
        for kontakt in self.data:
            if kontakt.phone == self.value:
                return False
        return True

class emailUnique(unique):

        def checkIsUnique(self):
            for kontakt in self.data:
                if kontakt.email == self.value and kontakt.email != "":
                    return False
            return True

