class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def perkenalkan(self):
        print(f"Halo, nama saya {self.nama}, NIM saya {self.nim}, jurusan {self.jurusan}.")

    def hitung_semester(self, tahun_masuk):
        tahun_sekarang = 2025
        semester = (tahun_sekarang - tahun_masuk) * 2
        return semester

# Membuat objek
ahmad = Mahasiswa("Ahmad Beni Rusli", "245720003", "Sistem Informasi")
ahmad.perkenalkan()
semester = ahmad.hitung_semester(2021)
print(f"Saya sekarang di semester {semester}.")