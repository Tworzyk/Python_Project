class Kontakt_id:
    def __init__(self):
        self._next_id=1
        self._free_ids=[]

    def get_next_id(self):
        if self._free_ids:
            return self._free_ids.pop(0)
        id = self._next_id
        self._next_id += 1
        return id

    def release_id(self,id):
        self._free_ids.append(id)

    def __str__(self):
        return f"Next ID: {self._next_id}, Free ID's: {self._free_ids}"


id_manager = Kontakt_id()
class Kontakt:
    def __init__(self,name,surname,phone,email):
        self.id = id_manager.get_next_id()
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def delete(self):
        id_manager.release_id(self.id)
        print(f"ID to : {self.id}")

    def __str__(self):
        return f" ID:{self.id} Imie: {self.name}, nazwisko: {self.surname}, phone: {self.phone}, email:{self.phone}"


