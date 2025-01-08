with open('./file/img.jpg', 'rb') as file:
    data = file.read()
    print(f"Ukuran file: {len(data) / 1024} bytes")
    
with open('./file/copy_img.jpg', 'wb') as file:
    file.write(data)