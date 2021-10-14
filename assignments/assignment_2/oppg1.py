from classes import Actor, Movie

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
    actors = dict() #En ordbok som skal inneholder Actor objekter som er søkbar på actor-ID
    movies = dict() #En ordbok som skal innholde Movie objekter som er søkbar på movie-ID


    # Filmer
    for line in movies_tsv.splitlines():
        movie_id, movie_title, movie_rating, _ = line.split('\t')
        movies[movie_id] = Movie(movie_title, movie_rating)

    # Skuespillere
    for actor in actors_tsv.splitlines():
        actor_id, actor_name, *actor_movies = actor.split('\t')
        actors[actor_id] = Actor(actor_name)
        
        # Legger alle skuespillere til sine filmer.
        # Eksluderer filmer som ikke er i databasen
        for movie in actor_movies:
            if movie in movies:
                actors[actor_id].add_movie(movie)
                movies[movie].add_actor(actor_id)

    return actors, movies 

def count_V_E(G):
    '''
    Teller noder og kanter
    input: dict for actors og movies
    output: 2 variabler - tallverdiene til node og kanter
    '''
    actors, movies = G
    num_V = len(actors)
    num_E = 0

    for movie in movies:
        movie_cast = movies[movie].get_actors()

        num_E += int(len(movie_cast)*(len(movie_cast)-1)/2) # N*(N-1)/2
    
    return num_V, num_E

#Oppgave 1
def main():
    f1 = 'actors.tsv'
    f2 = 'movies.tsv'
    G = make_graph(f1, f2) # "lager grafene" og returnerer dict for skuespiller og filmer
    num_a, num_m = count_V_E(G)
    print()
    print(f'Nodes:{num_a}')
    print(f'Edges:{num_m}')

def solu_func():
    f1 = 'actors.tsv'
    f2 = 'movies.tsv'
    G = make_graph(f1, f2) # "lager grafene" og returnerer dict for skuespiller og filmer
    num_a, num_m = count_V_E(G)
    print()
    print(f'Nodes:{num_a}')
    print(f'Edges:{num_m}')
    return G

if __name__ == "__main__":
    main()