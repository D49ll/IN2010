from collections import defaultdict
from heapq import heappop, heappush
import graphviz

def build_graph(lines):
    V = set()
    E = defaultdict(set)
    w = dict()

    for line in lines.splitlines():
        v, u, weight = line.strip().split()

        V.add(v) 
        V.add(u)

        E[v].add(u)
        E[u].add(v)
        
        w[(v, u)] = int(weight)
        w[(u, v)] = int(weight)

    return V, E, w

def draw_graph(name,G):
    V, E, w = G

    dot = graphviz.Graph()
    seen_edges = set()

    for v in V:
        dot.node(v)

        for u in E[v]:
            if (u, v) in seen_edges:
                continue
            seen_edges.add((v, u))
            dot.edge(v, u, label=str(w[(v, u)]))

    dot.render(name, format='png')

def kruskalMST(G):
    '''
    Grådige kanter. 

    Algoritmen finner de billigste kantene mellom to par av noder.
    Danner deretter en kluster av disse. 
    Dette gjentas til vi bare har en kluster.
    Det minimale spenntreet vil da være funnet.
    Antall kanter skal tilsvare |V|-1
    
    '''
    V, E, w = G

    Q = list()
    seen_node = set()

    #Legger til alle kanter i heapen.
    for v in V:
        seen_node.add(v)
        for u in E[v]:
            if u in seen_node:
                continue
            heappush(Q, (w[(v,u)],(v,u)))

    i = 0
    from collections import defaultdict
    C = defaultdict(set)
    T = dict()

    for v in V:
        C[v].add(v)
    i = len(T)
    #print(C)
    k=1
    while i < (len(V)-1):
        print(f'\niteration {k}')
        value, (v,u) = heappop(Q)
        
        if len(C[v])>1 or len(C[u])>1:
            if (v in C[v] and u in C[u]) or (u in C[v] and v in C[u]):
                continue 
        print(f'Edge: {(v, u)} = {value}')
        
        print(f'C[v]={C[v]} and C[u]={C[u]}')
        if C[v] != C[u]:
            C[v].add(u)
            C[u].add(v)
            T[(v,u)] = value

        
        #print(C)
        print(T)
        i = len(T)
        k +=1

    #print(i)

def primsMST(G,start):
    V, E, w = G
    
    T = dict()
    Q = list()
    D = dict()

    for v in V:
        D[v] = float('inf')
        heappush(Q, ((v,None),D[v]))
    
    D[start] = 0

    while Q:
        (start,edge) = heappop(Q)
        
            

if __name__=='__main__':
    lines = open('R_15-1').read()

    G = build_graph(lines)
    draw_graph('Simple undirected graph',G)

