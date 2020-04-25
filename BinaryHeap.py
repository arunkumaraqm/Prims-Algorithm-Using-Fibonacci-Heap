INFINITY = float('inf')

class MinHeap:
	"""
	Binary min-heap using array method.
	Supports operations extract_min, decrease_key, insert, merge.
	"""

	def __init__(self, arr = None, already_heap = False):
		"""
		Creates an empty heap when passed with no parameters.
		Initializes self.arr when passed with a list that is already a heap.
		Calls build_heap when given list is not a heap.
		"""
		if not arr:
			self.arr = []

		elif already_heap:
			self.arr = arr # 0 based indexing

		else:
			self.build_heap(arr)

	def __len__(self): return len(self.arr)

	def __str__(self):
		return str(self.arr)

	def swap(self, ind1, ind2):
		self.arr[ind1], self.arr[ind2] = self.arr[ind2], self.arr[ind1]

	def find_min_child(self, ind):
		"""
		Returns the index of the smaller child of a node.
		Returns -1 if node is a leaf.
		"""
		left = ind * 2 + 1
		right = left + 1

		if left >= len(self):
			return -1
		if right >= len(self):
			return left

		if self.arr[left] < self.arr[right]: return left
		else: return right

	def sift_down(self, ind):
		"""
		Swaps node with the smaller child repeatedly 
		until the node is smaller than both its children.
		"""
		while True:
			desired_child = self.find_min_child(ind)
			if desired_child == -1: break

			if self.arr[ind] > self.arr[desired_child]:
				self.swap(ind, desired_child)
				ind = desired_child
			else: break

	def sift_up(self, ind):
		"""
		Swaps node with its parent repeatedly
		until the node is larger than its parent.
		"""
		while True:
			if ind == 0: break # Root node has no parent
			parent = (ind-1)//2 

			if self.arr[ind] < self.arr[parent]:
				self.swap(ind, parent)
				ind = parent
			else: break

	def build_heap(self, arr):
		self.arr = arr

		# Performing sift down on all non-leaf nodes.
		# Leaf nodes always occupy the latter half of the array.
		for i in range((len(self) - 1) // 2, 0 -1, -1):
			self.sift_down(i)

	def insert(self, ele):
		self.arr.append(ele)
		self.sift_up(len(self) - 1) # Sift Up on the last element

	def decrease_key(self, ind, ele):
		if self.arr[ind] >= ele: 
			raise ValueError("New value is greater than current value!")
		self.arr[ind] = ele
		self.sift_up(ind)

	def extract_min(self):
		"Removes and returns the minimum key from heap."
		if len(self) == 0: return None

		minn = self.arr[0]
		self.arr[0] = self.arr[-1]
		del self.arr[-1]

		self.sift_down(0)
		return minn

	def merge(self, other):	
		"Builds a new MinHeap after combining the two existing ones."
		return MinHeap(self.arr + other.arr)
	
def heapsort(arr):
	# Sorts arr in ascending order and returns sorted array.
	# Note: a min-heap heapsort sorts in descending order in your textbooks.
	# But this function doesn't do it in-place.
	heap = MinHeap(arr)
	size = len(arr)
	sorted_arr = [heap.extract_min() for i in range(size)]
	return sorted_arr

###########################################
## ADDITIONS FOR USE IN PRIM'S ALGORITHM ##
###########################################

class HeapNode():
	"The array in minheap will be a list of HeapNodes."
	def __init__(self, vertex, key, index):
		self.vertex = vertex
		self.key = key
		self.index = index 
		# We need the index attribute because decrease_key needs to sift_up on an index.
		# index is updated whenever the HeapNode moves to another place in the array.

	# Dunder methods for comparison of keys
	def __lt__(self, other): return self.key < other.key
	def __le__(self, other): return self.key <= other.key
	def __gt__(self, other): return self.key > other.key
	def __ge__(self, other): return self.key >= other.key
	def __eq__(self, other): return self.key == other.key

	def __str__(self):
		return f"({self.vertex}, {self.key}, {self.index})"	

class MinHeapForPrims(MinHeap):
	"""
	For Prim's algorithm, each node in the array will have to store vertex and key.
	And the heap will be maintained only with respect to keys.
	Given any vertex, we must be able to fetch the key from the heap
	i.e. fetch the corresponding HeapNode from the heap.
	"""
	def __init__(self, nfverts):
		# Initializes arr to [0, inf, inf, inf, ...]
		src = 0 

		# vertex_heapnode_map is implemented using a list instead of a dict
		# because vertices are labeled from 0 to nfverts - 1 anyway.
		# Initially, node.index = node.vertex.
		self.vertex_heapnode_map = [HeapNode(vx, INFINITY, vx) for vx in range(nfverts)]
		first_node = self.vertex_heapnode_map[src]
		first_node.key = 0

		# Need a copy for arr because operations will change the order of nodes in arr but 
		# the order in vertex_heapnode_map will remain unchanged.
		self.arr = self.vertex_heapnode_map.copy()

	def swap(self, ind1, ind2): # Assumes non-negative indices
		# Swaps HeapNodes in arr but also maintaince node.index properly.
		self.arr[ind1], self.arr[ind2] = self.arr[ind2], self.arr[ind1]
		self.arr[ind1].index = ind1
		self.arr[ind2].index = ind2

	def extract_min(self):
		# Extracts and returns vertex with minimum key.
			if len(self) == 0: return None

			extracted_vertex = self.arr[0].vertex
			self.swap(0, len(self) - 1)
			del self.arr[-1]

			self.sift_down(0)
			return extracted_vertex

	def decrease_key(self, vertex, new_key):
		# Decreases the key for a given vertex to new_key.

		node = self.vertex_heapnode_map[vertex]

		assert node.key >= new_key, "New value is greater than current value!"
		node.key = new_key
		self.sift_up(node.index)

	def __str__(self):
		return "\n".join(str(node) for node in self.arr) + "\n"

	def fetch_key(self, vertex):
		return self.vertex_heapnode_map[vertex].key
