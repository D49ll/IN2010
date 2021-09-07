class Teque:
    def __init__(self):
        self.queue = []

    def push_back(self, x):
        self.queue.append(x)

    def push_front(self, x):
        self.queue.insert(0,x)

    def push_middle(self,x):
        i = ((len(self.queue)+ 1) // 2)
        self.queue.insert(i, x)

    def get(self, i):
        print(self.queue[i])

q = Teque()

f = open('teque/1.in', 'r')

Lines = f.readlines()

n = int(Lines[0])

for i in range(1, n+1):
    msg, x = Lines[i].split(" ")
    x = int(x)
    if msg == "push_back":
        q.push_back(x)
    elif msg == "push_front":
        q.push_front(x)
    elif msg == "push_middle":
        q.push_middle(x)
    else:
        q.get(x) # x = i





'''
q = Teque()

q.push_back(9)
q.push_front(3)
q.push_middle(5)

for i in range(3):
    q.get(i)

q.push_middle(1)

for i in range(1, 3):
    q.get(i)
'''