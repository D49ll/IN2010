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
            i -= i

    def push_middle(self,x):
        length = len(self.queue)
        i = ((length + 1) // 2)

        while i < length:
            

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



