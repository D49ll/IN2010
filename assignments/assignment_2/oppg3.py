from collections import defaultdict
from heapq import heappush, heappop

import oppg1
import oppg2

def shortest_path_dijkstra_best_rating(G, start, end=None):
    '''
    Tar inn:
        G - Graf: Tuple av dict: skuespiller og film
        start - Start_node: string: skuespiller-id
    Returnerer:
        parents_path - dict
            key: node_id
            value: tuple(foreldre node_id, høyeste kant)
    '''    
    V, E = G #Finner alle kanter og noder
    Q = [(0, 0, start)] #Første steg koster ingenting, legger dette i køen
    D = defaultdict(lambda: (float('inf'), float('inf'))) #Oppretter en defaultdict D for (Antall steg, rating). D blir initiert med steg = inf og rating = 0
    
    D[start] = (0,0) #Oppdaterer steg for å stå i start

    parents_path = {start : (None, None)} #Første steg
    final_step = float('inf')

    while Q:
        #Henter fra kø
        step, rating, v = heappop(Q)
        
        step += 1
        if final_step < step:
            return parents_path

        #For alle kanter tilhørende noden v
        for e in V[v].get_movies():
            current_movie_rating = (10-float(E[e].get_rating()))
            tot_rating = rating + current_movie_rating
            #oppdaterer kosten til aktuell kant, NB! den inverse verdien.
            
            #Sjekker alle noder aktuell kant leder til
            for u in E[e].get_actors():
                if end == u:
                    final_step = step
                #Finner den kanten med minst kost
                if step <= D[u][0] and tot_rating <= D[u][1] and v != u:
                    D[u] = (step, tot_rating)
                    heappush(Q, (step, tot_rating, u))
                    parents_path[u] = (v, e)
 
                
    return parents_path


def main():
    f1 = 'actors.tsv'
    f2 = 'movies.tsv'
    G = oppg1.make_graph(f1, f2)
    start_list = ['nm2255973', 'nm0424060', 'nm4689420', 'nm0000288', 'nm0031483']
    end_list = ['nm0000460', 'nm0000243', 'nm0000365', 'nm0001401', 'nm0931324']
    
    
    for start, end in zip(start_list, end_list):
        span_tree = shortest_path_dijkstra_best_rating(G, start, end)
        shortest_path = oppg2.bfs_shortest_path_between(span_tree, end)
        oppg2.pretty_print(G, start, shortest_path, weight = True)


def solu_func(G):
    start_list = ['nm2255973', 'nm0424060', 'nm4689420', 'nm0000288', 'nm0031483']
    end_list = ['nm0000460', 'nm0000243', 'nm0000365', 'nm0001401', 'nm0931324']
    
    
    for start, end in zip(start_list, end_list):
        span_tree = shortest_path_dijkstra_best_rating(G, start, end)
        shortest_path = oppg2.bfs_shortest_path_between(span_tree, end)
        oppg2.pretty_print(G, start, shortest_path, weight = True)

if __name__ == "__main__":
    main()