def inSort(A):
    n=len(A)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]
    return A

def insertionSort(A):
    for j in range(len(A)):
        key = A[j]
        i = j-1
        while i>-1 and A[i]>key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A    

A = [8, 2, 4, 9, 3, 6]
print(inSort(A))