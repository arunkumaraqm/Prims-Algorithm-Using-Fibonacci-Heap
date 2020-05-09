from collections import defaultdict

class Graph:
	"""
	We use a list of lists for adjacency matrix representation.
	We use a dictionary of dictionaries for adjacency lists representation.
	If vertex 0 is connected to vertex 4 with the weight 500
	and vertex 1 is connected to vertex 4 with the weight 900, 
	this is what it looks like:
	{
	0: {4: 500},
	1: {4: 900},
	4: {0: 500, 1: 900}

	}

	In both representations, an edge weight can be accessed by graph[u][v]
	but the adj lists will raise a KeyError if there is no edge u-v.
	An object of this class cannot have both of these representations simulataneously.
	"""

	def __init__(self, nfverts = None, representation = None):
		self.nfverts = nfverts # no. of vertices

		self.representation = representation if representation else "matrix"
		if self.representation == "matrix":
			self.graph = [] # list of lists

		elif self.representation == "lists":
			self.graph = defaultdict(dict) # dict of dicts
		
		else:
			raise ValueError("Invalid representation.")

	def read_from_file(self, input_file): 
		# The input should be an adjacency matrix either way.

		self.nfverts = int(input_file.readline())
		
		if self.representation == "matrix": 
			def inner_loop(u):
				self.graph.append([int(number) for number in input_file.readline().split()])
		else:
			def inner_loop(u):
				for v, number in enumerate(input_file.readline().split()):
					number = int(number)
					if number != 0: self.graph[u][v] = number


		for u in range(self.nfverts): 
			inner_loop(u)

	def change_representation(self):
		# Changes representation from matrix to lists or vice versa 
		# and returns old representation

		if self.representation == "matrix":
			adj_lists = defaultdict(dict)
			for i, row in enumerate(self.graph):
				for j, ele in enumerate(row):
					if ele != 0: adj_lists[i][j] = ele
			temp = self.graph
			self.graph = adj_lists
			self.representation = "lists"
			return temp
		
		else:
			adj_mat = []
			for i in range(self.nfverts):
				row = []
				for j in range(self.nfverts):
					try:
						ele = self.graph[i][j]
					except KeyError:
						ele = 0
					row.append(ele)
				adj_mat.append(row)
			temp = self.graph
			self.graph = adj_mat
			self.representation = "matrix"
			return temp

	def fill_with_zeros(self):
		# Fill the adjacency matrix with zeros to initialize mst.

		assert self.representation == "matrix", "Wrong representation!"
		self.graph = [[0] * self.nfverts for _ in range(self.nfverts)]

	def __str__(self):
		if self.representation == "matrix":
			return "\n".join(str(row) for row in self.graph)
		else: # You expect that it prints edges but that's not what it does.
			return '\n'.join(str(adj_list) for adj_list in self.graph.items())

def compute_mst_and_cost(precursor, grf):
	"""
	Makes the adjacency matrix of the minimum spanning tree,
	returns that graph and also returns the total cost of the MST.
	"""
	
	mst = Graph(grf.nfverts, representation = "matrix")
	mst.fill_with_zeros()
	cost = 0

	# precursor[0] is useless.
	for cur, parent in enumerate(precursor[1:], 1):
		#print(f"(cur, par) = ({cur, parent})")
		mst.graph[parent][cur] = grf.graph[parent][cur]
		cost += grf.graph[parent][cur]
	
	return mst, cost
