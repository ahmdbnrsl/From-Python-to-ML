with open("./file/example.txt", "w") as file:  # Mode 'w' untuk menulis
    file.write("Halo Dunia!\n")
    file.write("Ini baris kedua.")
    
with open("./file/example.txt", "a") as file:  # Mode 'a' untuk menambah
    file.write("\nBaris tambahan.")