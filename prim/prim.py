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
import csv
import matplotlib.pyplot as plt

def createGraph(A):
    '''
    Function that receives a matrix that is not in the standart form and transform into
    a graph
    '''
    maxval = int(A[len(A)-1][0])
    M = np.zeros((maxval, maxval))

    for i in range(0, len(A)):
        row = int(A[i][0])
        column = int(A[i][1])
        value = A[i][2]
        M[row-1][column-1] = value

    return M

def minDistance(dist, mstSet, V):
    '''
    Function that return the minimum edge weight node
    '''
    min = sys.maxsize 
    for v in range(V):
        if mstSet[v] == False and dist[v] < min:
            min = dist[v]
            min_index = v

    return min_index

def plotGraph(G):
    '''
    Function that receives a graph G and draws it
    '''
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels = True)
    edge_labels = nx.get_edge_attributes(G,'length')
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 11) #prints weight on all the edges
    
    return pos

def prim(G, start):
    '''
    Function that receives a graph and a starting node, and returns a minimal spanning tree
    '''
    V = G.number_of_nodes() - 1
    dist = []
    parent = [None]*V
    mst_set = []

    for i in range(V):
        dist.append(sys.maxsize)
        mst_set.append(False)

    dist[0] = 0
    parent[0] = -1

    for count in range(V-1):
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
                nx.draw_networkx_edges(G, pos, edgelist = [(parent[X], X)], width = 2.5, alpha = 0.6, edge_color = 'r')
    
if __name__ == "__main__":
    A = np.loadtxt(sys.argv[1])
    try:
        G = nx.from_numpy_matrix(A)
    except:
        A = createGraph(A)
        G = nx.from_numpy_matrix(A)

    pos = plotGraph(G)
    prim(G, pos)
    
    plt.show()