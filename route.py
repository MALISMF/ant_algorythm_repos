class Route:
    def __init__(self, nodes, edges, length, q):
        self.nodes = nodes
        self.edges = edges
        self.length = length
        self.addpheromones = q/length

