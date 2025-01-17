# [expression for item in iterable if condition]

#without list comprehension 
angka = []
for i in range(5):
    angka.append(i)
print(angka)  # Output: [0, 1, 2, 3, 4]

# with list comprehension
angka = [i for i in range(5)]
print(angka)  # Output: [0, 1, 2, 3, 4]

# adding condition
# without list comprehension
genap = []
for i in range(10):
    if i % 2 == 0:
        genap.append(i)
print(genap)  # Output: [0, 2, 4, 6, 8]
# with list comprehension
genap = [i for i in range(10) if i % 2 == 0]
print(genap)  # Output: [0, 2, 4, 6, 8]

# with operation
huruf_kapital = [huruf.upper() for huruf in "python"]
print(huruf_kapital)  # Output: ['P', 'Y', 'T', 'H', 'O', 'N']

kuadrat = [x**2 for x in range(5)]
print(kuadrat)  # Output: [0, 1, 4, 9, 16]

# nested list comprehension
matriks = [[j for j in range(3)] for i in range(3)]
print(matriks)
# Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# complex example
vokal = [huruf for huruf in "Python List Comprehension" if huruf.lower() in "aeiou"]
print(vokal)  # Output: ['o', 'i', 'o', 'e', 'e', 'i', 'o']

primes = [x for x in range(2, 50) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
print(primes)  # Output: [2, 3, 5, 7, 11, ..., 47]