import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
#Nodos del grafo
G.add_node('1', pos = (57,390))
G.add_node('2', pos = (97,434))
G.add_node('3', pos = (72,553))
G.add_node('4', pos = (198,505))
G.add_node('5', pos = (140,473))
G.add_node('6', pos = (203,400))
G.add_node('7', pos = (269,391))
G.add_node('8', pos = (345,391))
G.add_node('9', pos = (327,308))
G.add_node('10', pos = (243,322))
G.add_node('11', pos = (218,251))
G.add_node('12', pos = (267,122))
G.add_node('13', pos = (385,172))
G.add_node('14', pos = (371,230))
G.add_node('15', pos = (457,225))
G.add_node('16', pos = (459,265))
G.add_node('17', pos = (414,325))
G.add_node('18', pos = (472,368))
G.add_node('19', pos = (495,450))
G.add_node('20', pos = (568,573))
G.add_node('21', pos = (578,498))
G.add_node('22', pos = (714,527))
G.add_node('23', pos = (722,431))
G.add_node('24', pos = (603,425))
G.add_node('25', pos = (568,364))
G.add_node('26', pos = (526,312))
G.add_node('27', pos = (518,185))
G.add_node('28', pos = (452,154))
G.add_node('29', pos = (603,140))
G.add_node('30', pos = (663,191))
G.add_node('31', pos = (650,305))
G.add_node('32', pos = (790,354))


#Aristas del grafo
G.add_edge('1', '2', weight=3)
G.add_edge('1', '3', weight=3)
G.add_edge('1', '6', weight=3)
G.add_edge('2', '3', weight=3)
G.add_edge('2', '6', weight=3)
G.add_edge('2', '5', weight=3)
G.add_edge('3', '4', weight=3)
G.add_edge('3', '5', weight=3)
G.add_edge('4', '6', weight=4)
G.add_edge('4', '8', weight=4)
G.add_edge('4', '5', weight=4)
G.add_edge('4', '7', weight=4)
G.add_edge('5', '6', weight=4)
G.add_edge('6', '7', weight=4)
G.add_edge('6', '9', weight=4)
G.add_edge('6', '10', weight=4)
G.add_edge('7', '8', weight=5)
G.add_edge('8', '9', weight=5)
G.add_edge('8', '17', weight=5)
G.add_edge('8', '19', weight=5)
G.add_edge('9', '10', weight=2)
G.add_edge('9', '11', weight=2)
G.add_edge('9', '14', weight=2)
G.add_edge('9', '15', weight=2)
G.add_edge('9', '7', weight=2)
G.add_edge('9', '17', weight=3)
G.add_edge('10', '11', weight=6)
G.add_edge('11', '12', weight=2)
G.add_edge('11', '14', weight=2)
G.add_edge('12', '13', weight=2)
G.add_edge('13', '14', weight=1)
G.add_edge('13', '15', weight=1)
G.add_edge('13', '28', weight=1)
G.add_edge('14', '15', weight=2)
G.add_edge('15', '16', weight=5)
G.add_edge('15', '27', weight=5)
G.add_edge('15', '28', weight=5)
G.add_edge('16', '17', weight=3)
G.add_edge('16', '18', weight=6)
G.add_edge('16', '26', weight=6)
G.add_edge('17', '18', weight=3)
G.add_edge('18', '19', weight=2)
G.add_edge('18', '25', weight=2)
G.add_edge('19', '20', weight=4)
G.add_edge('19', '21', weight=4)
G.add_edge('20', '21', weight=3)
G.add_edge('21', '22', weight=4)
G.add_edge('22', '23', weight=3)
G.add_edge('22', '24', weight=3)
G.add_edge('22', '32', weight=4)
G.add_edge('23', '24', weight=2)
G.add_edge('23', '32', weight=4)
G.add_edge('24', '25', weight=4)
G.add_edge('24', '31', weight=4)
G.add_edge('24', '32', weight=4)
G.add_edge('25', '26', weight=3)
G.add_edge('25', '31', weight=3)
G.add_edge('26', '27', weight=4)
G.add_edge('26', '30', weight=4)
G.add_edge('26', '31', weight=5)
G.add_edge('27', '28', weight=6)
G.add_edge('27', '29', weight=6)
G.add_edge('27', '30', weight=6)
G.add_edge('29', '30', weight=7)
G.add_edge('30', '31', weight=5)
G.add_edge('31', '32', weight=5)


Capitales = ['1', '2', '9', '12', '13', '14', '19', '22', '23', '24', '25',
             '31', '26', '27', '30', '32']

Cities = {'1':'Lisboa', '2':'Madrid', '3':'Cadiz', '4':'Barcelona', '5':'Valencia',
        '6':'Pamplona', '7':'Lyon', '8':'Marsella', '9':'Paris', '10':'Brest',
        '11':'Dieppe', '12':'Londres', '13':'Amsterdam', '14':'Bruselas',
        '15':'Francfort', '16':'Munich', '17':'Zurich', '18':'Venecia',
        '19':'Roma', '20':'Palermo', '21':'Brindisi', '22':'Atenas',
        '23':'Sofia', '24':'Sarajevo', '25':'Zagreb', '26':'Viena', '27':'Berlin',
        '28':'Essen', '29':'Danzing', '30':'Varsovia', '31':'Budapest', '32':'Bucarest'}

#Funciones a usar
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

# Inicia la ejecucion
print("Nodo de Salida")
Salida = input()
print("Nodo de Llegada")
Llegada = input()


if Salida > Llegada:
    x = Salida
    Salida = Llegada
    Llegada = x

    print()
    print("Tren 1")
    Gra1 = create_copy(G)
    D1, P1 = create_path(Gra1, Salida, Llegada)
    inv_P1 = P1[::-1]
    A1 = names(inv_P1)
    print('path: ', A1)
    S1 = capitals_score(Gra1, Salida, Llegada)
    L1 = convert_edges(P1)
    N1 = path_without_edge(Gra1, P1)

    print()
    print("Tren 2")
    Gra2 = create_copy(Gra1)
    D2, P2 = create_path(Gra2, Salida, Llegada)
    inv_P2 = P2[::-1]
    A2 = names(inv_P2)
    print('path: ', A2)
    S2 = capitals_score(Gra2, Salida, Llegada)
    L2 = convert_edges(P2)
    N2 = path_without_edge(Gra2, P2)

    print()
    print("Tren 3")
    Gra3 = create_copy(Gra2)
    D3, P3 = create_path(Gra3, Salida, Llegada)
    inv_P3 = P3[::-1]
    A3 = names(inv_P3)
    print('path: ', A3)
    S3 = capitals_score(Gra3, Salida, Llegada)
    L3 = convert_edges(P3)
    N3 = path_without_edge(Gra3, P3)

    print()
    print("Tren 4")
    Gra4 = create_copy(Gra3)
    D4, P4 = create_path(Gra4, Salida, Llegada)
    inv_P4 = P4[::-1]
    A4 = names(inv_P4)
    print('path: ', A4)
    S4 = capitals_score(Gra4, Salida, Llegada)
    L4 = convert_edges(P4)
    N4 = path_without_edge(Gra4, P4)

    print()
    print("Tren 5")
    Gra5 = create_copy(Gra4)
    D5, P5 = create_path(Gra5, Salida, Llegada)
    inv_P5 = P5[::-1]
    A5 = names(inv_P5)
    print('path: ', A5)
    S5 = capitals_score(Gra5, Salida, Llegada)
    L5 = convert_edges(P5)
    N5 = path_without_edge(Gra5, P5)

    new_G = create_copy(G)
    for u,v in G.edges():
        j = u,v
        k = v,u
        if j not in L3:
            if k not in L3:
                new_G.remove_edge(u,v)

    for node in G.nodes():
         if node not in P3:
             new_G.remove_node(node)

else:
    print()
    print("Tren 1")
    Gra1 = create_copy(G)
    D1, P1 = create_path(Gra1, Salida, Llegada)
    A1 = names(P1)
    print('path: ', A1)
    S1 = capitals_score(Gra1, Salida, Llegada)
    L1 = convert_edges(P1)
    N1 = path_without_edge(Gra1, P1)

    print()
    print("Tren 2")
    Gra2 = create_copy(Gra1)
    D2, P2 = create_path(Gra2, Salida, Llegada)
    A2 = names(P2)
    print('path: ', A2)
    S2 = capitals_score(Gra2, Salida, Llegada)
    L2 = convert_edges(P2)
    N2 = path_without_edge(Gra2, P2)

    print()
    print("Tren 3")
    Gra3 = create_copy(Gra2)
    D3, P3 = create_path(Gra3, Salida, Llegada)
    A3 = names(P3)
    print('path: ', A3)
    S3 = capitals_score(Gra3, Salida, Llegada)
    L3 = convert_edges(P3)
    N3 = path_without_edge(Gra3, P3)

    print()
    print("Tren 4")
    Gra4 = create_copy(Gra3)
    D4, P4 = create_path(Gra4, Salida, Llegada)
    A4 = names(P4)
    print('path: ', A4)
    S4 = capitals_score(Gra4, Salida, Llegada)
    L4 = convert_edges(P4)
    N4 = path_without_edge(Gra4, P4)

    print()
    print("Tren 5")
    Gra5 = create_copy(Gra4)
    D5, P5 = create_path(Gra5, Salida, Llegada)
    A5 = names(P5)
    print('path: ', A5)
    S5 = capitals_score(Gra5, Salida, Llegada)
    L5 = convert_edges(P5)
    N5 = path_without_edge(Gra5, P5)


    new_G = create_copy(G)
    for u,v in G.edges():
        j = u,v
        k = v,u
        if j not in L3:
            if k not in L3:
                new_G.remove_edge(u,v)

    for node in G.nodes():
         if node not in P3:
             new_G.remove_node(node)


color_map = []
for node in new_G:
    if node in Capitales:
        color_map.append('purple')
    else:
        color_map.append('green')

pos = nx.get_node_attributes(new_G, 'pos')
labels = nx.get_edge_attributes(new_G, 'weight')

nx.draw(new_G, pos, with_labels=True, node_size = 100, font_size = 6,
        node_color = color_map, font_color = 'white', edgelist = L3)

nx.draw_networkx_edge_labels(new_G, pos, alpha = 0.9, edge_labels = labels, font_size = 7,
                             bbox = dict(facecolor='lightblue', edgecolor='none', pad=0.5))

imData = plt.imread("mapa.png")
plt.imshow(imData)

plt.show()
