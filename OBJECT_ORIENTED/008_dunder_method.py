# dunder method diapit menggunakan double underscore 

class Kendaraan:
    def __init__(self, nama, kecepatan): # this is dunder method
        self.nama = nama
        self.kecepatan = kecepatan
        
    def __str__(self):
        return f"{self.nama} dengan kecepatan {self.kecepatan} km/jam"
        
    def __repr__(self):
        return f"Kendaraan('{self.nama}', {self.kecepatan})"

    def __add__(self, other):
        return self.kecepatan + other.kecepatan
        
class Garasi:
    def __init__(self, kendaraan):
        self.kendaraan = kendaraan

    def __len__(self):
        return len(self.kendaraan)

motor = Kendaraan("Motor", 80)
mobil = Kendaraan("Mobil", 120)

print(mobil)  # Output: Mobil dengan kecepatan 120 km/jam
print(repr(mobil))  # Output: Kendaraan('Mobil', 120)
print(mobil + motor)  # Output: 200

garasi = Garasi(["Mobil", "Motor", "Sepeda"])
print(len(garasi))  # Output: 3