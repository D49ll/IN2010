import oppg1
import oppg2

def components_and_size(G):
    V, E = G
    size_of_comp = dict()
    key_V = list(V.keys())
    while key_V:
        start_node = key_V[0]
        parents = oppg2.shortest_path_dijkstra(G, start_node)
        if len(parents) in size_of_comp:
            size_of_comp[len(parents)] = size_of_comp[len(parents)] + 1
        else:
            size_of_comp[len(parents)] = 1
        key_V = [x for x in key_V if x not in parents]

    return size_of_comp    

def main():
    f1 = 'actors.tsv'
    f2 = 'movies.tsv'
    G = oppg1.make_graph(f1, f2)
    
    comp_list = components_and_size(G)
    for key, val in reversed(sorted(comp_list.items())):
        print(f'There are {val} components of size {key}')

def solu_func(G):
    comp_list = components_and_size(G)
    for key, val in reversed(sorted(comp_list.items())):
        print(f'There are {val} components of size {key}')


if __name__ == "__main__":
    main()