from edge import Edge
from graph import Graph
from route import Route
import random
import matplotlib.pyplot as plt
import numpy as np


class AntColony:
    def __init__(self, num_ants, num_cities, num_iterations, alpha, beta, rho, q):
        self.num_ants = 30
        self.num_cities = 6
        self.num_iterations = 10000
        self.alpha = 0.7
        self.beta = 1
        self.rho = 0.5
        self.q = 1
        self.rrr = [5]

    

    def choose_edge(self, node, neighbors):

        """
        Расчитываем шансы для каждого соседа.

        node (str): текущий узел
        neighbors (list): список соседей

        chances (list): список шансов для каждого соседа
        """
        chances = []
        for neighbor in neighbors:
            neighbors_pheromones = neighbor.pheromones #Значение феромонов соседа
            neighbors_attractivnes = neighbor.attractivnes #Обратная длина соседа

            probability_num = (neighbors_pheromones ** self.alpha) * (neighbors_attractivnes ** self.beta)
            probability_denom = sum((neighbor.pheromones ** self.alpha) * (neighbor.attractivnes ** self.beta) for neighbor in neighbors)
            probability = probability_num / probability_denom #Шанс перейти в соседа
            
            chances.append(probability)

        
        """
        Выбираем следующий узел из соседей с учетом шансов.

        next_node (str): следующий узел из соседей
        """
        
        if len(chances) != 0:
            chosen_edge = random.choices(neighbors, weights=chances)[0]
            return chosen_edge
        

    def algorithm(self):
        shortest_route = None
        for iteration in range(self.num_iterations):
            routes = []
            optimal_route_count = 0
            start_nodes = list(g1.nodes)
            for ant in range(self.num_ants):
                start_node = start_nodes[ant % len(start_nodes)]
                current_node = start_node
                visited_nodes = [current_node] 
                visited_edges = []
                length = 0
                while len(visited_nodes) < self.num_cities:
                    next_edge = self.choose_edge(current_node, [neighbor for neighbor in g1.edges[current_node] if neighbor.nodes[1] not in visited_nodes])
                    if next_edge is None:
                        break

                    visited_nodes.append(next_edge.nodes[1])
                    visited_edges.append(next_edge)
                    current_edge = next_edge
                    current_node = next_edge.nodes[1]
                    length += current_edge.length

                if len(visited_nodes) == self.num_cities:
                    return_edge = g1.get_edge(current_node, start_node)
                    if return_edge:
                        visited_nodes.append(start_node)
                        visited_edges.append(return_edge)
                        length += return_edge.length

                    if len(visited_nodes) == self.num_cities + 1:
                        route = Route(visited_nodes, visited_edges, length, 4)
                        routes.append(route)
                        if len(self.rrr) != 1000:
                            self.rrr.append(route)

                        if shortest_route is None or route.length < shortest_route.length:
                            shortest_route = route

                        if shortest_route and route.length == shortest_route.length:
                            optimal_route_count += 1

            self.update_pheromones(routes)

        
        if shortest_route:
            print("Shortest route found:")
            print(f"Nodes: {shortest_route.nodes}")
            print(f"Length: {shortest_route.length}")
        else:
            print("No valid route found.")


    def update_pheromones(self, routes):
        for route in routes:
            for edge in route.edges:

                edge.pheromones *= (1 - self.rho) # уменьшаем феромоны на коэффициенте испарения
                edge.pheromones += self.q / route.length # добавляем феромоны на основе длины пути


                
                
ant = AntColony(1,1,1,1,1,1,1)
g1 = Graph()
g1.add_edge('a', 'f', 1)
g1.add_edge('a', 'b', 3)

g1.add_edge('b', 'a', 3)
g1.add_edge('b', 'c', 8)
g1.add_edge('b', 'g', 3)

g1.add_edge('c', 'b', 3)
g1.add_edge('c', 'g', 1)
g1.add_edge('c', 'd', 1)

g1.add_edge('d', 'c', 8)
g1.add_edge('d', 'f', 1)

g1.add_edge('f', 'a', 3)
g1.add_edge('f', 'd', 3)

g1.add_edge('g', 'a', 3)
g1.add_edge('g', 'b', 3)
g1.add_edge('g', 'c', 3)
g1.add_edge('g', 'd', 5)
g1.add_edge('g', 'f', 4)



neighbors = g1.edges['a']

abc = ant.algorithm()



