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