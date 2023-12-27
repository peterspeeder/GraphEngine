# Graph Visualization and Shortest Path Algorithm

This Python code provides functionality for generating a random directed graph with weighted edges, visualizing the graph using matplotlib and networkx, and computing the shortest paths from a specified source node using Dijkstra's algorithm.

## Requirements

- Python 3.x
- Matplotlib
- Networkx

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repository
    ```

3. Run the example:

    ```bash
    python your_script_name.py
    ```

## Code Structure

The code is organized into two classes:

- `GraphVisualizer`: Handles the visualization of a directed graph using matplotlib and networkx.
- `GraphEngine`: Provides methods for generating random edges, visualizing the graph, and computing the shortest paths.

## Example

```python
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
