import queue
import math

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
        #self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def getEdges(self):
        for v in g:
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                print('( %s , %s, %3d)' % (vid, wid, v.get_weight(w)))

    def get_vertices(self):
        return self.vert_dict.keys()

    def setAllUnexplored(self):
         for v in self:
            v.explored = False

    def dfs(self,s):
        P = list()  #Cria pilha
        P.append(s)
        while(len(P) != 0):
            v = P.pop()
            v.explored = True   
            for w in v.get_connections():    
                if(w.explored == False):   
                    P.append(w) #Insere na pilha         
        P.clear() 

    def grauDoVertice(self,u):
        grau = 0
        for v in self:
            for w in v.get_connections():
                if(v.id == u.id or w.id == v.id):
                    grau +=1
        return grau
    
    def isConected(self):
        self.setAllUnexplored()
        for v in self:
            if(v.explored == False): 
                for w in v.get_connections():
                    if(self.grauDoVertice(v) > 0):
                        self.dfs(v) 
                        v.explored = True
                    if( self.grauDoVertice(w) > 0):
                        self.dfs(w) 
                        w.explored = True                        
        for v in self:
            if(v.explored == False):
                return False                   
        return True 

    def isEulerian(self):
        if(self.isConected() == False):
            return 'Não é Euleriano, desconexo'
        impares = 0
        for v in self:
            if(self.grauDoVertice(v)%2 != 0):
                impares += 1
        if impares == 0:
            return 'Tem ciclo Euleriano'
        if impares == 2:
            return 'Tem caminho Euleriano'
        if impares > 2:
            return 'Não é Euleriano'


if __name__ == '__main__':

    g = Graph()

    g.add_vertex('0')
    g.add_vertex('1')
    g.add_vertex('2')
    g.add_vertex('3')
    g.add_vertex('4')
    g.add_vertex('5')

    g.add_edge('0', '1', 1)
    g.add_edge('1', '2', 1)
    g.add_edge('2', '3', 1)
    g.add_edge('3', '0', 1)
    g.add_edge('2', '4', 1)
    g.add_edge('1', '5', 1)

    print(g.isEulerian())