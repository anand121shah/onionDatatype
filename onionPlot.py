import matplotlib.pyplot as plt
import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_node("Component A")
G.add_node("Component B")
G.add_node("Component C")
G.add_node("Component D")

# Add edges to the graph
G.add_edge("Component A", "Component B")
G.add_edge("Component B", "Component C")
G.add_edge("Component C", "Component D")
G.add_edge("Component D", "Component A")

# Set node positions
pos = nx.circular_layout(G)

# Draw the nodes and edges
nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=1000)
nx.draw_networkx_edges(G, pos, edge_color="gray")

# Add labels to the nodes
nx.draw_networkx_labels(G, pos, font_color="black", font_size=12)

# Set plot attributes
plt.axis("off")
plt.title("Onion Diagram")
plt.tight_layout()

# Display the diagram
plt.show()
