import re

# Mencocokkan pola di awal string
result = re.match(r'Python', 'Python is fun')
print(result.group())  # Output: Python

text = "Belajar Python itu menyenangkan"
result_2 = re.search(r'Python', text)
if result_2:
    print(f"Ketemu: {result_2.group()}")  # Output: Ketemu: Python
    
text_2 = "Email saya adalah ahmad@example.com dan info@example.org"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text_2)
print(emails)  # Output: ['ahmad@example.com', 'info@example.org']

text_3 = "Ahmad suka Python. Ahmad belajar setiap hari."
result_3 = re.sub(r'Ahmad', 'Dia', text_3)
print(result_3)
# Output: Dia suka Python. Dia belajar setiap hari.

#Email validator 
def check_email(email):
    results = re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)
    if results:
        return "Email valid"
    return "Email tidak valid"
print(check_email('ahmad@gmail.com'))

# Mengubah semua string menjadi *
def hidden_password(password):
    return re.sub(r'.', '*',  password)

password = "1234"
print(hidden_password(password))

def hidden_password(password):
    return re.sub(r'[A-Za-z]', '*', password)

password = "Pass1234"
print(hidden_password(password))  # Output: ****Pass1234

def hidden_password(password):
    return re.sub(r'\d', '*', password)

password = "Pass1234"
print(hidden_password(password))  # Output: Pass****