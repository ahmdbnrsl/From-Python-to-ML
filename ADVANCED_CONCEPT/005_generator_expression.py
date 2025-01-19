# Generator Expression
gen = (x**2 for x in range(5))
print(gen)  # Output: <generator object ...>

# Mengakses elemen generator
for val in gen:
    print(val)  # Output: 0, 1, 4, 9, 16
    
gen = (x**2 for x in range(5))

print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 4

gen = (x for x in range(10) if x % 2 == 0)
print(list(gen))  # Output: [0, 2, 4, 6, 8]

gen = (x for x in range(10))
print(sum(gen))  # Output: 45

gen = (str(x) for x in range(5))
print(", ".join(gen))  # Output: "0, 1, 2, 3, 4"

# Membaca file baris demi baris (misal "data.txt")
with open("data.txt", "r") as file:
    gen = (line.strip() for line in file if line.strip())
    for line in gen:
        print(line)
        
        
# Angka genap terbesar di range 1-100
gen = (x for x in range(1, 101) if x % 2 == 0)
print(max(gen))  # Output: 100
