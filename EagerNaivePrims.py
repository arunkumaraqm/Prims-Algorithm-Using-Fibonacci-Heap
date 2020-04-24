"""
Prim's implemented with adjacency matrix and traversal.
Eager - Insert, extract_min and decrease_key are for keys corresponding to vertices.
"""
INFINITY = float('inf')

class Graph:
	def __init__(self, nfverts):
		self.nfverts = nfverts
		self.mat = []

	def read_adjacency_matrix(self):
		"Reads matrix for graph from stdin."

		for _ in range(self.nfverts):
			self.mat.append([int(number) for number in input().split()])

	def fill_with_zeros(self):
		mat = []
		for _ in range(self.nfverts):
			mat.append([0] * self.nfverts)
		self.mat = mat

	def __str__(self):
		return "\n".join(str(row) for row in self.mat)

def extract_min(key, visited):
	"Returns vertex, with minimum key, that has not been visited."
	minn, minind = INFINITY, None

	for ind, current_key in enumerate(key):
		if visited[ind] == False:
			if minn > current_key: 
				minn = current_key
				minind = ind
	return minind

def decrease_key(key, ind, newval):
	assert newval < key[ind]
	key[ind] = newval

def adjacent_vertices_of(u_vertex, graph):
	"Generator returning adjacent vertices of a given vertex."
	for v_vertex, edge_cost in enumerate(graph.mat[u_vertex]):
		if edge_cost > 0:
			yield v_vertex


def prims_mst(graph):
	key = [INFINITY] * graph.nfverts
	precursor = [None] * graph.nfverts
	visited = [False] * graph.nfverts

	src = 0
	key[src], precursor[src] = 0, None

	for _ in range(graph.nfverts):
		u = extract_min(key, visited)
		visited[u] = True

		for v in adjacent_vertices_of(u, graph):
			if visited[v] == False and graph.mat[u][v] < key[v]:
				decrease_key(key, v, graph.mat[u][v]) # TODO Maybe this could be made more efficient.
				precursor[v] = u

	#print(f"key = {key}")
	#print(f"precursor = {[i + 1 for i in precursor]}")
	return precursor

def compute_mst_and_cost(precursor, graph):
	"Makes the adjacency matrix of the minimum spanning tree,\
	 returns that graph and also returns the total cost of the MST."
	
	mst = Graph(graph.nfverts)
	mst.fill_with_zeros()
	cost = 0

	# precursor[0] is useless.
	for cur, parent in enumerate(precursor[1:], 1):
		#print(f"(cur, par) = ({cur, parent})")
		mst.mat[parent][cur] = graph.mat[parent][cur]
		cost += graph.mat[parent][cur]
	
	return mst, cost


def main():
	"Driver function."
	nfverts = int(input())
	graph = Graph(nfverts)
	graph.read_adjacency_matrix()
	
	precursor = prims_mst(graph)
	mst, cost = compute_mst_and_cost(precursor, graph)
	
	print(mst)
	print(f"Cost = {cost}")
main()
