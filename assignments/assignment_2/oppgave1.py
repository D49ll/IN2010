# from os import read


# i = 0
# read_lines = 1000

# for line in open('actors.tsv'):
#     n_id, n ,*tt_id = line.split('\t')
#     i += 1
   
#     if i == read_lines:
#         break
from collections import defaultdict

def actor_filmography(actors_tsv, movies_tsv):
    actors = list()
    filmography = defaultdict(set)
    library = defaultdict(list)

    #Lager et bibliotek av filmer
    for line in movies_tsv.splitlines():
        tt_id, tt_name, tt_rating, _ = line.split('\t')
        
        library[tt_id] = [tt_name, tt_rating]

    #Oppretter en skuespiller med en liste av personens filmografi
    for line in actors_tsv.splitlines():
        actor,_ ,*movies = line.split('\t')
        actors.append(actor)
        for movie in movies:
            if movie in library:
                filmography[actor].add(movie)

    print(len(actors))
    #Sjekker en skuespillers filmografi mot en annen
    
    for i in range(len(actors)-1):
        for j in range(len(actors)-1):
            if filmography[actors[i]] in filmography[actor[j]] and actors[i] != actors[j]:
                print('hei')


    return actors, filmography

actors_tsv = open('actors2.tsv').read()
movies_tsv = open('movies.tsv').read()

G = actor_filmography(actors_tsv,  movies_tsv)





#print(movies)

