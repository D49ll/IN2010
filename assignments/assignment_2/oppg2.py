from collections import defaultdict, deque
from heapq import heappush, heappop

import oppg1

'''
Oioioi. Her var teksten noe utydelig. Tolket det som at i denne oppgaven var vekten 
på kantene var ratingen. Dette gjorde det noe mer kopmplisert.
'''

# def shortest_path_dijkstra(G, s):
#     '''
#     Tar inn:
#         G - Graf: Tuple av dict: skuespiller og film
#         s - Start_node: string: skuespiller-id

#     Returnerer:
#         parents_path - dict
#             key: node_id
#             value: tuple(foreldre node_id, korteste kant)
#     '''
#     V, E = G
#     Q = [(0, s)]
#     D = defaultdict(lambda: float('inf'))
#     D[s] = 0
#     parents_path = {s : (None, None)}

#     while Q:
#         cost, v1 = heappop(Q)
#         for e in V[v1].get_movies():
#             c = cost + float(E[e].get_rating())
#             for v2 in E[e].get_actors():
#                 if c < D[v2] and v1 != v2:
#                     D[v2] = c
#                     heappush(Q, (c, v2))
#                     parents_path[v2] = (v1, e)

#     return parents_path

def bfs_shortest_path_from_to(G,start,end=None):
    '''
    Inn:
        En graf, G (tuple(V, E))
        En startnode (str)
        En sluttnode (str)

    Ut:
        En dict, parents = {node : (foreldrenode, kant som forbinder dem)}
            key: Node
            val: tuple(Foreldrenode, Kant som forbinder dem)
    '''
    V, E = G
    parents = {start : (None, None)}
    queue = deque([start])    

    while queue:
        #Henter fra kø (FIFO)
        v = deque.popleft(queue)

        #Ser på alle kanter til en node
        for e in V[v].get_movies():
            #Finner alle noder som forbindes med aktuell kant
            for u in E[e].get_actors():
                
                #Dersom noden vi finner sluttnoden så
                #returneres parents
                if u == end:
                    parents[u] = (v,e)
                    return parents

                #Dersom noden ikke finnes i parents
                #Legges den til, deretter settes den tilbake i køen
                if u not in parents:
                    parents[u] = (v, e)
                    queue.append(u)

    return parents

def bfs_shortest_path_between(parents, end):
    '''
    Tar inn:
        parents - dict
            key: node_id
            value: tuple(foreldre node_id, korteste kant)
        end - End_node: string: skuespiller-id

    Returnerer:
        Kortest vei fra rot til sluttnode definert av end
    '''
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

    print()
    print(V[start_node].get_name())

    for i in range(len(shortest_path)-1):
        rating = E[shortest_path[i][1]].get_rating()
        title = E[shortest_path[i][1]].get_title()
        next_actor = V[shortest_path[i+1][0]].get_name()
        w += (10-float(rating))

        print(f'===[ {title} ({rating}) ] ===> {next_actor}')
    if weight:
        print(f'Total weight: {round(w,1)}')

def main():
    f1 = 'actors.tsv'
    f2 = 'movies.tsv'
    G = oppg1.make_graph(f1, f2)
    V, E = G
    start_list = ['nm2255973', 'nm0424060', 'nm4689420', 'nm0000288', 'nm0031483']
    end_list = ['nm0000460', 'nm0000243', 'nm0000365', 'nm0001401', 'nm0931324']
    
    for start, end in zip(start_list, end_list):
        span_tree = bfs_shortest_path_from_to(G,start,end)
        
        shortest_path = bfs_shortest_path_between(span_tree, end)
        pretty_print(G, start, shortest_path)

def solu_func(G):
    start_list = ['nm2255973', 'nm0424060', 'nm4689420', 'nm0000288', 'nm0031483']
    end_list = ['nm0000460', 'nm0000243', 'nm0000365', 'nm0001401', 'nm0931324']
    
    for start, end in zip(start_list, end_list):
        span_tree = bfs_shortest_path_from_to(G,start,end)

        #span_tree = shortest_path_dijkstra(G, start)
        shortest_path = bfs_shortest_path_between(span_tree, end)
        pretty_print(G, start, shortest_path)



if __name__ == '__main__':
    main()
