def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in (n-1, i, -1):
            if arr[j] < arr[i-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = arr[j]
    return arr

print(f"List after sorting: {bubble_sort([5, 7, 1, 8, 9, 12, 12, 34, 78, 4])}")