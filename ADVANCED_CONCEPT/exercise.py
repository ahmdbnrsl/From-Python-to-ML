import math

# Faktorial dari 1 hingga 5
factorial = [math.factorial(x) for x in range(1, 6)]
print(f"Faktorial dari 1 hingga 5: {factorial}")

# Angka ganjil dari 1 hingga 20
odd = [i for i in range(1, 21) if i % 2 != 0]
print(f"Angka ganjil dari 1 hingga 20: {odd}")

# Matriks 3 × 3
matriks = [[j for j in range(1, 4)] for _ in range(3)]
print("Matriks 3 × 3:")
for row in matriks:
    print(row)

# Cara 1: Menggunakan range langsung
matriks1 = [[j for j in range(i, i + 3)] for i in range(1, 10, 3)]
print(f"Matriks Cara 1: {matriks1}")

# Cara 2: Menggunakan slicing
angka = list(range(1, 10))
print(angka)
print(angka[3:])
matriks2 = [angka[i:i + 3] for i in range(0, len(angka), 3)]
print(f"Matriks Cara 2: {matriks2}")

# Generator Expression 
# membuat factorial 1 - 5
factorial = (math.factorial(i) for i in range(1, 6))
print(list(factorial))

# angka ganjil dari 1 - 20
odd = (i for i in range(1, 20) if i % 2 != 0)
print(list(odd))

# berapa banyak angka genap dari 1 - 1000
even = (i for i in range(1, 1001) if i % 2 == 0)
print(len(list(even)))

# Faktorial dari 1 hingga 5
factorial = (math.factorial(i) for i in range(1, 6))
print("Faktorial:", list(factorial))  # Output: [1, 2, 6, 24, 120]

# Angka ganjil dari 1 hingga 20
odd = (i for i in range(1, 20, 2))
print("Angka ganjil:", list(odd))  # Output: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Jumlah angka genap dari 1 hingga 1000
even_count = sum(1 for i in range(1, 1001) if i % 2 == 0)
print("Jumlah angka genap:", even_count)  # Output: 500

# Procedural paradigm untuk mencetak factorial dari 1 - 5
import math

def factorial(start, end):
    if start >= end:
        raise ValueError("Masukan dari angka terkecil ke terbesar")
    else:
        result = [math.factorial(i) for i in range(start, end+1)]
        print(result)

factorial(1, 5)

#OOP paradigms untuk mencetak angka genap
class Angka:
    def __init__(self, angka):
        if angka <= 0:
            raise ValueError("Masukan hanya bilangan bulat positif")
        else:
            self.angka = angka
    def is_genap(self):
        print(self.angka % 2 == 0)

angka = Angka(6)
angka.is_genap()

# functional paradigm untuk menjumlahkan semua angka genap dari 1 - 20
angka_genap = sum((i for i in range(1, 21) if i % 2 == 0))
print(angka_genap)

import math

# Procedural Paradigm
def factorial(start=1, end=5):
    if start >= end:
        raise ValueError("Masukan dari angka terkecil ke terbesar")
    result = [math.factorial(i) for i in range(start, end + 1)]
    return result

print("Faktorial:", factorial())  # Output: [1, 2, 6, 24, 120]

# OOP Paradigm
class Angka:
    def __init__(self, angka):
        if angka <= 0:
            raise ValueError("Masukan hanya bilangan bulat positif")
        self.angka = angka

    def is_genap(self):
        return self.angka % 2 == 0

angka = Angka(6)
print("Apakah genap:", angka.is_genap())  # Output: True

# Functional Paradigm
angka_genap = sum(i for i in range(1, 21) if i % 2 == 0)
print("Jumlah angka genap:", angka_genap)  # Output: 110

# Asynchronous task
import asyncio as asc
import requests
import json

async def make_request(url):
    await asc.sleep(2)
    return requests.get(url)

async def fetch_data():
    url = "https://api.github.com/users/ahmdbnrsl"
    print(f"Start fetching data to {url}...")
    response = await make_request(url)
    print(f"Data successfully taked with response : \n{json.dumps(response.json(), indent=2)}\n\n")

async def process_data():
    print("Start processing...")
    await asc.sleep(3)
    print("Processing finish")

async def main():
    await asc.gather(
        fetch_data(),
        process_data()
    )

asc.run(main())


import httpx

# Fungsi untuk membuat request HTTP secara asynchronous
async def make_request(url):
    async with httpx.AsyncClient() as client:
        return await client.get(url)

# Fungsi untuk mengambil data dari API
async def fetch_data():
    url = "https://api.github.com/users/ahmdbnrsl"
    print(f"Start fetching data from {url}...")
    try:
        response = await make_request(url)
        if response.status_code == 200:
            print(f"Data successfully fetched:\n{json.dumps(response.json(), indent=2)}\n\n")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while fetching data: {e}")

# Fungsi untuk memproses data
async def process_data():
    print("Start processing...")
    await asc.sleep(3)
    print("Processing finished\n")

# Fungsi utama untuk menjalankan kedua tugas secara bersamaan
async def main():
    await asc.gather(
        fetch_data(),
        process_data()
    )

asc.run(main())