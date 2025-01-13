from abc import ABC, abstractmethod

class Hewan:
    def suara(self):
        print("Hewan Bersuara")
        
class Kambing(Hewan):
    def suara(self):
        print("Mbeeekk Mbeekk")
        
class Anjing(Hewan):
    def suara(self):
        print("Guk Guk Guk")
        
def buat_suara(hewan):
    hewan.suara()
    
kambing = Kambing()
anjing = Anjing()

buat_suara(kambing)
buat_suara(anjing)
# ABSTRACT CLASS

# class Kendaraan(ABC):
#     @abstractmethod
#     def bergerak(self):
#         pass
#     
# class Mobil(Kendaraan):
#     def bergerak(self):
#         return "Bergerak dijalan"
#         
# class Pesawat(Kendaraan):
#     def bergerak(self):
#         return "Terbang di udara"
        
# def kendaraan_bergerak(kendaraan):
#     print(kendaraan.bergerak())
#     
# mobil = Mobil()
# pesawat = Pesawat()
# 
# kendaraan_bergerak(mobil)
# kendaraan_bergerak(pesawat)


class Kendaraan:
    def __init__(self, nama, kecepatan):
        self.nama = nama
        self.kecepatan = kecepatan

    def __str__(self):
        return f"Ini adalah {self.nama} dengan kecepatan {self.kecepatan} km/jam"

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.kecepatan * other
        raise ValueError("Nilai untuk perkalian harus berupa angka (int/float).")

    def __eq__(self, other):
        if not isinstance(other, Kendaraan):
            return False
        return self.kecepatan == other.kecepatan

class Mobil(Kendaraan):
    pass

class Motor(Kendaraan):
    pass

# Membuat objek
mobil = Mobil("Mobil", 300)
motor = Motor("Motor", 200)

print(f'''
Method __str__ :
1. {mobil}
2. {motor}
Method __mul__ :
1. Jarak tempuh mobil : {mobil * 2}KM
2. Jarak tempuh motor : {motor * 2}KM
Method __eq__ :
Perbandingan Kecepatan Motor dan Mobil : {"Mobil memiliki kecepatan yang sama dengan Motor" if mobil == motor else "Mobil memiliki kecepatan yang tak sama dengan Motor"}
''')