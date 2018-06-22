'''
    Prim's Algorithm
    Alunos:
        @author Felipe Sampaio
        @author Romão Martines
        @author Sylviane Vitor
    Referencias:
        https://github.com/abcsds/Prim/blob/master/prim.py
            [acesso em 17 de junho de 2018]
        https://github.com/MUSoC/Visualization-of-popular-algorithms-in-Python/blob/master/Prim's/prims.py
            [acesso em 17 de junho de 2018]
'''
import numpy as np
import networkx as nx
import sys
import math
import matplotlib.pyplot as plt

def minDistance(dist, mstSet, V):
    '''
    Function that return the minimum edge weight node
    '''
    minimum = math.inf 
    min_index = None
    for v in range(V):
        if (mstSet[v] == False) and (dist[v] < minimum):
            minimum = dist[v]
            min_index = v

    return min_index

def plotGraph(G):
    '''
    Function that receives a graph G and draws it
    '''
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels = True)
    edge_labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 11) # prints weight on all the edges
    
    return pos

def prim(G, start):
    '''
    Function that receives a graph and a starting node, and returns a minimal spanning tree
    '''
    V = G.number_of_nodes()
    dist = []
    parent = [None] * V
    mst_set = []

    for i in range(V):
        dist.append(math.inf)
        mst_set.append(False)

    dist[0] = 0
    parent[0] = -1

    for count in range(0, V):
        u = minDistance(dist, mst_set, V)
        mst_set[u] = True

        for v in range(V):
            if (u, v) in G.edges():
                if (mst_set[v] == False) and (G[u][v]['weight'] < dist[v]):
                    dist[v] = G[u][v]['weight']
                    parent[v] = u   

    for X in range(V):
        if parent[X] != -1:
            if (parent[X], X) in G.edges():
                nx.draw_networkx_edges(G, pos, edgelist = [(parent[X], X)], width = 2.5, alpha = 0.6, edge_color = '#00FF00')
    
if __name__ == "__main__":
    A = np.loadtxt(sys.argv[1])

    try:
        G = nx.from_numpy_matrix(A)
    except:
        G = nx.read_weighted_edgelist(sys.argv[1])
        G = nx.convert_node_labels_to_integers(G)

    print (G)

    pos = plotGraph(G)
    prim(G, pos)
    
    plt.show()