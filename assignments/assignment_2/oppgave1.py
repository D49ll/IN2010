from collections import defaultdict

#
#  from os import read


# i = 0
# read_lines = 1000

# for line in open('actors.tsv'):
#     n_id, n ,*tt_id = line.split('\t')
#     i += 1
   
#     if i == read_lines:
#         break

# def actor_filmography(actors_tsv, movies_tsv):
#     nm_ids = list()
#     in_movies = defaultdict(set)
#     tt_ids = defaultdict(list)

#     #Lager et bibliotek av alle filmer listet i movies.tsv
#     for line in movies_tsv.splitlines():
#         tt_id, tt_name, tt_rating, _ = line.split('\t')
        
#         tt_ids[tt_id] = [tt_name, tt_rating]

#     #Oppretter en liste med skuespillere.  med en liste av personens filmografi
#     for line in actors_tsv.splitlines():
#         nm_id, _, *tt_id = line.split('\t')
#         nm_ids.append(nm_id)
#         for m in tt_ids:
#             if m in tt_ids:
#                 in_movies[nm_id].add(m)

#     #Oppretter noder og sjekker 
#     for actor in actors:
#         if in_movies[actor] in 



#     return actors, in_movies

# def actor_filmography(actors_tsv, movies_tsv):
#     actors = list()
#     filmo = defaultdict(list)
#     movies = defaultdict(list)

#     #Lager et bibliotek av alle filmer listet i movies.tsv
#     for line in movies_tsv.splitlines():
#         movie_id, movie_name, movie_rating, _ = line.split('\t')
        
#         movies[movie_id] = [movie_name, movie_rating]

#     #Oppretter en liste med skuespillere.  med en liste av personens filmografi
#     for line in actors_tsv.splitlines():
#         actor_id, actor_name, *actor_movies = line.split('\t')
#         actors.append(actor_id)
#         for movie in actor_movies:
#             if movie in movies:
#                 filmo[actor_id].append(movie)

#     E = defaultdict(set)
#     w = dict()
    
#     #Oppretter noder og sjekker 

#     for i in range(len(actors)):
#         for j in range(len(actors)):
#         if filmo[actors[i]][j] in 


#     for actor1 in actors:
#         #print(f'len={len(actor1)}')
#         for actor2 in actors:
#             #print(f'i={i}')
#             #print(f'actor1: {actor1}')
#             #print(f'actor2: {actor2}')
#             #print(f'filmo[actor1]: {filmo[actor1][i]}')
#             if filmo[actor1][i] in filmo[actor2]:
#                 print('here')
#                 E[actor1].add(actor2) #oppretter en kant mellom disse to
#                 w[(actor1, actor2)] = movies[filmo[actor1][i]]
#             i += 1


#     return actors, E, w



actors_tsv = open('actors2.tsv').read()
movies_tsv = open('movies.tsv').read()

imdb_database = defaultdict(list)
actors = defaultdict(list)

for line in movies_tsv.splitlines():
    movie_id, movie_title, movie_rating, _ = line.split('\t')
    imdb_database[movie_id] = [movie_title, movie_rating]


for line in actors_tsv.splitlines():
    actor_id, actor_name, *actor_movies = line.split('\t')
    acted_in = []
    for movie in actor_movies:
        if movie in imdb_database:
            acted_in.append(movie) 
    actors[actor_id] = [actor_name, acted_in]

for actor in actors.values():
    print(actor[0])    
    
    
