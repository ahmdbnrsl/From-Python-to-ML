with open('./file/data.txt', 'w') as file:
    file.write("Python itu mudah.\nBelajar Python itu asik.")
    
with open('./file/data.txt', 'r') as file:
    print(file.read())
    
with open('./file/data.txt', 'a') as file:
    file.write("\nAku sedang belajar file handling.")