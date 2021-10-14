import functions as func

def run():
    f1 = 'actors.tsv'
    f2 = 'movies.tsv'
    G = func.make_graph(f1, f2) # "lager grafene" og returnerer dict for skuespiller og filmer
    num_a, num_m = func.count_V_E(G)
    print()
    print(f'Nodes:{num_a}')
    print(f'Edges:{num_m}')
    return G

if __name__ == "__main__":
    f1 = 'actors.tsv'
    f2 = 'movies.tsv'
    G = func.make_graph(f1, f2) # "lager grafene" og returnerer dict for skuespiller og filmer
    num_a, num_m = func.count_V_E(G)
    print()
    print(f'Nodes:{num_a}')
    print(f'Edges:{num_m}')
