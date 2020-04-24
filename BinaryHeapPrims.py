"Prims using adjacency matrix and binary heap."

from BinaryHeapStandard import MinHeap
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

class HeapNode():
	def __init__(self, vertex, key, index):
		self.vertex = vertex
		self.key = key
		self.index = index

	def __lt__(self, other): return self.key < other.key
	def __le__(self, other): return self.key <= other.key
	def __gt__(self, other): return self.key > other.key
	def __ge__(self, other): return self.key >= other.key
	def __eq__(self, other): return self.key == other.key

	def __str__(self):
		return f"({self.vertex}, {self.key}, {self.index})"	

class MinHeapForPrims(MinHeap):
	def __init__(self, nfverts):
		src = 0 
		self.vertex_heapnode_map = [HeapNode(vx, INFINITY, vx) for vx in range(nfverts)]
		first_node = self.vertex_heapnode_map[src]
		first_node.key = 0

		self.arr = self.vertex_heapnode_map.copy()

	def swap(self, ind1, ind2): # Assumes non-negative indices
		self.arr[ind1], self.arr[ind2] = self.arr[ind2], self.arr[ind1]
		self.arr[ind1].index = ind1
		self.arr[ind2].index = ind2

	def extract_min(self):
			if len(self) == 0: return None

			extracted_vertex = self.arr[0].vertex
			self.swap(0, len(self) - 1)
			del self.arr[-1]

			self.sift_down(0)
			return extracted_vertex

	def decrease_key(self, vertex, new_key):
		node = self.vertex_heapnode_map[vertex]

		assert node.key >= new_key, "New value is greater than current value!"
		node.key = new_key
		self.sift_up(node.index)

	def __str__(self):
		return "\n".join(str(node) for node in self.arr) + "\n"

	def fetch_key(self, vertex):
		return self.vertex_heapnode_map[vertex].key

def adjacent_vertices_of(u_vertex, graph):
	"Generator returning adjacent vertices of a given vertex."
	for v_vertex, edge_cost in enumerate(graph.mat[u_vertex]):
		if edge_cost > 0:
			yield v_vertex

def prims_mst(graph):
	precursor = [None] * graph.nfverts
	visited = [False] * graph.nfverts

	src = 0
	heap = MinHeapForPrims(graph.nfverts)
	#print(heap)

	for _ in range(graph.nfverts):
		u = heap.extract_min()
		#print("After extraction: \n", heap)
		visited[u] = True

		for v in adjacent_vertices_of(u, graph):
			if visited[v] == False and graph.mat[u][v] < heap.fetch_key(v):
				heap.decrease_key(v, graph.mat[u][v]) 
				#print(f"After decrease_key on {v}: \n", heap)
				precursor[v] = u
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