#!/usr/bin/env python3
import networkx as nx
import math

class Grafo(object):
    def __init__(self, C):
        self.edges = []
        # Monta o grafo especificando os valores forward(fe) e backward(be) para cada aresta
        for linha in C:
            u = []
            for valor in linha:
                u.append({'fe': valor, 'be': 0})
            self.edges.append(u)

        self.nodes = [{'predecessor': None} for x in C]

        self.src = 0
        self.terminal = len(self.nodes) - 1

    # Retorna lista das arestas que formam o camninho entre src e terminal 
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

    # Busca em profundidade para achar Pst
    # Retorna o caminho achado
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
                        # Encontrou o terminal, está pronto para retornar o caminho 
                        if(i == self.terminal):
                            return self.getPath()
        return [] # se não encontrar nenhum caminho Pst retorna lista vazia

# Encontra o gargalo do caminho e ajusta o fluxo
def augment(G, P):
    print("\nAugment")
    gargalo = math.inf
    
    for u,v in P:
        fe = G.edges[u][v]['fe']
        be = G.edges[u][v]['be']

        fluxo = fe if fe > be else be # escolhe a aresta com o maior capacidade disponível para se passar

        if fluxo < gargalo:
            gargalo = fluxo

    print("Gargalo: {}".format(gargalo))

    for u,v in P:
        fe = G.edges[u][v]['fe']
        be = G.edges[u][v]['be']

        fluxo_anterior = "({}, {})".format(u,v) + str(G.edges[u][v])

        if fe > be: # escolhe a aresta com o maior capacidade disponível para se passar
            G.edges[u][v]['fe'] = G.edges[u][v]['fe'] - gargalo
            G.edges[v][u]['be'] = G.edges[v][u]['be'] + gargalo
        else:
            G.edges[u][v]['be'] = G.edges[u][v]['be'] - gargalo
            G.edges[v][u]['fe'] = G.edges[v][u]['fe'] + gargalo

        print(fluxo_anterior + " -> " + str(G.edges[u][v]))

    return gargalo

def maxflow(G):
    f = 0
    iteracao = 0

    Pst = G.findPath()

    while Pst:
        print("Iteração {}\n".format(iteracao))
        print("Pst: " + str(Pst))
        f = f + augment(G, Pst)
        print("\nFlow: " + str(f))
        print('===============================')
        Pst = G.findPath()
        iteracao = iteracao + 1

    flow = {}

    for i in range(len(G.edges)):
        flow[i] = {}
        for j in range(len(G.edges)):
            if(G.edges[j][i]['be'] > 0):
                flow[i][j] = G.edges[j][i]['be']

    return (f, flow)

if __name__ == "__main__":
    capacidades = [[0, 16, 13, 0, 0, 0],
                   [0, 0, 10, 12, 0, 0],
                   [0, 4, 0, 0, 14, 0],
                   [0, 0, 9, 0, 0, 20],
                   [0, 0, 0, 7, 0, 4],
                   [0, 0, 0, 0, 0, 0]]

    # Cria o grafo a partir da matriz de capacidades
    G = Grafo(capacidades)

    print(maxflow(G))

    print("\nMaxflow do networx (para comparação)")
    # Teste do mesmo grafo com o algoritmo do networkx para comparar os resultados
    G = nx.DiGraph()
    for i, linha in enumerate(capacidades):
        for j, val in enumerate(linha):
            if val > 0:
                G.add_edge(i,j, capacity=val)

    a = nx.maximum_flow(G, 0, 5)

    print(a)
