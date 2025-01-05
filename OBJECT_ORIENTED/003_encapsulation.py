class Mahasiswa:
    def __init__(self, nama):
        self.__nama = nama  # Atribut privat

    def get_nama(self):
        return self.__nama  # Mengakses atribut privat

# Membuat objek
ahmad = Mahasiswa("Ahmad")
print(ahmad.get_nama())  # Output: Ahmad