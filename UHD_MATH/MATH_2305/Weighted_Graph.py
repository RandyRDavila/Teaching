#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 16:42:36 2018

@author: randydavila
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 20:36:37 2017

Author: Randy R. Davila
Course: MATH 2305 - Discrete Mathematical Structures

In this python script we define a simple and weighted graph class object. This
object should be used to write Prim's and Kruskal's algorithms.
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Weighted_Graph(object):

    def __init__(self, edge_list_file):
       """ Set the edge list directory address """
       self.edge_list_file = edge_list_file



    def edge_dict(self):
        """ Reads in the edge list from the provided directory address and
            creates a edge dictionary where the keys are the edges and values
            are the corresponding edge weights. In particular, to access the
            value of edge (a,b), simply type edge_dict[(a,b)]"""
        edge_dict = dict()                                 # dict()=empty dictionary
        edge_list = np.loadtxt(self.edge_list_file, int)   # numpy 2-d array
        for row in edge_list:
            edge_dict[(row[0], row[1])] = row[2]           # Assign keys and values
        return edge_dict


    def edge_set(self):
        """ Returns the set of edges """
        return set(self.edge_dict().keys())


    def vertex_set(self):
        """ Returns the set of vertices """
        vertex_set = set()                                 # set()= the empty set
        for e in self.edge_set():
            for v in e:
                vertex_set.add(v)
        return vertex_set


    def draw_graph(self):
        """ This function is used to visualize your weighted graph. The functions
            used inside are from the networkx library. """

        G = nx.read_edgelist(self.edge_list_file, nodetype=int, data=(('weight',float),))
        e=[(u,v) for (u,v,d) in G.edges(data=True)]
        pos=nx.spring_layout(G) # positions for all nodes
        nx.draw_networkx_nodes(G,pos,node_size=250) # nodes
        nx.draw_networkx_edges(G,pos,edgelist=e,width=1) # edges

        # labels
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        plt.axis('off')
        plt.show()

    def draw_subgraph(self, H):
        """ This function is used to visualize your weighted graph. The functions
            used inside are from the networkx library. """

        G = nx.read_edgelist(self.edge_list_file, nodetype=int, data=(('weight',float),))
        e1=[(u,v) for (u,v,d) in G.edges(data=True)]
        e2= [e for e in e1 if e in H[1]]
        v1 =[v for v in H[0]]
        pos=nx.spring_layout(G) # positions for all nodes
        nx.draw_networkx_nodes(G,pos,node_size=250) # nodes
        nx.draw_networkx_nodes(G,pos, nodelist = v1,node_size=400)
        nx.draw_networkx_edges(G,pos,edgelist=e1,width=1) # edges
        nx.draw_networkx_edges(G,pos,edgelist=e2, edgecolor = 'red' ,width=5)

        # labels
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        plt.axis('off')
        plt.show()