def inverse_weight(graph, weight='weight'):
    copy_graph = graph.copy()
    for n, eds in copy_graph.adjacency():
        for ed, eattr in eds.items():
            copy_graph[n][ed][weight] = eattr[weight] * -1
    return copy_graph

def longest_path_and_length(graph, s, t, weight='weight'):
    i_w_graph = inverse_weight(graph, weight)
    path = nx.dijkstra_path(i_w_graph, s, t)
    length = nx.dijkstra_path_length(i_w_graph, s, t)
    return path, length

def capitals_score(graph, s, t):
    x, score = longest_path_and_length(graph, s, t)
    print('length: ', score)
    count = 0
    for q in x:
        if q in Capitales:
            count += 1
    if count != 0:
        score = score*(2*count)
    print('score: ', score)
    return score

def create_copy(graph):
    new_G = graph.copy()
    return new_G

def create_path(graph, s, t):
    x, score = longest_path_and_length(graph, s, t)
    # print('path: ', x)
    new_G = graph.copy()
    for node in graph.nodes():
         if node not in x:
             new_G.remove_node(node)
    return new_G, x

def path_without_edge(graph, path):
    h = []
    if len(path) >= 4:
        for i in range(len(path)):
            if i <= len(path)-2:
                j = (path[i], path[i+1])
                h.append(j)
        h.pop(0)
        h.pop(-1)
        u, v = h[len(h)//2]
        # print('u: ', u, 'v: ', v)
        graph.remove_edge(u, v)
    elif len(path) == 2:
        j = (path[0], path[1])
        h.append(j)
        u, v = h[0]
        # print('u: ', u, 'v: ', v)
        graph.remove_edge(u,v)
    elif len(path) == 3:
        j = (path[0], path[1])
        h.append(j)
        k = (path[1], path[2])
        h.append(k)
        u, v = h[len(h)//2]
        # print('u: ', u, 'v: ', v)
        graph.remove_edge(u,v)

def convert_edges(path):
    h = []
    for i in range(len(path)):
        if i <= len(path)-2:
            j = (path[i], path[i+1])
            h.append(j)
    return h

def final(l1, l2, l3, l4, l5):
    lf = l1
    lf += l2
    lf += l3
    lf += l4
    lf += l5
    L = []
    for q in lf:
        if q not in L:
            L.append(q)
    return L

def names(path):
    City=[]
    for q in path:
        if q in Cities.keys():
            City.append((q, Cities[q]))
    return City
