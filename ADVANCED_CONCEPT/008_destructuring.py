# returning tuple
def angka():
    return 1, 2, 3

satu, dua, tiga = angka()
print(satu, dua, tiga)

# make rest value
satu, *next = angka()
print(satu, next)# """next display as list"""

# returning list
def angka():
    return [1, 2, 3, 4, 5]

satu, *next =angka()
print(satu, next)

# returning dictionary
def persegi(num):
    luas = num ** 2
    volume = num ** 3
    keliling = num * 4
    return {"luas": luas, "vol": volume, "kel":keliling}

def destructure(dct):
    keys = tuple(i for i in dct)
    return (dct[key] for key in keys)

# Contoh penggunaan:
persegi_ = persegi(2)
luas, *_ = destructure(persegi_)
print(luas) 