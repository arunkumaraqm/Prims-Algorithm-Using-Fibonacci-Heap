class MinHeap:

	def __init__(self, arr = None, already_heap = False):
		"""
		Creates an empty heap when passed with no parameters.
		Initializes self.arr when passed with an array that is already a heap.
		Calls build_heap when passed array is not a heap.
		"""
		if not arr:
			self.arr = [None]
			self.size = 0
		elif already_heap:
			self.arr = [None] + arr # 1 based indexing
			self.size = len(self.arr) - 1
		else:
			self.build_heap(arr)

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
			else:
				break

	def sift_up(self, ind):
		"""
		Swaps node with its parent repeatedly
		until the node is larger than its parent.
		"""
		while True:
			parent = ind//2
			if parent == 0: break
			if self.arr[ind] < self.arr[parent]:
				self.swap(ind, parent)
				ind = parent
			else:
				break

	def swap(self, ind1, ind2):
		self.arr[ind1], self.arr[ind2] = self.arr[ind2], self.arr[ind1]

	def find_min_child(self, ind):
		"""
		Returns the index of the smaller child of a node.
		Returns -1 if node is a leaf.
		"""
		left = ind * 2
		right = left + 1
		if left > self.size:
			return -1
		if right > self.size:
			return left
		if self.arr[left] < self.arr[right]:
			return left
		else:
			return right

	def build_heap(self, arr):
		self.arr = [None] + arr
		self.size = len(self.arr) - 1
		for i in range(self.size // 2, 0, -1):
			self.sift_down(i)

	def insert(self, ele):
		self.arr.append(ele)
		self.size += 1
		self.sift_up(self.size)

	def decrease_key(self, ind, ele):
		assert self.arr[ind] < ele
		self.arr[ind] = ele
		self.sift_up(ind)

	def extract_min(self):
		"Removes and returns the minimum key from heap."
		if self.size == 0: return None
		minn = self.arr[1]
		self.arr[1] = self.arr[self.size]
		del self.arr[self.size]
		self.size -= 1

		self.sift_down(1)
		return minn

	def merge(self, other):	
		"Builds a new MinHeap after combining the two existing ones."
		return MinHeap(self.arr[1:] + other.arr[1:])
	
	def __str__(self):
		return str(self.arr[1:])

def heapsort(arr):
	# Descending order since we're using a min-heap
	heap = MinHeap(arr)
	while heap.size:
		heap.swap(1, heap.size)
		heap.size -= 1
		heap.sift_down(1)
	return heap.arr[1:]


"""
# Tests for extract_min:
def testing_extract_min_1():
	heap = MinHeap([10, 20, 25, 22, 30, 25, 28], already_heap = True)
	for i in range(1, 8):
		print(heap.extract_min(), heap)

def testing_extract_min_2():
	heap = MinHeap([90, 90, 90], already_heap = True)
	for i in range(3):
		print(heap.extract_min(), heap)

def testing_extract_min_3():
	heap = MinHeap([], already_heap = True)
	for i in range(3):
		print(heap.extract_min(), heap)

Tests for decrease_key:

#1
heap = MinHeap([10, 20, 25, 22, 30, 25, 28], already_heap = True)
for i in range(1, 8):
	heap.decrease_key(i, heap.arr[i] - 1)
print(heap)

#2
heap = MinHeap([10, 20, 25, 22, 30, 25, 28], already_heap = True)
heap.decrease_key(7, 0)
print(heap)

#3
heap = MinHeap([10, 20, 25, 22, 30, 25, 28], already_heap = True)
heap.decrease_key(1, 11)
print(heap)

Tests for insert:
#1
heap = MinHeap()
for i in [60, 20, 10, 70, 35, 24]:
	heap.insert(i)
	print(heap)

#2
heap = MinHeap([10, 20, 30, 40, 50])
for i in [40, 30, 20, 10]:
	heap.insert(i)
	print(heap)

Tests for build_heap:
#1
heap = MinHeap([60, 20, 10, 70, 35, 24])
print(heap)

#2
heap = MinHeap()
heap.build_heap([10, 20, 30, 40, 50, 40, 30, 20, 10])
print(heap)

Tests for sift_up:
#1
heap = MinHeap([10, 20, 25, 22, 30, 25, 28], already_heap = True)
for i in range(1, 7):
	heap.sift_up(i)
	print(heap)

#2
heap = MinHeap([10, 20, 25, 22, 30, 25, 18], already_heap = True)
heap.sift_up(7)
print(heap)

#3
heap = MinHeap([10, 20, 25, 22, 30, 25, 9], already_heap = True)
heap.sift_up(7)
print(heap)

#4
heap = MinHeap([10, 20, 25, 18, 19, 25, 28], already_heap = True)
heap.sift_up(5)
heap.sift_up(4)
print(heap)

Tests for sift_down:
#1
heap = MinHeap([10, 20, 25, 22, 30, 25, 28], already_heap = True)
for i in range(1, 7):
	heap.sift_down(i)
	print(heap)

#2
heap = MinHeap([10, 20, 25, 22, 30, 25, 18], already_heap = True)
heap.sift_down(3)
print(heap)

#3
heap = MinHeap([10, 20, 25, 12, 30, 25, 28], already_heap = True)
heap.sift_down(2)
print(heap)

#4
heap = MinHeap([70, 20, 25, 22, 30, 25, 28], already_heap = True)
print(heap)
heap.sift_down(1)
print(heap)
"""