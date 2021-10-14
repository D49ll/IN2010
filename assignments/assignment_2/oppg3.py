from collections import defaultdict
from heapq import heappush, heappop

import oppg1
import oppg2

def shortest_path_dijkstra_best_rating(G, s):
    '''
    Tar inn:
        G - Graf: Tuple av dict: skuespiller og film
        s - Start_node: string: skuespiller-id

    Returnerer:
        parents_path - dict
            key: node_id
            value: tuple(foreldre node_id, høyeste kant)
    '''    
    V, E = G
    Q = [(0, s)]
    D = defaultdict(lambda: float('inf'))
    D[s] = 0
    parents_path = {s : (None, None)} 

    while Q:
        cost, v = heappop(Q)
        for e in V[v].get_movies():
            c = cost + (10-float(E[e].get_rating()))
            for u in E[e].get_actors():
                if c < D[u] and v != u:
                    D[u] = c
                    heappush(Q, (c, u))
                    parents_path[u] = (v, e)
    return parents_path


def main():
    f1 = 'actors.tsv'
    f2 = 'movies.tsv'
    G = oppg1.make_graph(f1, f2)
    start_list = ['nm2255973', 'nm0424060', 'nm4689420', 'nm0000288', 'nm0031483']
    end_list = ['nm0000460', 'nm0000243', 'nm0000365', 'nm0001401', 'nm0931324']
    
    
    for s, e in zip(start_list, end_list):
        span_tree = shortest_path_dijkstra_best_rating(G, s)
        shortest_path = oppg2.bfs_shortest_path_between(span_tree, e)
        oppg2.pretty_print(G, s, shortest_path, weight = True)


def solu_func(G):
    start_list = ['nm2255973', 'nm0424060', 'nm4689420', 'nm0000288', 'nm0031483']
    end_list = ['nm0000460', 'nm0000243', 'nm0000365', 'nm0001401', 'nm0931324']
    
    
    for s, e in zip(start_list, end_list):
        span_tree = shortest_path_dijkstra_best_rating(G, s)
        shortest_path = oppg2.bfs_shortest_path_between(span_tree, e)
        oppg2.pretty_print(G, s, shortest_path, weight = True)

if __name__ == "__main__":
    main()