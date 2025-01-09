# basic syntax

def nama_fungsi(parameter):
    # Kode di dalam fungsi
    return hasil

# without parameter

def sapa():
    print("Halo, Ahmad!")

sapa()  # Memanggil fungsi

# with parameter

def sapa_2(nama):
    print(f"Halo, {nama}!")

sapa_2("Ahmad")  # Output: Halo, Ahmad!
sapa_2("Beni")   # Output: Halo, Beni!

# function with return value

def jumlahkan(a, b):
    return a + b

hasil = jumlahkan(5, 10)
print(hasil)  # Output: 15

# default parameter

def sapa_3(nama="Ahmad"):
    print(f"Halo, {nama}!")

sapa_3()           # Output: Halo, Ahmad!
sapa_3("Beni")     # Output: Halo, Beni!

# advanced example

def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

def cetak_luas(panjang, lebar):
    luas = hitung_luas_persegi_panjang(panjang, lebar)
    print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")

# Panggil fungsi
cetak_luas(10, 5)

# LAMBDA FUNCTION OR ANONYMOUS FUNCTION

# example one to make simple fuction with only one line

tambah = lambda a, b: a + b
print(tambah(5, 10))  # Output: 15

# example lambda function with parameter
halo = lambda: "Halo, Dunia!"
print(halo())  # Output: Halo, Dunia!

# lambda function with logic operator

genap = lambda x: x % 2 == 0
print(genap(4))  # Output: True
print(genap(5))  # Output: False

# lambda as argument of higher order function

# map
angka = [1, 2, 3, 4]
hasil = list(map(lambda x: x * 2, angka))
print(hasil)  # Output: [2, 4, 6, 8]

# filter

angka_2 = [1, 2, 3, 4, 5]
hasil_2 = list(filter(lambda x: x % 2 == 0, angka_2))
print(hasil_2)  # Output: [2, 4]

# sorted
data = [("Ahmad", 25), ("Beni", 22), ("Citra", 23)]
hasil_3 = sorted(data, key=lambda x: x[1])  # Urutkan berdasarkan umur
print(hasil_3)  # Output: [('Beni', 22), ('Citra', 23), ('Ahmad', 25)]

# training

# kuadrat

kuadrat = lambda number: number ** 2
print(kuadrat(5))

# filtered negative number

list_of_number = [1, -2, 3, 4, 5, -7]
filtered_negative_number = list(filter(lambda x: x < 0, list_of_number))
print(filtered_negative_number)

# rest parameter
# ARGS
def data_siswa(*nama_siswa):
    print(nama_siswa)

data_siswa("Beni", "Ahmad", "Rusli")

# KEYWORD ARGS
def data_mahasiswa(**nama_mahasiswa):
    print(nama_mahasiswa)

data_mahasiswa(nama="Ahmad", umur=19)

# MIX
def data_penduduk(*penduduk, **kwpenduduk):
    print(penduduk)
    print(kwpenduduk)
    
data_penduduk("Cikarag", nama="Ahmad Beni Rusli")