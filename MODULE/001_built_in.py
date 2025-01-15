import math

print(math.sqrt(16))  # Output: 4.0
print(math.pi)        # Output: 3.141592653589793

import random

print(random.randint(1, 10))  # Output: Angka acak antara 1 dan 10
print(random.choice(["apel", "mangga", "pisang"]))  # Output: Item acak dari list

import os

print(os.name)              # Output: 'posix' (Linux/Mac) atau 'nt' (Windows)
print(os.getcwd())          # Output: Direktori kerja saat ini

from datetime import datetime

now = datetime.now()
print(now)  # Output: Tanggal dan waktu saat ini