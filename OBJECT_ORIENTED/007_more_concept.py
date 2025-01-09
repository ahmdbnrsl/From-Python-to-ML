# Singleton
class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        
        return cls._instance
    def __init__(self, nama):
        self.nama = nama
        
Nama = Singleton("Ahmad")
print(Nama.nama)
print(vars(Nama))

class Singleton2:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print("Membuat instance baru.")
            cls._instance = super().__new__(cls)
        else:
            print("Menggunakan instance yang sudah ada.")
        return cls._instance

obj1 = Singleton2()
obj2 = Singleton2()
print(obj1 is obj2)  # Output: True
