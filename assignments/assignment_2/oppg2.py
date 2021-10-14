import functions as func

def run(G):
    start_list = ['nm2255973', 'nm0424060', 'nm4689420', 'nm0000288', 'nm0031483']
    end_list = ['nm0000460', 'nm0000243', 'nm0000365', 'nm0001401', 'nm0931324']
    
    for start, end in zip(start_list, end_list):
        span_tree = func.bfs_shortest_path_from_to(G,start,end)

        #span_tree = shortest_path_dijkstra(G, start)
        shortest_path = func.bfs_shortest_path_between(span_tree, end)
        func.pretty_print(G, start, shortest_path)

if __name__ == '__main__':
    f1 = 'actors.tsv'
    f2 = 'movies.tsv'
    G = func.make_graph(f1, f2)
    V, E = G
    start_list = ['nm2255973', 'nm0424060', 'nm4689420', 'nm0000288', 'nm0031483']
    end_list = ['nm0000460', 'nm0000243', 'nm0000365', 'nm0001401', 'nm0931324']
    
    for start, end in zip(start_list, end_list):
        span_tree = func.bfs_shortest_path_from_to(G,start,end)
        
        shortest_path = func.bfs_shortest_path_between(span_tree, end)
        func.pretty_print(G, start, shortest_path)
