def bubble_sort(arr):
    n = len(arr)
    print("Process starting...")
    for i in range(n):
        print(f"Outer Loop at : {i + 1}")
        for j in range(0, n-i-1):
            print(f"Inner Loop at : {j + 1}")
            if arr[j] > arr[j+1]:
                print(f"Sorting Process : {arr}")
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    for i in range(len(arr)):
        # Anggap elemen pertama adalah yang terkecil
        min_idx = i
        
        for j in range(i+1, len(arr)):
            print("Min idx ", min_idx)
            if arr[j] < arr[min_idx]:
                print(j)
                min_idx = j
        # Tukar elemen terkecil ke posisi i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

data = [64, 25, 12, 22, 11]

selection_sort(data)
print("Sorted array:", data)

bubble_sort(data)
print("Sorted array:", data)