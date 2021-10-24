from collections import defaultdict #default dict raises no KeyError
import graphviz

def dfs_rec(G, start, visited, path):
    #Ønsker kun å se på kanter til grafen
    _, E, _ = G

    path.append(start) #Definerer start posisjon
    visited.add(start) #Oppdaterer at vi har vært i start noden

    for v in E[start]:
        if v not in visited:
            dfs_rec(G, v, visited, path)

    return path

def build_graph_undir(lines):
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
        #This makes the grap undirected
        E[v].add(u)
        E[u].add(v)
        #print(E[v])
        
        #Add weights to the edges
        w[(v, u)] = int(weight)
        w[(u, v)] = int(weight)

    return V, E, w

def draw_graph_undir(G,name):
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

def build_graph_dir(lines):
    V = set() #Nodes
    E = defaultdict(set) #Edges
    w = dict()

    for line in lines.splitlines():
        v, u, weight = line.strip().split()

        #Legger til v og u i V. Da det er set() vil aldri noen verdier gjentas
        V.add(v)
        V.add(u)

        #Retningen blir bestemt av hvordan formatet 
        E[v].add(u)
        w[(v,u)] = int(weight)
    
    return V,E,w

def draw_graph_dir(G, name):
     V, E, w = G
     dot = graphviz.Digraph()

     for u in V:
          dot.node(u)

          for v in E[u]:
               dot.edge(u, v, label=str(w[(u, v)]))

     dot.render(name, format='png')

def draw_parents_weighted(G, parents, name):
    V, _, w = G
    dot = graphviz.Graph()
    for v in parents:
        u = parents[v]
        if u:
            dot.edge(v, u, label=str(w[(v, u)]))
    dot.render(name, format='png')



