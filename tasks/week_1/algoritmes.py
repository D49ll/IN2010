'''
This python file will contain the different algoritmes showcased in the lectures.
They can be seen in the lecture slides written in pseudo-code. Here they will 
be referenced as "Algorithme x".
'''

#Algoritme 2: En enkel søkealgoritme
def Search(A, x):
    '''
    Input: Et array A og et element x
    Output: Hvis x er i arrayet A, returner True eller False
    '''
    print(len(A))
    for i in range(0, len(A)):
        print(i)
        if A[i] == x:
            return True
    
    return False

#Algoritme 2: Test
A = [1,1,2,3,1,2,10,2,3,4,5,11,12]
x = 11

print(f"Finnes {x} i A? {Search(A,x)}")



#Algoritme 4: Binærsøk
def BinarySearch(x, A):
    '''
    Input: Et ordnet array A og et element x
    Output: Hvis x er i arrayet A, returner True eller False
    '''
    low = 0
    high = len

