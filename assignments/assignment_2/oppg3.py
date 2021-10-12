from collections import deque
from heapq import heappush, heappop
from collections import defaultdict

import oppg1
import oppg2

def shortest_path_dijkstra_best_rating(G, s):
    V, E = G
    Q = [(0, s)]
    D = defaultdict(lambda: float('inf'))
    D[s] = 0
    parents_path = {s : (None, None)}   #node : (foreldrenode, vekt)

    while Q:
        cost, v1 = heappop(Q)
        for e in V[v1].get_movies():
            c = cost + (10-float(E[e].get_rating()))
            for v2 in E[e].get_actors():
                if c < D[v2] and v1 != v2:
                    D[v2] = c
                    heappush(Q, (c, v2))
                    parents_path[v2] = (v1, e)
    return parents_path


def main():
    f1 = 'actors.tsv'
    f2 = 'movies.tsv'
    G = oppg1.make_graph(f1, f2)
    start_list = ['nm2255973', 'nm0424060', 'nm4689420', 'nm0000288', 'nm0031483']
    end_list = ['nm0000460', 'nm0000243', 'nm0000365', 'nm0001401', 'nm0931324']
    for i in range(len(start_list)):
        shortest_path = oppg2.bfs_shortest_path_between(shortest_path_dijkstra_best_rating(G, start_list[i]), end_list[i])
        oppg2.pretty_print(G, start_list[i], shortest_path, weight=True)


if __name__ == "__main__":
    main()
    pass