class MinHeap:
	def __init__(self, arr = None, already_heap = False):
		"""
		Creates an empty heap when passed with no parameters.
		Initializes self.arr when passed with an array that is already a heap.
		Calls build_heap when passed array is not a heap.
		"""
		if not arr:
			self.arr = []

		elif already_heap:
			self.arr = arr # 0 based indexing

		else:
			self.build_heap(arr)

	def __len__(self): return len(self.arr)

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
		assert self.arr[ind] >= ele, "New value is greater than current value!"
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
	
	def __str__(self):
		return str(self.arr)

def heapsort(arr):
	# Descending order since we're using a min-heap
	heap = MinHeap(arr)
	size = len(arr)
	sorted_arr = [heap.extract_min() for i in range(size)]
	return sorted_arr

