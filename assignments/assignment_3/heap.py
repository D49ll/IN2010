def BubbleDown(A,i,n):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and A[largest] < A[left]:
        largest, left = left, largest
    
    if right < n and A[largest] < A[right]:
        largest, right = right, largest
    
    if i != largest:
        A.swap(largest,i)
        BubbleDown(A, largest, n)

def BuildMaxHeap(A,n):
    for i in reversed(range(0, n//2)):
        BubbleDown(A,i,n)
    return A

def sort(A):
    BuildMaxHeap(A,len(A))
    for i in reversed(range(0,len(A))):
        A.swap(i,0)
        BubbleDown(A,0,i)
    return A