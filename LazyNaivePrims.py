"""
Prim's implemented with adjacency matrix and traversal.
Lazy - edges are extracted and inserted, as opposed to vertices.
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

class EdgeNode:
	def __init__(self, from_vx, to_vx, weight):
		self.from_vx = from_vx
		self.to_vx = to_vx
		self.weight = weight

	def __lt__(self, other): return self.weight < other.weight
	def __le__(self, other): return self.weight <= other.weight
	def __gt__(self, other): return self.weight > other.weight
	def __ge__(self, other): return self.weight >= other.weight
	def __eq__(self, other): return self.weight == other.weight

	def __str__(self):
		return f"({self.from_vx}, {self.to_vx}, {self.weight})"

class EdgeList(list):

	def extract_min(self):
		"Returns vertex, with minimum key, that has not been visited."
		minn, min_ind = EdgeNode(None, None, INFINITY), None
		for node_ind, node in enumerate(self):
			if node < minn:
				minn = node
				min_ind = node_ind
		
		try: del self[min_ind]
		except TypeError: 
			print("Nothing to extract! Exiting.")
			exit()
		
		return minn

	def insert(self, new_node: EdgeNode):
		self.append(new_node)

	def __str__(self):
		return "[{}]".format(", ".join(str(ele) for ele in self))

def adjacent_vertices_of(u_vertex, graph):
	"Generator returning adjacent vertices of a given vertex."
	for v_vertex, edge_cost in enumerate(graph.mat[u_vertex]):
		if edge_cost > 0:
			yield v_vertex


def prims_mst(graph):
	precursor = [None] * graph.nfverts
	visited = [False] * graph.nfverts
	edge_list = EdgeList()

	def insert_useful_edges_to_edge_list(cur_vx):
		for other_vx in adjacent_vertices_of(cur_vx, graph):
			if visited[other_vx] == False:
				new_node = EdgeNode(cur_vx, other_vx, graph.mat[cur_vx][other_vx])
				edge_list.insert(new_node)

	src = 0
	visited[src] = True
	precursor[src] = None

	insert_useful_edges_to_edge_list(src)

	for _ in range(graph.nfverts - 1): # We need (|V| - 1) edges for a spanning tree.
		while True:
			popped_node = edge_list.extract_min()
			from_vx, cur_vx, weight = popped_node.from_vx, popped_node.to_vx, popped_node.weight 

			if visited[cur_vx] == True: # This means there this edge will form a cycle in mst.
				continue # So we need to choose a different edge.
			else: 
				break

		visited[cur_vx] = True
		precursor[cur_vx] = from_vx

		insert_useful_edges_to_edge_list(cur_vx)

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