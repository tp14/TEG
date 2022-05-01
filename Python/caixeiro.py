import math
from itertools import permutations
import time

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.explored = False
        self.d = math.inf
        self.p = node 

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
    
    def getAdjacent(self):
        return self.adjacent

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def getNumVertex(self):
        return self.num_vertices

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def getAdjacente(self, v1, v2):
        if (v1 == v2):
            return 0
        for v in self:
            for w in v.get_connections():
                if (v.id == v1 and w.id == v2):
                    return(v.get_weight(w))
    
    def caixeiro(self):
        num = self.getNumVertex()
        s = 0
        #cria a matriz de distanciais
        dist = [[" "]*self.getNumVertex() for _ in range(self.getNumVertex())]
        #preenche a matriz de distanciais
        for i, w in enumerate(self):
            for j, v in enumerate(self):
                if (self.getAdjacente(w.id, v.id) != None):
                    dist[i][j] = self.getAdjacente(w.id, v.id)
                else:
                    dist[i][j] = math.inf

        #armazena todos os vertices menos o inicial
        vertices = list()
        for i in range(num):
            if i != s:
                vertices.append(i)

        #armazena o menor caminho
        caminho = math.inf
        proximasCidades = permutations(vertices)
        for i in proximasCidades:
            #armazena caminho atual
            caminhoAtual = 0
            #calcular o valor dos caminhos
            k = s
            for j in i:
                caminhoAtual += dist[k][j]
                k = j
            caminhoAtual += dist[k][s]
            #calcula o minimo
            caminho = min(caminho, caminhoAtual)

        return caminho

if __name__ == '__main__':

    iniH = time.time()
    h = Graph()

    h.add_vertex('0')
    h.add_vertex('1')
    h.add_vertex('2')
    h.add_vertex('3')
    h.add_vertex('4')

    h.add_edge('0', '1', 1)
    h.add_edge('1', '2', 1)
    h.add_edge('2', '3', 1)
    h.add_edge('3', '4', 1)
    h.add_edge('4', '0', 1)

    print(h.caixeiro())
    fimH = time.time()

    iniG = time.time()
    g = Graph()

    g.add_vertex('Porto Alegre')
    g.add_vertex('Maceio')
    g.add_vertex('Rio de Janeiro')
    g.add_vertex('Sao Luis')
    g.add_vertex('Cuiaba')
    g.add_vertex('Criciuma')

    g.add_edge('Porto Alegre', 'Maceio', 3.5)
    g.add_edge('Porto Alegre', 'Rio de Janeiro', 1)
    g.add_edge('Porto Alegre', 'Sao Luis', 2)
    g.add_edge('Porto Alegre', 'Cuiaba', 3)
    g.add_edge('Maceio', 'Rio de Janeiro', 2)
    g.add_edge('Maceio', 'Sao Luis', 1)
    g.add_edge('Maceio', 'Cuiaba', 2)
    g.add_edge('Maceio', 'Criciuma', 3)
    g.add_edge('Rio de Janeiro', 'Sao Luis', 2.9)
    g.add_edge('Rio de Janeiro', 'Cuiaba', 1)
    g.add_edge('Rio de Janeiro', 'Criciuma', 2)
    g.add_edge('Cuiaba', 'Criciuma', 2.2)
    g.add_edge('Criciuma', 'Porto Alegre', 0.3)
    g.add_edge('Sao Luis', 'Criciuma', 1)
    g.add_edge('Sao Luis', 'Cuiaba', 2)

    print(g.caixeiro())
    fimG = time.time()

    iniK = time.time()
    k = Graph()

    k.add_vertex('a')
    k.add_vertex('b')
    k.add_vertex('c')
    k.add_vertex('d')
    k.add_vertex('e')
    k.add_vertex('f')
    k.add_vertex('g')
    k.add_vertex('h')
    k.add_vertex('i')
    k.add_vertex('j')

    k.add_edge('a', 'c', 60)  
    k.add_edge('c', 'e', 70)
    k.add_edge('e', 'g', 70)
    k.add_edge('g', 'i', 80)
    k.add_edge('b', 'a', 170)
    k.add_edge('c', 'd', 180)
    k.add_edge('f', 'e', 180)
    k.add_edge('g', 'h', 180)
    k.add_edge('j', 'i', 190)
    k.add_edge('b', 'd', 70)
    k.add_edge('d', 'b', 70)
    k.add_edge('d', 'f', 70)
    k.add_edge('f', 'd', 70)
    k.add_edge('f', 'h', 70)
    k.add_edge('h', 'f', 70)
    k.add_edge('h', 'j', 70)
    k.add_edge('j', 'h', 70) 

    print(k.caixeiro())
    fimK = time.time()

    print("Grafo H: ", fimH-iniH)
    print("Grafo G: ", fimG-iniG)
    print("Grafo K: ", fimK-iniK)