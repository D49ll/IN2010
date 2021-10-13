from collections import defaultdict, deque
import graphviz


def buildgraph(lines):
    V = set()
    E = defaultdict(set)
    w = dict()

    for line in lines.splitlines():
        v, u, weight = line.strip().split()

        V.add(v)
        V.add(u)

        E[v].add(u)
        E[u].add(v)

        w[(v, u)] = int(weight)
        w[(u, v)] = int(weight)

    return V, E, w

def draw_parents(parents):
    dot = graphviz.Graph()
    for v in parents:
        u = parents[v]
        if u: dot.edge(v, u)
    dot.render('bfs_spanningtree', format='jpg')

def drawgraph(G):
    V, E, w = G
    dot = graphviz.Graph()
    seen_edges = set()

    for v in V:
        dot.node(v)

        for u in E[v]:
            if (u, v) in seen_edges:
                continue
            seen_edges.add((v, u))
            dot.edge(v, u, label=str(w[(v, u)]))

    dot.render('graph', format='jpg')

def bfs(G, s):
    _, E, _ = G
    visited = set([s])
    queue = deque([s])
    result = []

    while queue:
        v = deque.popleft(queue)
        result.append(v)
        for u in E[v]:
            if u not in visited:
                visited.add(u)
                queue.append(u)
    return result

def bfs_shortest_paths_from(G, s):
    _, E, _ = G
    parents = {s : None}
    queue = deque([s])

    while queue:
        v = deque.popleft(queue)
        for u in E[v]:
            if u not in parents:
                parents[u] = v
                queue.append(u)
    return parents

def bfs_shortest_path_between(G, s, t):
    parents = bfs_shortest_paths_from(G, s)
    v = t
    path = []

    if t not in parents:
        return path

    while v:
        path.append(v)
        v = parents[v]
    return path[::-1]


f1 = open('graf.txt').read()

G = buildgraph(f1)
parents = bfs_shortest_paths_from(G,'A')
print(parents)
drawgraph(G)
draw_parents(bfs_shortest_paths_from(G,'A'))
bfs_shortest_path_between(G, 'A', 'G')