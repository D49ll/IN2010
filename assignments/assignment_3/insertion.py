def sort(A):
    for i in range(1, len(A)):
        j = i

        while j > 0 and A[j-1] > A[j]:
            A.swap(j-1, j) #A[j - 1], A[j] = A[j],A[j - 1]
            j -= 1
            
    return A