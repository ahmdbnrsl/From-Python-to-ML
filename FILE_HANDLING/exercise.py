import csv

# with open('./file/data.txt', 'w') as file:
#     file.write("Python itu mudah.\nBelajar Python itu asik.")
#     
# with open('./file/data.txt', 'r') as file:
#     print(file.read())
#     
# with open('./file/data.txt', 'a') as file:
#     file.write("\nAku sedang belajar file handling.")
    
with open('./file/mahasiswa.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["NIM", "Nama", "Jurusan"])
    writer.writerow(["245720003", "Ahmad", "Sistem Informasi"])
    writer.writerow(["245720004", "Budi", "Informatika"])
    
with open("./file/mahasiswa.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["NIM"], row["Nama"], row["Jurusan"])
        
with open('./file/mahasiswa.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["245720003", "Putri", "Biologi"])