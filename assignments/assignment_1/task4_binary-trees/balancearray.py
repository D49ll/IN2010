def balanced_binary_tree_input(A,balanced):
    if len(A) == 2:
        balanced.append(A[-1])
        balanced.append(A[0])

    elif len(A) == 1:
        balanced.append(A[0])

    else:
        parent_index = len(A) // 2
        balanced.append(A[parent_index])
        
        right_child_array = A[parent_index+1:]
        left_child_array = A[:parent_index]
        balanced_binary_tree_input(right_child_array, balanced)
        balanced_binary_tree_input(left_child_array, balanced)

    return balanced
eq 10 | python3 balancearray.py | java BalanceChecker DDD

#Read/write to terminal
import sys

#Variables declaration
balanced_tree = []
sorted_input = []

#Reads input from terminal
for line in sys.stdin:
  sorted_input.append(int(line))

#Creates a input list representing a balanced tree
balanced_tree = balanced_binary_tree_input(sorted_input, balanced_tree)


#Converts input list to string
string_ints = [str(int) for int in balanced_tree]

#Writes output to terminal, with \n as delimitor
sys.stdout.write("\n".join(string_ints))


