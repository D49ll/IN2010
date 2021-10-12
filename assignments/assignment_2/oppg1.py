from collections import defaultdict, deque
from heapq import heappush, heappop
from os import umask 
from classes import Movie, Actor
import time as t

#Starttid
start_time = t.time()

#Funksjoner for oppgave 1
def make_graph(f1, f2):
    '''
    Funksjon som leser inn to filer
    input: to filnavn
    output: dict med id som nøkkel og objekt som verdi
        actors
        movies
    '''
    # Leser filer
    actors_tsv = open(f1).read()
    movies_tsv = open(f2).read()

    # Variabler
    V = dict() #En ordbok som skal inneholder Actor objekter som er søkbar på actor-ID
    E = dict() #En ordbok som skal innholde Movie objekter som er søkbar på movie-ID


    # Filmer
    for line in movies_tsv.splitlines():
        movie_id, movie_title, movie_rating, _ = line.split('\t')
        E[movie_id] = Movie(movie_title, movie_rating)

    # Skuespillere
    for actor in actors_tsv.splitlines():
        actor_id, actor_name, *actor_movies = actor.split('\t')
        V[actor_id] = Actor(actor_name)
        # Legger alle skuespillere til sine filmer.
        # Eksluderer filmer som ikke er i databasen
        for movie in actor_movies:
            if movie in E:
                V[actor_id].add_movie(movie)
                E[movie].add_actor(actor_id)

    return V, E 
def len_V_E(G):
    '''
    Teller noder og kanter
    input: dict for actors og movies
    output: 2 variabler - tallverdiene til node og kanter
    '''
    
    V, E = G

    num_V = len(V)
    num_E = 0

    for movie in E:
        movie_cast = E[movie].get_actors()

        #Vurder ikke filmer som kun har 1 skuespiller
        if len(movie_cast) < 2:
            continue

        #Teller antall kanter    
        num_E += int(len(movie_cast)*(len(movie_cast)-1)/2) # N*(N-1)/2
    
    return num_V, num_E

#Oppgave 1
def oppg1(G):
    num_V, num_E = len_V_E(G) #gjør beregninger av kanter og noder.
    print(f'Nodes:{num_V}')
    print(f'Edges:{num_E}')

#Funksjoner for oppgave 2
def shortest_path_dijkstra(G, start):
    V, E = G
    Q = [(0, start)]
    D = defaultdict(lambda: float('inf'))
    D[start] = 0
    parents = {start : (None, None)}   #node : (foreldrenode, vekt)

    while Q:
        cost, v = heappop(Q)
        for e in V[v].get_movies():
            c = cost + float(E[e].get_rating())
            for u in E[e].get_actors():
                if c < D[u] and v != u:
                    D[u] = c
                    heappush(Q, (c, u))
                    parents[u] = (v, e)
    return parents

def bfs_shortest_path_between(parents, end):
    v = (end, None)
    path = []

    if end not in parents:
        return path

    while v[0]:
        path.append(v)
        v = parents[v[0]]
    return path[::-1]

def pretty_print(G, start, shortest_path, weight = False):
    V, E = G
    w = 0
    print(V[start].get_name())
    
    for i in range(len(shortest_path)-1):
        rating = E[shortest_path[i][1]].get_rating()
        title = E[shortest_path[i][1]].get_title()
        actor = V[shortest_path[i+1][0]].get_name()

        print(f'===[ {title} ({rating}) ] ===> {actor}')
        
        w += (10-float(rating))

    if weight:
        print(f'Total weight: {round(w,1)}')

#Oppgave 2
def oppg2(G):
    start = ['nm2255973', 'nm0424060', 'nm4689420', 'nm0000288', 'nm0031483']
    end = ['nm0000460', 'nm0000243', 'nm0000365', 'nm0001401', 'nm0931324']
    
    for s, e in zip(start,end):
        parents = shortest_path_dijkstra(G, s)
        shortest_path = bfs_shortest_path_between(parents, e)
        pretty_print(G, s, shortest_path)



if __name__ == "__main__":
    #Lager graf for alle oppgavene
    G = make_graph('actors.tsv', 'movies.tsv')

    #oppg1(G)
    oppg2(G)


    print(f'timespent: {round(t.time()-start_time,2)}')


    
    