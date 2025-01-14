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

# polymorphism

class BangunDatar:
    def __init__(self, nama):
        self.nama = nama
    def luas(self, **ukuran):
        raise NotImplementedError("Metode luas harus diimplementasikan di kelas turunan.")

class Persegi(BangunDatar):
    def luas(self, **ukuran):
        if isinstance(ukuran["sisi"], (int, float)):
            return ukuran["sisi"] * ukuran["sisi"]
        raise ValueError("Nilai harus berupa angka (int/float).")

class Segitiga(BangunDatar):
    def luas(self, **ukuran):
        if isinstance(ukuran["alas"], (int, float)) and isinstance(ukuran["tinggi"], (int, float)):
            return 1/2 * ukuran["alas"] * ukuran["tinggi"]
        raise ValueError("Nilai harus berupa angka (int/float).")

def cetak_luas(bangun, **ukuran):
    print(f"Luas dari {bangun.nama} adalah {bangun.luas(**ukuran)}")

# Penggunaan
cetak_luas(Persegi("Persegi"), sisi=20)       # Output: Luas dari Persegi adalah 400
cetak_luas(Segitiga("Segitiga"), alas=10, tinggi=15)  # Output: Luas dari Segitiga adalah 75.0