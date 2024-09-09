def mergeSort(A):
    n = len(A)
    
    if n==1:
        return A
    mid = n//2
    L = mergeSort(A[:mid])
    R = mergeSort(A[mid:])
    return merge(L, R)

def merge(L, R):
    i=j=0
    answer = []
    
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            answer.append(L[i])
            i+=1
        else:
            answer.append(R[j])
            j+=1
    if i<len(L):
        answer.extend(L[i:])
    if j<len(R):
        answer.extend(R[j:])
    return answer

A = [12, 11, 13, 5, 6, 7]
print(mergeSort(A))

    
    