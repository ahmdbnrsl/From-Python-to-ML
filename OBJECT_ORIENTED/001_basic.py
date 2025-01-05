class Mahasiswa:
    def __init__(self, nama, nim):  # Konstruktor
        self.nama = nama  # Atribut
        self.nim = nim

    def perkenalkan(self):  # Metode
        print(f"Halo, nama saya {self.nama}, NIM saya {self.nim}.")

# Membuat objek
ahmad = Mahasiswa("Ahmad Beni Rusli", "245720003")
ahmad.perkenalkan()