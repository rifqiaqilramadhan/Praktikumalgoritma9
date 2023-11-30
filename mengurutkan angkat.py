def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def binary_search(sorted_arr, target):
    low, high = 0, len(sorted_arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = sorted_arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def search_and_sort(arr, target):
    bubble_sort(arr)
    index = binary_search(arr, target)

    if index != -1:
        print(f"Element {target} ditemukan pada indeks {index}.")
    else:
        print(f"Element {target} tidak ditemukan dalam list.")

angka = print(87, 56, 34, 23, 89, 15, 2, 200, 28, 31)
target_element = int(input("Masukkan nilai target: "))

my_list = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

my_list = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]

bubble_sort(my_list)

print("List setelah diurutkan:", my_list)

search_and_sort(my_list, target_element)