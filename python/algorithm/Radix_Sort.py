def countingSort(arr, place):
    n = len(arr)
    count = [0]*10
    output = [0]*n
    
    for i in range(n):
        index = arr[i] // place
        count[index % 10] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    i = n - 1
    while i >= 0:
        index = arr[i] // place
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
        
    for i in range(n):
        arr[i] = output[i]
    
def radixSort(arr):
    max_element = max(arr)
    
    place = 1
    while max_element//place > 0:
        countingSort(arr, place)
        place *= 10
    
arr = [133, 245, 612, 901, 322]
radixSort(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")        