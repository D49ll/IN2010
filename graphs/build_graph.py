from collections import defaultdict #default dict raises no KeyError
import graphviz

def build_graph(lines):
    #Input er en tekstfil hvor hver linje 
    #representerer kanten mellom to noder
    #og vekten til kanten.

    V = set() #Nodes
    E = defaultdict(set) #Edges
    w = dict() #Weights

    #Ser på en linje om gangen
    for line in lines.splitlines():
        v, u, weight = line.strip().split()

        #Add nodes to graph
        V.add(v) 
        V.add(u)

        #Add edges from v to u, u to v
        E[v].add(u)
        E[u].add(v)
        print(E[v])
        #Add weights to the edges
        w[(v, u)] = int(weight)
        w[(u, v)] = int(weight)

    return V, E, w

def draw_graph(G):
    V, E, w = G

    dot = graphviz.Graph()
    seen_edges = set()

    for v in V:
        dot.node(v) #Lager en node

        for u in E[v]:
            if (u, v) in seen_edges:
                continue
            seen_edges.add((v, u))
            dot.edge(v, u, label=str(w[(v, u)]))

    dot.render('graph', format='png')

def dfs_rec(G, start, visited, path):
    #Ønsker kun å se på kanter til grafen
    _, E, _ = G

    path.append(start) #Definerer start posisjon
    visited.add(start) #Oppdaterer at vi har vært i start noden

    for v in E[start]:
        if v not in visited:
            dfs_rec(G, v, visited, path)

    return path



def main():
    f = open("inout/simple_graph.txt")
    lines = f.read()

    print(lines)

    G = build_graph(lines)
    draw_graph(G)

    print(dfs_rec(G, 'A',set(),list()))



main()
