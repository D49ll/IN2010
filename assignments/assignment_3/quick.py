def ChoosePivot(A,low,high):
    '''
    Inn: Et array av usorterte heltall, A.
    Ut: Indeksen til pivotelementet i A.
    '''
    M = list()
    
    #Sorterer verdiene og finner medianen (pivotelementet)
    #Den vil alltid være på posisjon M[1]
    n = (high+low)
    M.append(A[low])
    M.append(A[n//2])
    M.append(A[high])
    M.sort()

    #Returnerer indeks til pivotelementet i A
    if M[1] == A[low]:
        return low
    elif M[1] == A[high]:
        return high
    else:
        return n//2

def Partition(A,low,high):
    #Finner indeksen til pivotelementet
    p = ChoosePivot(A,low,high)


    #Flytter pivotelementet til slutten av A. 
    #Slik vil man ikke overskriver det i partisjoneringen.
    A.swap(high,p)
    #A[p],A[high] = A[high],A[p]

    
    pivot = A[high] #Lagrer verdien til pivotelementet, A[high] kan dermed overskrives
    left = low      #Initierer venstre index
    right = high-1  #Initierer høyre index

    #Dersom indeksene krysser skal vi ikke utføre mer operasjoner
    #Da vil alle verdier til venstre være mindre enn pivotelemenet
    #Og alle verider til høyre være større enn pivotelementet
    while left <= right:

        #Øker left-indeks til vi finner et element som er større enn pivotelementet
        while left <= right and A[left]<=pivot:
            left +=1
        
        #Minker right-indeks til vi finner et element som er større enn pivotelementet
        while right >= left and A[right]>=pivot:
            right -= 1

        #Når man har funnet to nye elementer som er større og mindre enn pivotelementet
        #må disse bytte plass. Slik det store element blir flyttet til høyre og visaversa
        if left < right:
            #A[left],A[right] = A[right],A[left]
            A.swap(right,left)

    #A[left],A[high] = A[high],A[left]
    A.swap(high,left)
    return left

def sort(A,low=None,high=None):

    #Første iterasjon har ingen argumenter
    #Settes til 0 og n-1
    if low is None and high is None:
        low = 0
        high = len(A)-1

    if low >= high:
        return A
    partition = Partition(A,low,high)
    sort(A,low,partition-1)
    sort(A,partition+1,high)
    return A



# # For å teste algoritmen:
# f = open('inputs/nearly_sorted_10000').read()

# A = list()
# B = list()
# for number in f.splitlines():
#     A.append(int(number))
#     B.append(int(number))


# sort(A,0,len(A)-1)

# if A == sorted(B):
#     print('algoritmen funker')
# # for el in A:
#     # print(el)