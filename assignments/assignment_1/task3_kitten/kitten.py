#Read from file
f = open('inputs/input_5', 'r')
input_ = f.read().splitlines() #Uses \n as delimitor

#Kattis
#import sys
#in_str = sys.stdin.read().splitlines() 

#Define lists
parents = []
children = []
path = []

#Cat location from input
cat = int(input_[0])
path.append(cat)

#Create a list of parents and children
i = 1
while True:
    node = input_[i].split(" ")

    parent = int(node[0])
    child = [int (b) for b in node[1:]]

    if parent == -1:
        break
    
    parents.append(parent)
    children.append(child)
    i += 1


#Find next step by looking for cat in children
i = 0
while i < len(children):
    if cat in children[i]:
        cat = parents[i]
        path.append(cat)
        i = 0
    else:
        i += 1

#Kattis requires string output 
for step in path:
    print(str(step))
