class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

class MahasiswaBaru(Mahasiswa):  # Pewarisan
    def __init__(self, nama, nim, asal_sekolah):
        super().__init__(nama, nim)  # Memanggil konstruktor parent
        self.asal_sekolah = asal_sekolah

    def info(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}, Asal Sekolah: {self.asal_sekolah}")

# Membuat objek
ahmad = MahasiswaBaru("Ahmad", "245720003", "SMA Negeri 1 Cilacap")
ahmad.info()