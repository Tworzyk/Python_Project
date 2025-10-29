from os.path import defpath


class Kontakt_id:
    def __init__(self):
        self._next_id=1
        self._free_ids=[]

    def get_next_id(self):
        if self._free_ids:
            return self._free_ids.pop(0)
        id_manager = self._next_id
        self._next_id += 1
        return id_manager

    def release_id(self,id):
        self._free_ids.append(id)

    def __str__(self):
        return f"Next ID: {self._next_id}, Free ID's: {self._free_ids}"


id_manager = Kontakt_id()
class Kontakt:
    def __init__(self,name,surname,phone,email):
        self._id = id_manager.get_next_id()
        self._name = name
        self._surname = surname
        self._phone = phone
        self._email = email

    def delete(self):
        id_manager.release_id(self._id)
        print(f"ID to : {self._id}")

    def __str__(self):
        return f" ID:{self._id} Imie: {self._name}, nazwisko: {self._surname}, phone: {self._phone}, email:{self._email}"

    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    @property
    def surname(self):
        return self._surname
    @property
    def phone(self):
        return self._phone
    @property
    def email(self):
        return self._email


