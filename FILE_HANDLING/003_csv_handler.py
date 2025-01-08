import csv

with open('./file/data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Setiap baris berupa list



with open('./file/data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nama', 'Usia', 'Kota'])  # Header
    writer.writerow(['Ahmad', 25, 'Cilacap'])
    writer.writerow(['Budi', 30, 'Jakarta'])

with open('./file/data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Nama'], row['Usia'], row['Kota'])
        
