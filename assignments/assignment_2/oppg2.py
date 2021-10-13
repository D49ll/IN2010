from collections import defaultdict, deque
from heapq import heappush, heappop

import oppg1

'''
Oioioi. Her var teksten noe utydelig. Tolket det som at i denne oppgaven var vekten 
på kantene var ratingen. Dette gjorde det noe mer kopmplisert.
'''

def shortest_path_dijkstra(G, s):
    '''
    Tar inn:
        G - Graf: Tuple av dict: skuespiller og film
        s - Start_node: string: skuespiller-id

    Returnerer:
        parents_path - dict
            key: node_id
            value: tuple(foreldre node_id, korteste kant)
    '''
    V, E = G
    Q = [(0, s)]
    D = defaultdict(lambda: float('inf'))
    D[s] = 0
    parents_path = {s : (None, None)}

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

def bfs_shortest_path_from(G,start,end):
    V, E = G

    parents = {start : None}
    queue = deque([start])    

    while queue:
        actor = deque.popleft(queue)

        for movie in V[actor].get_movies(): #Finner alle kanter i en til en skuesl
            for actor2 in E[movie].get_actors(): #Finner alle skuespillerene i gitt film
                
                if actor2 == end:
                    parents[actor2] = (actor,movie)
                    return parents

                if actor2 not in parents:
                    parents[actor2] = (actor, movie)
                    queue.append(actor2)

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
        if v is None:
            break
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

        print(f'===[ {title} ({rating}) ] ===> {next_actor}')
        
        w += (10-float(rating))
    if weight:
        print(f'Total weight: {round(w,1)}')

def main():
    f1 = 'actors.tsv'
    f2 = 'movies.tsv'
    G = oppg1.make_graph(f1, f2)
    
    start_list = ['nm2255973', 'nm0424060', 'nm4689420', 'nm0000288', 'nm0031483']
    end_list = ['nm0000460', 'nm0000243', 'nm0000365', 'nm0001401', 'nm0931324']
    
    for s, e in zip(start_list, end_list):
        span_tree = bfs_shortest_path_from(G,s,e)
        shortest_path = bfs_shortest_path_between(span_tree, e)
        pretty_print(G, s, shortest_path)

def solu_func(G):
    start_list = ['nm2255973', 'nm0424060', 'nm4689420', 'nm0000288', 'nm0031483']
    end_list = ['nm0000460', 'nm0000243', 'nm0000365', 'nm0001401', 'nm0931324']
    
    for s, e in zip(start_list, end_list):
        span_tree = bfs_shortest_path_from(G,s,e)

        #span_tree = shortest_path_dijkstra(G, s)
        shortest_path = bfs_shortest_path_between(span_tree, e)
        pretty_print(G, s, shortest_path)



if __name__ == '__main__':
    main()
