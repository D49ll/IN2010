class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating
    
class Actor:
    def __init__(self, id,  name, movies):
        self.name = name
        self.movies = movies
        self.id = id
    
    def get_name(self):
        print(self.name)

    def get_movies(self):
        print(self.movies)

    def __eq__(self,other):
        print(set(self.movies) & set(other.movies))




actors_tsv = open('actors.tsv').read()
movies_tsv = open('movies.tsv').read()

imdb_database = dict()
actors = list()

#IMDB movie database
for line in movies_tsv.splitlines():
    movie_id, movie_title, movie_rating, _ = line.split('\t')
    imdb_database[movie_id] = Movie(movie_title, movie_rating)

#Actors
for actor in actors_tsv.splitlines():
    id, name, *movies = actor.split('\t')
    filmography = []
    for movie in movies:
        if movie in imdb_database:
            filmography.append(movie) 
    
    #actors[id] = [name, filmography]
    # print(name)
    actors.append(Actor(id, name, movies))

print(len(actors))

# for i in range(len(actors)):
#     actors[i].get_name()



# for movie in imdb_database:
#     actors_in_movie = []

#     for actor in actors:
#         if movie in actors[actor][1]:
#             actors_in_movie.append(actor)


