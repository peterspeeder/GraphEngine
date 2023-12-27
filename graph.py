import random
import collections
import heapq
import matplotlib.pyplot as plt
import networkx as nx

class GraphVisualizer:
    def __init__(self, times):
        self.edges = collections.defaultdict(list)
        for u, v, w in times:
            self.edges[u].append((v, w))

        self.G = nx.DiGraph()

        for node, neighbors in self.edges.items():
            for neighbor, weight in neighbors:
                self.G.add_edge(node, neighbor, weight=weight)

    def draw_graph(self, layout='circular'):
        if layout == 'circular':
            pos = nx.circular_layout(self.G)
        elif layout == 'spring':
            pos = nx.spring_layout(self.G)
        else:
            pos = nx.shell_layout(self.G)  # Default to shell layout if layout is not recognized

        nx.draw(self.G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black",
                font_weight="bold", arrowsize=20, width=2, edge_color="gray")

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
    def visualize_graph(times, layout='circular'):
        visualizer = GraphVisualizer(times)
        visualizer.draw_graph(layout)

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

# Example usage
if __name__ == "__main__":
    # Generate random edges
    random_edges = GraphEngine.generate_random_edges(n_nodes=5, max_weight=10, density=0.4)
    print("Random Edges:", random_edges)

    # Visualize the graph
    GraphEngine.visualize_graph(random_edges, layout='circular')

    # Compute and print shortest paths summary
    shortest_paths = GraphEngine.shortest_path_summary(len(random_edges), random_edges, src=0)
    print("Shortest Paths Summary:")
    for node, distance in shortest_paths.items():
        print(f"Node {node}: Shortest Distance from Source (0): {distance}")
