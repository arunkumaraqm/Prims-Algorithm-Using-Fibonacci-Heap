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

	def __init__(self, nfverts, representation = None):
		self.nfverts = nfverts # no. of vertices

		self.representation = representation if representation else "matrix"
		if self.representation == "matrix":
			self.graph = [] # list of lists

		elif self.representation == "lists":
			self.graph = defaultdict(dict) # dict of dicts
		
		else:
			raise ValueError("Invalid representation.")

	def __read_adjacency_matrix(self):
		for _ in range(self.nfverts):
			self.graph.append([int(number) for number in input().split()])
			
	def __read_adjacency_lists(self): 
		for u in range(self.nfverts):
			for v, number in enumerate(input().split()):
				number = int(number)
				if number != 0: self.graph[u][v] = number
		
	def read_from_stdin(self):
		# The input should be an adjacency matrix either way.
		if self.representation == "matrix": self.__read_adjacency_matrix()	
		else: self.__read_adjacency_lists()

	def fill_with_zeros(self):
		# Fill the adjacency matrix with zeros to initialize mst.

		assert self.representation == "matrix", "Wrong representation!"
		self.graph = [[0] * self.nfverts for _ in range(self.nfverts)]

	def __str__(self):
		if self.representation == "matrix":
			return "\n".join(str(row) for row in self.graph)
		else: # You expect that it prints edges but that's not what it does.
			return '\n'.join(str(adj_list) for adj_list in self.graph.items())
