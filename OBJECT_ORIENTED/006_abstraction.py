from abc import ABC, abstractmethod

class Hewan(ABC):
    @abstractmethod
    def suara(self):
        pass

class Kucing(Hewan):
    def suara(self):
        return "Meong"

class Anjing(Hewan):
    def suara(self):
        return "Guk Guk"

# Polymorphism dengan abstraksi
def buat_suara(hewan):
    print(hewan.suara())

# Membuat objek
kucing = Kucing()
anjing = Anjing()

buat_suara(kucing)  # Output: Meong
buat_suara(anjing)  # Output: Guk Guk