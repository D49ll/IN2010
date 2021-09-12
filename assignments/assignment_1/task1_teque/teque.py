class Teque:
    def __init__(self):
        self.queue = []

    def push_back(self, x):
        i = len(self.queue)
        self.queue = self.queue + [x]

    def push_front(self, x):
        i = len(self.queue)
        self.queue = self.queue + [0]
        while 0 < i:
            self.queue[i] = self.queue[i-1]
            i = i - 1
        self.queue[i] = x

    def push_middle(self,x):
        i = len(self.queue)
        k = ((i + 1) // 2)

        self.queue = self.queue + [0]

        while k < i:
            self.queue[i] = self.queue[i - 1]
            i = i - 1 
        self.queue[i] = x 

    def get(self, i):
        print(self.queue[i])

#Kattis input
#import sys
#Lines = sys.stdin.readlines()

#Sample input


f = open('inputs/input_100000', 'r') #Open inputfile
Lines = f.readlines() #read each line of file


q = Teque() 

n = int(Lines[0]) #First line 

for i in range(1, n+1):
    msg, x = Lines[i].split(" ")
    x = int(x)
    #print(f"msg={msg} and int={x}")
    if msg == "push_back":
        q.push_back(x)
    elif msg == "push_front":
        q.push_front(x)
    elif msg == "push_middle":
        q.push_middle(x)
    elif msg == "get":
        q.get(x) # x = i

