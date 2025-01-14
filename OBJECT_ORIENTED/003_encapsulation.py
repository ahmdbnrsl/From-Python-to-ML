class Mahasiswa:
    def __init__(self, nama):
        self.__nama = nama  # Atribut privat

    def get_nama(self):
        return self.__nama  # Mengakses atribut privat

# Membuat objek
ahmad = Mahasiswa("Ahmad")
print(ahmad.get_nama())  # Output: Ahmad

class Kendaraan:
    def __init__(self, nama, kecepatan):
        self.nama = nama          # Public
        self._jenis = "Transport" # Protected
        self.__kecepatan = kecepatan  # Private

    def get_kecepatan(self):  # Getter
        return self.__kecepatan

    def set_kecepatan(self, kecepatan):  # Setter
        if kecepatan > 0:
            self.__kecepatan = kecepatan
        else:
            print("Kecepatan harus lebih dari 0!")

mobil = Kendaraan("Mobil", 120)
print(mobil.nama)         # Output: Mobil (public)
print(mobil._jenis)       # Output: Transport (protected, masih bisa diakses tapi tidak disarankan)
print(mobil.get_kecepatan())  # Output: 120 (private melalui getter)

mobil.set_kecepatan(150)  # Mengubah kecepatan melalui setter
print(mobil.get_kecepatan())  # Output: 150