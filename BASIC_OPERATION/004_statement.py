# if

umur = 18
if umur >= 18:
    print("Kamu sudah dewasa")

# if and else

if umur >= 18:
    print("Kamu sudah dewasa")
else:
    print("Kamu masih anak-anak")

# if, elif, else

nilai = 85
if nilai >= 90:
    print("Grade: A")
elif nilai >= 80:
    print("Grade: B")
elif nilai >= 70:
    print("Grade: C")
else:
    print("Grade: D")

# logical operator
# >, <, >=, <=, ==, !=

is_coding = True
is_student = False

if is_coding and not is_student:
    print("Kamu programmer!")

umur_2 = 20
is_student_2 = True

if umur_2 >= 18 and is_student_2:
    print("Kamu mahasiswa dewasa")
elif umur < 18:
    print("Kamu masih anak-anak")
else:
    print("Kamu sudah dewasa, tapi bukan mahasiswa")
