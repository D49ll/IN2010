import time

from collections import defaultdict
from heapq import heappush, heappop

start_time = time.time()

class Movie:
    '''
    En klasse som initieres med tittel og vurdering av en gitt film.
    Innholder også alle skuespillere til filmen.            
    '''
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating
        self.actors = set()

    def add_actor(self, actor):
        self.actors.add(actor)

    def get_actor_names(self, actors_names):
        names = list()
        
        for actor in self.actors:
            names.append(actors_names[actor][0])

        return names

    def get_actors(self):
        return self.actors
    
    def get_title(self):
        return self.title

    def get_rating(self):
        return self.rating

# class Actor:
#     '''
#     sett inn beskrivelse her          
#     '''
#     def __init__(self, name):
#         self.name = name
#         self.movies = set()

#     def get_name(self):
#         return self.name

#     def add_movie(self, movie):
#         self.movies.add(movie)
    
#     def get_movies(self):
#         return self.movies        

def build_graph(actors_tsv,movies_tsv):
    # Variabler
    movies = dict() #En ordbok som skal innholde Movie objekter
    actors = dict() #En ordbok som inneholder alle skuespiller navn

    # Filmer
    for line in movies_tsv.splitlines():
        movie_id, movie_title, movie_rating, _ = line.split('\t')
        movies[movie_id] = Movie(movie_title, movie_rating)

    # Skuespillere
    for actor in actors_tsv.splitlines():
        actor_id, actor_name, *actor_movies = actor.split('\t')

        movie_in_database = list()
        # Legger alle skuespillere til sine filmer.
        # Eksluderer filmer som ikke er i databasen
        for movie in actor_movies:
            if movie in movies:
                movies[movie].add_actor(actor_id)
                movie_in_database.append(movie)

        actors[actor_id] = actor_name, movie_in_database

    return actors, movies

def print_graph(G):
    '''
    Printer antall noder og kanter i grafen.
    '''
    V, E = G
    print(f'Nodes:{len(V)}')

    edges = 0
    for movie in E:
        num_actors = len(E[movie].get_actors())

        #Vurder ikke filmer som kun har 1 skuespiller
        if num_actors < 2:
            continue

        #Teller antall kanter    
        edges += int(num_actors*(num_actors-1)/2) # N*(N-1)/2
    print(f'Edges:{edges}')

def is_end(movie_id, movies, end):
    m = movies[movie_id]

    if end in m.get_actors():
        print(m.get_title())
        return True
    
    return False



def main():
    # Åpner og leser filer
    actors_tsv = open('actors.tsv').read()
    movies_tsv = open('movies.tsv').read()

    G = build_graph(actors_tsv, movies_tsv)

    # Oppgave 1
    print_graph(G)

    # Oppgave 2

    start='nm2255973'
    end='nm0000460'
    actors, movies = G
    found = False
    

    for movie_id in actors[start][1]:
        print(movie_id)
        
        found = is_end(movie_id,movies,end)
        if found:
            break
        
    


    


main()
print(f'time: {time.time()-start_time}')
