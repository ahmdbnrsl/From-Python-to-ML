class Burung:
    def bersuara(self):
        print("Burung berbunyi: cuit cuit")

class Kucing:
    def bersuara(self):
        print("Kucing berbunyi: meong meong")

# Polymorphism dengan memanggil metode 'bersuara'
def buat_bersuara(hewan):
    hewan.bersuara()

burung = Burung()
kucing = Kucing()

buat_bersuara(burung)  # Output: Burung berbunyi: cuit cuit
buat_bersuara(kucing)  # Output: Kucing berbunyi: meong meong

# POLYMORPHISM WITH INHERITANCE 

class Kendaraan:
    def bergerak(self):
        print("Kendaraan bergerak")

class Mobil(Kendaraan):
    def bergerak(self):
        print("Mobil melaju di jalan")

class Kapal(Kendaraan):
    def bergerak(self):
        print("Kapal berlayar di laut")

# Polymorphism dalam aksi
def jalan_kendaraan(kendaraan):
    kendaraan.bergerak()

mobil = Mobil()
kapal = Kapal()

jalan_kendaraan(mobil)  # Output: Mobil melaju di jalan
jalan_kendaraan(kapal)  # Output: Kapal berlayar di laut

# POLYMORPHISM WITH INHERENT FUNCTION

print(len("Ahmad"))        # Output: 5 (jumlah huruf di string)
print(len([1, 2, 3, 4]))   # Output: 4 (jumlah elemen di list)