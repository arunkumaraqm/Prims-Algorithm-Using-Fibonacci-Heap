"""
Prim's implemented with adjacency matrix and traversal.
Lazy - edges are extracted and inserted, as opposed to vertices.
"""
from Graph import Graph

class EdgeNode:
	"""
	A node in EdgeList representing a single edge.
	Each edge has a "from vertex", a "to vertex" and an edge weight.

	Note: 
		Yes, an edge in an undirected graph has no direction,
		but you can think of it as two edges -
		an edge from u to v with weight w
		and an edge from v to u with weight w.
		But we'll always only need one of these edges 
		because the from_vx is visited.
	"""

	def __init__(self, from_vx, to_vx, weight):
		self.from_vx = from_vx
		self.to_vx = to_vx
		self.weight = weight

	# Dunder methods for comparison of edge weights
	def __lt__(self, other): return self.weight < other.weight
	def __le__(self, other): return self.weight <= other.weight
	def __gt__(self, other): return self.weight > other.weight
	def __ge__(self, other): return self.weight >= other.weight
	def __eq__(self, other): return self.weight == other.weight

	def __str__(self):
		return f"({self.from_vx}, {self.to_vx}, {self.weight})"

class EdgeList(list):
	"""
	A list of EdgeNodes. 
	extract_min is done by traversing the list.
	no decrease_key because it is not needed for lazy implementation.
	"""

	def extract_min(self):
		# Extracts and returns minimum edge in EdgeList object.

		try:
			min_ind, min_edge_node = min(enumerate(self), key = lambda tupl: tupl[1].weight)
		except ValueError: # Empty sequence
			raise ValueError('Nothing to extract.')
		else: 
			del self[min_ind]
			return min_edge_node

	def insert(self, new_node):
		assert type(new_node) == EdgeNode
		self.append(new_node)

	def __str__(self):
		return "[{}]".format(", ".join(str(ele) for ele in self))


def prims_mst(grf):
	precursor = [None] * grf.nfverts # precursor[from_vx] := to_vx for vertices in MST
	visited = set()
	edge_list = EdgeList()

	def adjacent_vertices_of(u_vertex):
		# Generator returning adjacent vertices of a given vertex.
		
		for v_vertex, edge_wt in enumerate(grf.graph[u_vertex]):
			if edge_wt != 0:
				yield v_vertex

	def insert_useful_edges_to_edge_list(cur_vx):
		# Non-zero edges from cur_vx to unvistied vertices are "useful".

		for other_vx in adjacent_vertices_of(cur_vx):
			if other_vx not in visited:
				new_node = EdgeNode(cur_vx, other_vx, grf.graph[cur_vx][other_vx])
				edge_list.insert(new_node)

	src = 0
	visited.add(src)
	precursor[src] = None

	insert_useful_edges_to_edge_list(src)

	for _ in range(grf.nfverts - 1): # We need (|V| - 1) edges for a spanning tree.
		while True:
			popped_node = edge_list.extract_min()
			from_vx, cur_vx, weight = popped_node.from_vx, popped_node.to_vx, popped_node.weight 

			if cur_vx in visited: # This means there this edge will form a cycle in mst.
				continue # So we need to choose a different edge.
			else: 
				break

		visited.add(cur_vx)
		precursor[cur_vx] = from_vx

		insert_useful_edges_to_edge_list(cur_vx)

	return precursor
