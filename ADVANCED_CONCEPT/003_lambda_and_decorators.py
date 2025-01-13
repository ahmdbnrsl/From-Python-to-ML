kuadrat = lambda angka: angka ** 2

print(kuadrat(4))

# decorator
def logging(func):
    def bungkus():
        print("start executing...")
        func()
        print("end executing...")
    return bungkus
    
@logging
def hallo():
    print("Hello World")
    
hallo()

# decorator with parameter
def log_params(func):
    def wrap(*args, **kwargs):
        print(f"Arguments : {args}, {kwargs}")
        func(*args, **kwargs)
        print(f"Total {len(args) + len(kwargs)} Arguments")
    return wrap
    
@log_params
def tambah(first, second, third):
    print(first + second + third)

tambah(9, 9, third=18)

import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Total Waktu Eksekusi {end - start} detik")
        return result
    return wrapper

@timing
def nested_loop(count):
    for i in range(count):
        for i in range(count):
            for i in range(count):
                pass

nested_loop(30)

# Decorator with lambda
def validate_argument(func):
    return lambda *angka, **kwangka: func(*angka, **kwangka) if angka[0] != 0 else print("Angka tidak boleh 0")
    
@validate_argument
def check_ganjil_genap(angka):
    print("Genap") if angka % 2 == 0 else print("Ganjil")
    
check_ganjil_genap(0)