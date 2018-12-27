

def c(e, G):
    return G.edge_dict()[e]


def incident_edges(T, G):
    edges = []
    for v in T[0]:
        for e in G.edge_set():
            if v in e:
                edges.append(e)
    return [e for e in edges if set(e).issubset(T[0]) == False]


def min_incident_edge(T, G):
    edges = incident_edges(T, G)
    min_e = edges[0]
    for e in edges:
        if c(e, G) < c(min_e, G):
            min_e = e
    return min_e

def update(T, G):
    e = min_incident_edge(T, G)
    T[0].add(e[0])
    T[0].add(e[1])
    T[1].append(e)
    
    return None 
