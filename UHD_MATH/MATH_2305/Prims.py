

from Weighted_Graph import Weighted_Graph
from functions import c, update




def Prims(edge_list, start_vertex = 0, draw = False, show_cost = False):
    
    G = Weighted_Graph(edge_list)
    T = ({start_vertex}, [])
    
    if draw == True:
        G.draw_graph()
        
    while T[0] != G.vertex_set():
        update(T, G)
        if draw == True:
            G.draw_subgraph(T)
        
    if show_cost == True:
        print(f'The optimal cost: {sum([c(e,G) for e in T[1]])}')

    return T


    
    