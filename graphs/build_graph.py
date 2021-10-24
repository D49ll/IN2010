from collections import defaultdict
from heapq import heappush, heappop

import functions as fn

def dijkstra(G, start):
    _, E, w = G
    Q = [(0, start)] #Oppdaterer startposisjon og kost. Legger dette på Q
    D = defaultdict(lambda: float('inf'))
    D[start] = 0 #Oppdaterer spenntreet med kost for startposisjon

    parents = {start: None}

    while Q: #Så lenge det er noe i kø
        
        cost, v = heappop(Q) #Henter det minste elementet (noden) og tilhørende kost for å komme dit

        for u in E[v]: #Sjekker kantene til det minste elementet (noden)
            c = cost + w[(v,u)] #Oppdaterer kost, dvs nåværende kost + kosten det vil ha å traversere fra v til u
            if c < D[u]: #Dersom denne totale kosten er mindre enn den tidligere kosten endres den. Hust at D[u] initieres til uendelig ved første traversering
                D[u] = c
                heappush(Q, (c,u))#Den nye kosten for å nå u legges på heapen, sammen med aktuell node.
                
                parents[u] = v #Oppdaterer foreldren til u. Den som putter u på køen.

    return parents




if __name__=='__main__':
    f = open("inout/R_14-1")
    lines = f.read()

    #Bygge grafer basert på input
    G = fn.build_graph_undir(lines)
    G_dir = fn.build_graph_dir(lines)

    V,E,_ = G_dir

    print(E)
    #Visualiserer grafene
    fn.draw_graph_dir(G_dir,'Directed')
    fn.draw_graph_undir(G, 'Undirected')
    
    #Utfører operasjoner på grafer
    #D = dijkstra(G, 'A')

    #fn.draw_parents_weighted(G, D, 'dijkstra_spanningtree')
    