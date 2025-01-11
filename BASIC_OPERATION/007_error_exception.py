try:
    hasil = 10 / 0  # Ini akan memunculkan error
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")
finally:
    print("Blok finally selalu dijalankan.")