class Movie:
    '''
    En klasse som initieres med tittel og vurdering av en gitt film.
    Innholder også alle skuespillere til filmen.            
    '''
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating
        self.actors = set()

    def get_title(self):
        return self.title

    def get_rating(self):
        return self.rating   

    def add_actor(self, actor):
        self.actors.add(actor)
    
    def get_actors(self):
        return self.actors

class Actor:
    '''
    sett inn beskrivelse her          
    '''
    def __init__(self, name):
        self.name = name
        self.movies = set()

    def get_name(self):
        return self.name

    def add_movie(self, movie):
        self.movies.add(movie)
    
    def get_movies(self):
        return self.movies