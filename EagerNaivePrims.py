"""
Prim's implemented with adjacency matrix and traversal.
Eager - Insert, extract_min and decrease_key are for keys corresponding to vertices.
"""
from Graph import Graph
INFINITY = float('inf')

class KeyList(list):
	def __init__(self, nfverts):
		super().__init__([INFINITY for i in range(nfverts)])
		src = 0
		self[src] = 0

	def extract_min(self, visited):
		# Returns vertex, with minimum key, that has not been visited.
		minn, minind = INFINITY, None

		for ind, current_key in enumerate(self):
			if ind not in visited:
				if minn > current_key: 
					minn = current_key
					minind = ind
		return minind

	def decrease_key(self, ind, newval):
		assert newval <= self[ind], "Given value is greater than key."
		self[ind] = newval

def prims_mst(grf):
	key_list = KeyList(grf.nfverts)
	precursor = [None] * grf.nfverts
	visited = set()

	def adjacent_vertices_of(u_vertex):
		# Generator returning adjacent vertices of a given vertex.
		for v_vertex, edge_cost in enumerate(grf.graph[u_vertex]):
			if edge_cost > 0:
				yield v_vertex

	for _ in range(grf.nfverts):
		u = key_list.extract_min(visited)	
		visited.add(u)

		for v in adjacent_vertices_of(u):
			if v not in visited and grf.graph[u][v] < key_list[v]:
				key_list.decrease_key(v, grf.graph[u][v]) 
				precursor[v] = u

	return precursor