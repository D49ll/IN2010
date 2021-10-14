import functions as func

def run(G):
    comp_list = func.components_and_size(G)
    for key, val in reversed(sorted(comp_list.items())):
        print(f'There are {val} components of size {key}')


if __name__ == "__main__":
    f1 = 'actors.tsv'
    f2 = 'movies.tsv'
    G = func.make_graph(f1, f2)
    
    comp_list = func.components_and_size(G)
    for key, val in reversed(sorted(comp_list.items())):
        print(f'There are {val} components of size {key}')
