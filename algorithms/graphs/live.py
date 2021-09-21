import graphviz

class Vertex:
    def __init__(self, elem):
        self.elem = elem
        self.v_out = set()
        self.v_in = set()

def buildgraph1(line): 
    V = set()
    E = set()

    for line in lines:
        course, *deps = line.strip().split()
        V.add(course)

        for dep in deps:
            E.add((dep, course))

    return V, E

def buildgraph2(line): 
    graph = dict()
    
    # Initierer alle noder
    for line in lines:
        course = line.split()[0]
        graph[course] = Vertex(course)


    for line in lines:
        course, *deps = line.strip().split()
        v = graph[course]
        
        for dep in deps:
            if dep not in graph:
                continue
            w = graph[dep]
            v.v_in.add(w)
            w.v_out.add(w)

    return graph

def topsort(graph):
    V = graph.values()
    stack = []
    result = []

    for v in V:
        if len(v.v_in) == 0:
            stack.append(v)

    while len(stack) > 0:
        v = stack.pop()
        result.append(v.elem)
        for w in v.v_out:
            w.v_in.discard(v) #måte å fjerne noe fra en mengde
            if len(w.v_in) == 0:
                stack.append(w)
    
    return result

with open('graph','r') as f:
    lines = f.readlines()
    graph = buildgraph2(lines)
    print(topsort(graph))

    #G = buildgraph1(lines)
    #V, E = G
    #for edge in E:
    #    print(edge)

#def drawgraph(G):
#    V, E = G
#    dot = graphviz.Digraph()
#    dot.edges(E)
#    dot.render('g')
#drawgraph(graph)

    