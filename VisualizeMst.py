import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from Graph import Graph as myGraph
from sys import stdin

def visualize(matrix, edges_in_mst):
	
	grf = nx.from_numpy_matrix(np.array(matrix))

	pos = nx.spring_layout(grf)
	edge_labels = nx.get_edge_attributes(grf, 'weight')

	nx.draw_networkx_nodes(grf, pos, node_color = 'pink')
	nx.draw_networkx_labels(grf, pos)
	nx.draw_networkx_edges(grf, pos, edge_color = 'purple', width = 1.5) # show all edges, thin lines
	nx.draw_networkx_edges(grf, pos, edgelist = edges_in_mst, edge_color = 'red', width = 2.5) # highlight mst
	nx.draw_networkx_edge_labels(grf, pos, edge_labels = edge_labels)

	plt.show()	

