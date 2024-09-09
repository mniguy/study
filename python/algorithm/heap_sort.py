def heapify(arr, n, i):
    largest = i
    l = 2*i
    r = 2*i + 1

    if l<n and arr[i]<arr[l]:
        largest = l
    if r<n and arr[largest]<arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        return heapify(arr, n, largest)
    return arr
    
def heapSort(arr):
    n = len(arr)

    for i in range(n//2, 0, -1):
        arr = heapify(arr, n, i)
    for i in range(n - 1, 1, -1):
        (arr[i], arr[1]) = (arr[1], arr[i])
        arr = heapify(arr, i, 1)
    return arr
    
arr = [None, 12, 11, 13, 5, 6, 7]
arr = heapSort(arr)
n = len(arr)
print('Sorted array')
for i in range(n):
    print(arr[i], end=" ")