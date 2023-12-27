import random
import collections
import heapq
import matplotlib.pyplot as plt
import networkx as nx
from heapdict import heapdict
import scipy

class GraphVisualizer:
    def __init__(self, times):
        self.edges = collections.defaultdict(list)
        for u, v, w in times:
            self.edges[u].append((v, w))

        self.G = nx.DiGraph()

        for node, neighbors in self.edges.items():
            for neighbor, weight in neighbors:
                self.G.add_edge(node, neighbor, weight=weight)

    def draw_graph(self, layout=None, path=None):
        layouts = {
            'circular': nx.circular_layout,
            'spring': nx.spring_layout,
            'shell': nx.shell_layout,
            'kamada_kawai': nx.kamada_kawai_layout,
            'planar': nx.planar_layout,
            'spectral': nx.spectral_layout,
            'random': nx.random_layout,
            'bipartite': nx.bipartite_layout,
            'spiral': nx.spiral_layout,
            'fruchterman_reingold': nx.fruchterman_reingold_layout,
        }

        if layout not in layouts:
            print(f"Unknown layout '{layout}'. Using 'circular' layout.")
            layout = 'circular'

        pos = layouts[layout](self.G)

        plt.figure(figsize=(12, 12))  # Increase figure size
        nx.draw(self.G, pos, with_labels=True, node_size=300, node_color="skyblue", font_size=8, font_color="black",
                font_weight="bold", arrowsize=15, width=1.5, edge_color="gray")

        if path:
            path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
            nx.draw_networkx_edges(self.G, pos, edgelist=path_edges, edge_color='r', width=2.0)

        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels)

        plt.show()

class GraphEngine:
    @staticmethod
    def generate_random_edges(n_nodes, max_weight=10, density=0.3):
        edges = []
        for i in range(n_nodes):
            for j in range(n_nodes):
                if i != j and random.random() < density:
                    weight = random.randint(1, max_weight)
                    edges.append((i, j, weight))
        return edges

    @staticmethod
    def visualize_graph(times, layout='circular', path=None):
        visualizer = GraphVisualizer(times)
        visualizer.draw_graph(layout, path)

    @staticmethod
    def shortest_path_summary(n, edges, src):
        adj = collections.defaultdict(list)

        for s, d, weight in edges:
            adj[s].append([d, weight])

        shortest = {}
        minHeap = [[0, src]]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, n2])
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest

    @staticmethod
    def find_most_efficient_path(n, edges, src, target):
        adj = collections.defaultdict(list)

        for s, d, weight in edges:
            adj[s].append([d, weight])

        minHeap = [[0, src, []]]  # Include an empty list for path tracking

        while minHeap:
            w1, n1, path = heapq.heappop(minHeap)
            if n1 == target:
                return path + [n1]  # Return the path if the target is reached

            for n2, w2 in adj[n1]:
                if n2 not in path:
                    heapq.heappush(minHeap, [w1 + w2, n2, path + [n1]])

        return []

# Example usage
if __name__ == "__main__":
    # Generate random edges
    random_edges = GraphEngine.generate_random_edges(n_nodes=12, max_weight=10, density=.4)
    print("Edges:", random_edges)

    # Visualize the graph
    #GraphEngine.visualize_graph(random_edges, layout='random')
    layout = 'kamada_kawai'
    # Find and visualize the most efficient path
    target_node = 1  # Change the target node as needed
    most_efficient_path = GraphEngine.find_most_efficient_path(len(random_edges), random_edges, src=0, target=target_node)

    print(f"Most Efficient Path to Node {target_node}: {most_efficient_path}")

    GraphEngine.visualize_graph(random_edges, layout=layout, path=most_efficient_path)
