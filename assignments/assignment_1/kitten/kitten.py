f = open('test0.in', 'r') #Open inputfile

Lines = f.read().splitlines() #read each line of file

print(Lines)
cat_position = int(Lines[0])
parent = []
child = [[]]
search_index = 0
run = True

for i in range(1, len(Lines)):
    string = Lines[i].split(" ")
    parent[search_index] = string[i]

    for j in range(len(string)):
        child[search_index][j] = string[j] 

    print(string[0])
    print(string[1:])
    
    search_index =+ search_index




