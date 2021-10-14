from heapq import heappush, heappop
from collections import defaultdict, deque
from classes import Movie, Actor


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

def shortest_path_dijkstra_best_rating(G, start, end=None):
    '''
    Tar inn:
        G - Graf: Tuple av dict: skuespiller og film
        start - Start_node: string: skuespiller-id
    Returnerer:
        parents_path - dict
            key: node_id
            value: tuple(foreldre node_id, høyeste kant)
    '''    
    V, E = G #Finner alle kanter og noder
    Q = [(0, 0, start)] #Første steg koster ingenting, legger dette i køen
    D = defaultdict(lambda: (float('inf'), float('inf'))) #Oppretter en defaultdict D for (Antall steg, rating). D blir initiert med steg = inf og rating = 0
    
    D[start] = (0,0) #Oppdaterer steg for å stå i start

    parents_path = {start : (None, None)} #Første steg
    final_step = float('inf')

    while Q:
        #Henter fra kø
        step, rating, v = heappop(Q)
        
        step += 1
        if final_step < step:
            return parents_path

        #For alle kanter tilhørende noden v
        for e in V[v].get_movies():
            current_movie_rating = (10-float(E[e].get_rating()))
            tot_rating = rating + current_movie_rating
            #oppdaterer kosten til aktuell kant, NB! den inverse verdien.
            
            #Sjekker alle noder aktuell kant leder til
            for u in E[e].get_actors():
                if end == u:
                    final_step = step
                #Finner den kanten med minst kost
                if step <= D[u][0] and tot_rating <= D[u][1] and v != u:
                    D[u] = (step, tot_rating)
                    heappush(Q, (step, tot_rating, u))
                    parents_path[u] = (v, e)
 
                
    return parents_path

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

def components_and_size(G):
    V, E = G
    size_of_comp = dict()
    key_V = list(V.keys())
    while key_V:
        start_node = key_V[0]
        parents = bfs_shortest_path_from_to(G, start_node)
        if len(parents) in size_of_comp:
            size_of_comp[len(parents)] = size_of_comp[len(parents)] + 1
        else:
            size_of_comp[len(parents)] = 1
        key_V = [x for x in key_V if x not in parents]

    return size_of_comp    
