# from oppg1_copy import actors, movies 
from collections import deque
from heapq import heappush, heappop
from collections import defaultdict

import oppg1

'''
Oioioi. Her var teksten noe utydelig. Tolket det som at i denne oppgaven var vekten 
på kantene var ratingen. Dette gjorde det noe mer kopmplisert.
'''

'''
Har kun testet hvordan man kan få tak i informasjonen vi trenger fra oppg1 her.
Det som står nå skal funke, prøv med debugger som jeg viste for å teste.
Tror din brukte så lang tid fordi det er et stort datasett.
Så anbefaler å bruke _2 filene, men gjør dem større om du må for å få med skuespillerne du skal teste koden på.
Må implementere algoritmene som det står om på forelesning.
Fordelen er at oppg2 har korteste vei som er 2 kanter for alle (se utskrift i oppgavesett)
'''

def dijkstra(G, s):
    V, E = G
    Q = [(0, s)]
    D = defaultdict(lambda: float('inf'))
    D[s] = 0
    
    while Q:
        cost, v1 = heappop(Q)
        for e in V[v1].get_movies():
            c = cost + float(E[e].get_rating())
            for v2 in E[e].get_actors():
                if c < D[v2]:
                    D[v2] = c
                    heappush(Q, (c, v2))
    return D

def shortest_path_dijkstra(G, s):
    V, E = G
    Q = [(0, s)]
    D = defaultdict(lambda: float('inf'))
    D[s] = 0
    parents_path = {s : (None, None)}   #node : (foreldrenode, vekt)

    while Q:
        cost, v1 = heappop(Q)
        for e in V[v1].get_movies():
            c = cost + float(E[e].get_rating())
            for v2 in E[e].get_actors():
                if c < D[v2] and v1 != v2:
                    D[v2] = c
                    heappush(Q, (c, v2))
                    parents_path[v2] = (v1, e)
    return parents_path

def bfs_shortest_from(G, s):
    '''
    Tar inn:
        G - Graf: Tuple av dict: skuespiller og film
        s - Start_node: string: skuespiller-id
        e - End_node: string: skuespiller-id
    '''
    V, E = G
    parents = {s : None}
    queue = deque([s])
    result = []

    while queue:
        v1 = deque.popleft(queue)    # key of actor
        result.append(v1)            # add 
        for e in V[v1].get_movies():
            for v2 in E[e].get_actors():
                if v2 not in parents:
                    parents[v2] = v1
                    queue.append(v2)
    return parents

def bfs_shortest_between(G, s, e):
    '''
    Tar inn:
        G - Graf: Tuple av dict: skuespiller og film
        s - Start_node: string: skuespiller-id
        e - End_node: string: skuespiller-id
    '''
    V, E = G
    parents = {s : None}
    queue = deque([s])
    result = []

    while queue:
        v1 = deque.popleft(queue)    # key of actor
        result.append(v1)            # add 
        for e in V[v1].get_movies():
            for v2 in E[e].get_actors():
                if v2 not in parents:
                    parents[v2] = v1
                    queue.append(v2)

    # while queue:
    #     v = deque.popleft(queue)
    #     result.append(v)
    #     for u in E[v]:
    #         if u not in parents:
    #             parents[u] = v
    #             queue.append(u)
    return parents

def bfs_shortest_path_between(parents, end):
    # parents = shortest_path_dijkstra(G, start)
    v = (end, None)
    path = []

    if end not in parents:
        return path

    while v[0]:
        path.append(v)
        v = parents[v[0]]
    return path[::-1]


def pretty_print(G, start_node, shortest_path, weight = False ):
    V, E = G
    w = 0
    print(V[start_node].get_name())
    for i in range(len(shortest_path)-1):
        rating = E[shortest_path[i][1]].get_rating()
        print(f'===[ {E[shortest_path[i][1]].get_title()} ({rating}) ] ===> {V[shortest_path[i+1][0]].get_name()}')
        w += (10-float(rating))
    if weight:
        print(f'Total weight: {round(w,1)}')

def main():
    f1 = 'actors.tsv'
    f2 = 'movies.tsv'
    G = oppg1.make_graph(f1, f2)
    start_list = ['nm2255973', 'nm0424060', 'nm4689420', 'nm0000288', 'nm0031483']
    end_list = ['nm0000460', 'nm0000243', 'nm0000365', 'nm0001401', 'nm0931324']
    for i in range(len(start_list)):
        shortest_path = bfs_shortest_path_between(shortest_path_dijkstra(G, start_list[i]), end_list[i])
        pretty_print(G, start_list[i], shortest_path)

def uten_vekting():
    f1 = 'actors2.tsv'
    f2 = 'movies2.tsv'
    G = oppg1.make_graph(f1, f2)
    start_node = 'nm0353790'
    end_node = 'nm0853576'
    parents = bfs_shortest_from(G, start_node)

def redusert_datasett():
    f1 = 'actors2.tsv'
    f2 = 'movies2.tsv'
    G = oppg1.make_graph(f1, f2)
    s = 'nm0353790'
    parents = shortest_path_dijkstra(G, s)
    print(parents)
    # print(list(zip(*sorted(D.items()))))

def test_dijkstra():
    f1 = 'actors2.tsv'
    f2 = 'movies2.tsv'
    G = oppg1.make_graph(f1, f2)
    s = 'nm0353790'
    D = dijkstra(G, s)
    for key in D:
        print(f'{key}: {D[key]}')

def test_spd():
    f1 = 'actors2.tsv'
    f2 = 'movies2.tsv'
    G = oppg1.make_graph(f1, f2)
    start = 'nm0000001'
    end = 'nm0853576'
    # parent_path = shortest_path_dijkstra(G, start)
    shortest_path = bfs_shortest_path_between(G, start, end)
    for i in shortest_path:
        print(i)

if __name__ == '__main__':
    # uten_vekting()
    # test_dijkstra()
    # redusert_datasett()
    # test_spd()
    main()

    pass
