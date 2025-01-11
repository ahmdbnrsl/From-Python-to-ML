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

data = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(data)
print("Sorted array:", data)