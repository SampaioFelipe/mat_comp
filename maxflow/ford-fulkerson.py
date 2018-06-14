#!/usr/bin/env python3
import networkx as nx
import math

class Grafo(object):

    def __init__(self, C):
        self.edges = []

        for i, linha in enumerate(C):
            u = []
            for j, valor in enumerate(linha):
                u.append({'fe': valor, 'be': 0})
            self.edges.append(u)

        self.nodes = [{'predecessor': None} for x in C]

        self.src = 0
        self.terminal = len(self.nodes) - 1


    def getPath(self):
        path = []
        u = self.terminal
        parent = self.nodes[u]['predecessor']
        path.append((parent, u))

        while parent:
            u = parent
            parent = self.nodes[u]['predecessor']
            path.append((parent, u))

        return path

    def findPath(self):
        stack = [self.src]
        visitados = [self.src]

        while stack:

            u = stack.pop()

            for i, edge in enumerate(self.edges[u]):
                if edge['fe'] + edge['be'] != 0:
                    if i not in visitados:
                        visitados.append(i)
                        stack.append(i)

                        self.nodes[i]['predecessor'] = u

                        if(i == self.terminal):
                            print('findpath', self.nodes)
                            return self.getPath()
        return []

capacidades = [[0, 16, 13, 0, 0, 0],
      [0, 0, 10, 12, 0, 0],
      [0, 4, 0, 0, 14, 0],
      [0, 0, 9, 0, 0, 20],
      [0, 0, 0, 7, 0, 4],
      [0, 0, 0, 0, 0, 0]]


def augment(G, P):
    gargalo = math.inf

    print(P)

    for u,v in P:
        fe = G.edges[u][v]['fe']
        be = G.edges[u][v]['be']
        fluxo = fe if fe > be else be
        if fluxo < gargalo:
            gargalo = fluxo

    for u,v in P:
        fe = G.edges[u][v]['fe']
        be = G.edges[u][v]['be']
        print(G.edges[u][v])

        if fe > be:
            G.edges[u][v]['fe'] = G.edges[u][v]['fe'] - gargalo
            G.edges[v][u]['be'] = G.edges[v][u]['be'] + gargalo
        else:
            G.edges[u][v]['be'] = G.edges[u][v]['be'] - gargalo
            G.edges[v][u]['fe'] = G.edges[v][u]['fe'] + gargalo

        print(G.edges[u][v])
        print('=====')

    return gargalo

def maxflow(G):
    f = 0

    Pst = G.findPath()

    while Pst:
        f = f + augment(G, Pst)
        Pst = G.findPath()

    flow = {}

    for i in range(len(G.edges)):
        flow[i] = {}
        for j in range(len(G.edges)):
            if(G.edges[j][i]['be'] > 0):
                flow[i][j] = G.edges[j][i]['be']

    return (f, flow)

G = Grafo(capacidades)

print(maxflow(G))

for l in G.edges:
    print(l)

G = nx.DiGraph()

for i, linha in enumerate(capacidades):
    for j, val in enumerate(linha):
        if val > 0:
            G.add_edge(i,j, capacity=val)

a = nx.maximum_flow(G, 0, 5)

print(a)
