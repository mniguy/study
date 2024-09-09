def countingSort(arr):
    n = len(arr)
    k = max(arr) + 1
    count = [0] * k
    for i in range(n):
        count[arr[i]] += 1
    
    for i in range(1, k):
        count[i] += count[i - 1]
    
    output = [0] * n
    m = n - 1
    while m >= 0:
        output[count[arr[m]] - 1] = arr[m]
        count[arr[m]] -= 1
        m -= 1
    for i in range(n):
        arr[i] = output[i]
    return arr                

arr = [3, 1, 5, 4, 8, 2]
countingSort(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")