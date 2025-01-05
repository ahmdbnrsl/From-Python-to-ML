# For Loop

hobi = ["coding", "painting", "math"]
for item in hobi:
    print(item)

# While Loop

i = 1
while i <= 5:
    print(i)
    i += 1  # Increment

# Example

# List dan For Loop
for h in hobi:
    print(f"Saya suka {h}")

# Dictionary dan For Loop
profil = {"nama": "Ahmad", "umur": 25, "tinggi": 170.5}
for key, value in profil.items():
    print(f"{key}: {value}")

# While Loop
countdown = 3
while countdown > 0:
    print(f"Hitung mundur: {countdown}")
    countdown -= 1
print("Selesai!")
