with open("./file/example.txt", "r") as file:  # Mode 'r' untuk membaca
    isi = file.read()
    print(isi)
    
# Read line by line
with open("./file/example.txt", "r") as file:
    for baris in file:
        print(baris.strip())  # Menghapus karakter '\n' di akhir baris