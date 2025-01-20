# Synchronous 
def say_hello():
    print("Hello!")
    return "Done"

result = say_hello()
print(result)

# Asynchronous 
import asyncio

async def say_hello():
    print("Hello!")
    return "Done"

# Menjalankan fungsi asynchronous
asyncio.run(say_hello())

# Await 


async def proses_a():
    print("Proses A dimulai")
    await asyncio.sleep(2)  # Simulasi proses lama
    print("Proses A selesai")

async def proses_b():
    print("Proses B dimulai")
    await asyncio.sleep(1)  # Simulasi proses lama
    print("Proses B selesai")

async def main():
    await proses_a()
    await proses_b()

asyncio.run(main())

# async io gather untuk menjalankan tugas secara bersamaan

async def proses_a():
    print("Proses A dimulai")
    await asyncio.sleep(2)
    print("Proses A selesai")

async def proses_b():
    print("Proses B dimulai")
    await asyncio.sleep(1)
    print("Proses B selesai")

async def main():
    await asyncio.gather(proses_a(), proses_b())

asyncio.run(main())

# async io create task

async def proses_a():
    print("Proses A dimulai")
    await asyncio.sleep(2)
    print("Proses A selesai")

async def proses_b():
    print("Proses B dimulai")
    await asyncio.sleep(1)
    print("Proses B selesai")

async def main():
    task_a = asyncio.create_task(proses_a())
    task_b = asyncio.create_task(proses_b())

    await task_a
    await task_b

asyncio.run(main())

# input output application 

async def baca_file(file):
    print(f"Membaca {file}...")
    await asyncio.sleep(1)  # Simulasi waktu baca
    print(f"File {file} selesai dibaca")

async def main():
    await asyncio.gather(
        baca_file("file1.txt"),
        baca_file("file2.txt"),
        baca_file("file3.txt"),
    )

asyncio.run(main())