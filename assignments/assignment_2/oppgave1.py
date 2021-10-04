from collections import defaultdict

actors_tsv = open('actors2.tsv').read()
movies_tsv = open('movies.tsv').read()

imdb_database = dict()
actors = dict()

#IMDB movie database
for line in movies_tsv.splitlines():
    movie_id, movie_title, movie_rating, _ = line.split('\t')
    imdb_database[movie_id] = [movie_title, movie_rating]

#Actors
for actor in actors_tsv.splitlines():
    id, name, *movies = line.split('\t')
    filmography = []
    for movie in movies:
        if movie in imdb_database:
            filmography.append(movie) 
    actors[id] = [name, filmography]

E = defaultdict(set)
w = dict()





# #Edges and weights
# for actor_info1 in actors.values():
#     print(actor_info1[0])

#     for movie_id in actor_info1[1]:
#         print(imdb_database[movie_id])
#         for actor_info2 in actors.values():
#             #print(actor_info2[0])
#             if actor_info1[0] == actor_info2[0]:
#                 continue
#             elif movie_id in actor_info2[1]:
#                 E[actor_info1[0]].add(actor_info2[0])
                


# #Nodes and Edges
# print(f'Nodes: {len(actors)}')
# sum = 0
# for actor in actors.values():
#     sum+=len(E[actor[0]])

# print(f'Edges:{sum}')
        


    
    
