A = [x for x in range(10)]

balanced = []

def print_binary_tree(A,balanced):
    if len(A) == 2:
        balanced.append(A[-1])
        balanced.append(A[-2])
        #print(A[-1])
        #print(A[-2])

    elif len(A) == 1:
        balanced.append(A[-1])
        #print(A[-1])
    
    #elif len(A)%2 == 1:
    else:
        parent_index = len(A) // 2
        balanced.append(A[parent_index])
        #print(A[parent_index])
        right_child_array = A[parent_index+1:]
        left_child_array = A[:parent_index]
        
        print_binary_tree(right_child_array, balanced)
        print_binary_tree(left_child_array, balanced)
    '''
    else:
        parent_index = (len(A)//2) - 1
        balanced.append(A[parent_index])
        #print(A[parent_index])

        right_child_array = A[parent_index+1:]
        left_child_array = A[:parent_index]
        print_binary_tree(right_child_array, balanced)
        print_binary_tree(left_child_array, balanced)
    '''

    return balanced

test = print_binary_tree(A, balanced)
print(test)

#string_ints = [str(int) for int in test]

#test2=" ".join(string_ints)

#print(test2)
