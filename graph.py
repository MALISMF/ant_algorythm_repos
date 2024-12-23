from edge import Edge

class Graph:
    def __init__(self):
        self.edges = {}  
        self.nodes = []

    def add_edge(self, node1, node2, length):
        edge = Edge(node1, node2, length) 
        """add a new edge"""
        if node1 not in self.edges:
            self.edges[node1] = []
        if node2 not in self.edges:
            self.edges[node2] = []

        self.edges[node1].append(edge)

        """add a new node"""
        if node1 not in self.nodes:
            self.nodes.append(node1)
        if node2 not in self.nodes:
            self.nodes.append(node2)

    def get_edge(self, from_node, to_node):
        """
        Возвращает ребро между двумя заданными узлами.

        Параметры:
        from_node (str): начальный узел
        to_node (str): конечный узел

        Возвращает:
        Edge: ребро между узлами или None, если ребро не найдено
        """
        if from_node in self.edges:
            for edge in self.edges[from_node]:
                if edge.nodes[1] == to_node:
                    return edge
        return None
    
    
    def pheromone_update(self, rho, q, route):
        length = route.length

        for node in self.nodes:
            for edge in self.edges[node]:
                edge.pheromone *= rho # испарение
                edge.pheromone += q/length # добавление

