from collections import defaultdict
INFINITY = float('inf')
teststr = "loud"##

class FibHeapNode:
	"""
	Each node contains
	- key aka ele
	- rank = no. of children 
	- parent pointer because the node is a part of a heap ordered tree
	- left and right pointers because the node is a part of 
	circular doubly linked list
	- mark is a boolean value to indicate whether node has lost a child
	"""

	def __init__(self, ele):
		self.ele = ele
		self.rank = 0

		self.parent = None
		self.left = self
		self.right = self
		self.child = None

		self.mark = False # True if node lost one child.

	def children_generator(self):
		# Generates children from the circular linked list self.child
		if self.child is None: return 
		
		cur_child = self.child
		
		while cur_child.right is not self.child:
			yield cur_child
			cur_child = cur_child.right
		yield cur_child

	def print_tree(self, tabwidth = 0):
		"""
		Tabbed display of nodes
		No. of tabs = level at which that node is
		An asterisk after the value indicates that this node is marked
		"""

		print(tabwidth*"    ", self.ele, '*' if self.mark else '', sep = "")
		input()#
		for childtree in self.children_generator():
			childtree.print_tree(tabwidth + 1)

	def __str__(self):
		return str(self.ele)

	# Magic methods for comparison
	def __lt__(self, other): return self.ele < other.ele
	def __le__(self, other): return self.ele <= other.ele
	def __gt__(self, other): return self.ele > other.ele
	def __ge__(self, other): return self.ele >= other.ele
	def __eq__(self, other): return self.ele == other.ele


class FibHeap:
	"""
	The root list is a circular doubly linked list.
	It's beginning is given by the head pointer.
	min_node points to the node with the minimum key.

	Each node in root list is the root of a heap ordered tree.
	"""

	def __init__(self, head = None, min_node = None):
		if head is None:
			self.head = None
			self.min_node = None

		else:
			self.head = head
			self.min_node = min_node

	def insert(self, new_ele):
		# Inserting the newnode at the end of the root list.
		new_node = FibHeapNode(new_ele)

		if self.head:
			self.__merge_lls(self.head, new_node)

			if new_node < self.min_node: self.min_node = new_node

		else: # empty heap
			self.head = new_node
			self.min_node = new_node

	def merge(self, other):
		if self.head is None:
			self.head = other.head
			return
		elif other.head is None:
			return

		self.min_node = min(self.min_node, other.min_node)
		self.head = self.__merge_lls(self.head, other.head)

		other.head = None
		other.min_node = None


	def __link(self, node1, node2): # Assuming node1 and node2 are roots.
		node2.parent = node1
		node2.mark = False
		node1.rank += 1
		if node1.child:
			head = node1.child
			tail = head.left
			self.__attach(node2, head)
			self.__attach(tail, node2)

		else:
			node1.child = node2

	def __root_list_generator(self):
		if self.head is None: return
		cur_node = self.head.right

		while cur_node is not self.head:
			yield cur_node.left
			cur_node = cur_node.right

		yield cur_node.left


	def print_heap(self):
		print("head and minnode", self.head, self.min_node)
		for root in self.__root_list_generator():
			#print(root, '(', root.left, root.right, root.child,')')
			root.print_tree()
		print()

	def __remove_node(self, node):
		# Caution: Updating min_node is not this method's concern
		# Assumes node is not None.
		if node is node.right: # If heap only has one node right now.
			self.head = None
			return

		if self.head is node: # If the head is the node to be popped.
			self.head = self.head.right

		self.__attach(node.left, node.right)
		node.left, node.right = node, node

	def __consolidate(self):		
		self.degree_tree_map = defaultdict(lambda: None)

		def merging_trees(cur_root):
			other_root = self.degree_tree_map[cur_root.rank]
			#print(other_root)#

			if other_root is None:
				self.degree_tree_map[cur_root.rank] = cur_root
				return
			else:
				self.degree_tree_map[cur_root.rank] = None
				if cur_root <= other_root:
					self.__remove_node(other_root)
					self.__link(cur_root, other_root) 
					combined_root = cur_root
				else:
					self.__remove_node(cur_root)
					self.__link(other_root, cur_root) 
					combined_root = other_root

				merging_trees(combined_root)

		self.min_node = self.head

		for cur_root in self.__root_list_generator():
			# print(cur_root, self.head, end=" ")
		
			if cur_root < self.min_node:
				self.min_node = cur_root

			merging_trees(cur_root)


	def __attach(self, node1, node2):
		# Connecting node 1 and node 2 such that node 2 is at node 1's right side
		node1.right = node2
		node2.left = node1

	def __merge_lls(self, head_one, head_two, teststr = ""):
		# Merging two circular doubly linked lists and returning the new head.
		tail_one, tail_two = head_one.left, head_two.left
		self.__attach(tail_one, head_two)
		self.__attach(tail_two, head_one)
		if teststr != "silent": self.print_heap()
		return head_one

	def extract_min(self):
		if not self.head: 
			raise IndexError("Popping from an empty heap.")

		node_to_be_popped = self.min_node
		if node_to_be_popped.child: 
			# If the node to be popped has any children,
			# Add them to the root list.
			self.__merge_lls(self.head, node_to_be_popped.child)

		if teststr == "loud": self.print_heap()#

		if node_to_be_popped is self.head: self.head = self.head.right # Test this. 
		self.__remove_node(node_to_be_popped)
		self.__consolidate()

		return node_to_be_popped.ele
		
def not_extract_min_test(mylist):
	heap = FibHeap()
	
	for i in mylist:
		heap.insert(i)
	print("After all insertions:")
	heap.print_heap()#

	for x in range(len(mylist)):
		print(f"After {x + 1}th extraction:")
		heap.extract_min()
		heap.print_heap()

def extract_min_test(mylist):
	heap = FibHeap()
	
	for i in mylist:
		heap.insert(i)
	#print("After all insertions:")
	#heap.print_heap()#

	for x in range(4):
	#	print(f"After {x + 1}th extraction:")
		heap.extract_min("silent")
	#print("after 4th ex")
	#heap.print_heap()
	print("during 5th ex")
	heap.extract_min("loud")
	print("after 5th ex")
	heap.print_heap()
	#heap.extract_min()
"""
After 4th extraction:
head and minnode 4 4
4
    7
    4
        4
    8
        8
        9
            10
"""

extract_min_test_1 = lambda: extract_min_test([1, 2])
extract_min_test_2 = lambda: extract_min_test([1, 2, 3, 4])
extract_min_test_3 = lambda: extract_min_test([10, 20, 30, 40, 50, 60, 70, 80])
extract_min_test_4 = lambda: extract_min_test([8, 8, 2, 4, 1, 4, 2, 9, 10, 4, 2, 7])

extract_min_test_4()

def _FibHeap__remove_node_test_1():
	heap = FibHeap()
	for i in [1]:
		heap.insert(i)
	heap._FibHeap__remove_node(heap.head)
	print(heap.head, heap.min_node)
	assert heap.head is None

	heap = FibHeap()
	for i in [1, 2]:
		heap.insert(i)
	heap._FibHeap__remove_node(heap.head.right)
	print(heap.head, heap.min_node, heap.head.right, heap.head.left)

	heap = FibHeap()
	for i in [1, 2]:
		heap.insert(i)
	heap._FibHeap__remove_node(heap.head.left)
	print(heap.head, heap.min_node, heap.head.right, heap.head.left)

	heap = FibHeap()
	for i in [1, 2]:
		heap.insert(i)
	heap._FibHeap__remove_node(heap.head)
	print(heap.head, heap.min_node, heap.head.right, heap.head.left)

def _FibHeap__remove_node_test_2():
	heap = FibHeap()
	mylist = [5, 3, 1, 7]
	for i in mylist: heap.insert(i)
	for j in range(len(mylist)):
		heap._FibHeap__remove_node(heap.head)
		heap.print_heap()

def _FibHeap__remove_node_test_3():
	heap = FibHeap()
	mylist = [5, 3, 1, 7]
	for i in mylist: heap.insert(i)
	for j in range(len(mylist)):
		heap._FibHeap__remove_node(heap.head.right)
		print(f"After {j+1}th removal:")
		heap.print_heap()

def _FibHeap__remove_node_test_4():
	heap = FibHeap()
	mylist = [5, 3, 1, 7]
	for i in mylist: heap.insert(i)
	for j in range(len(mylist)):
		heap._FibHeap__remove_node(heap.head.left)
		print(f"After {j+1}th removal:")
		heap.print_heap()

def _FibHeap__remove_node_test_5():
	heap = FibHeap()
	mylist = None
	def revert_to_initial():
		nonlocal mylist, heap
		mylist = [5, 3, 1, 7]
		heap = FibHeap()
		for i in mylist: heap.insert(i)

	revert_to_initial()
	heap._FibHeap__remove_node(heap.head.right.right)
	print("New case: ")
	heap.print_heap()

	revert_to_initial()
	heap._FibHeap__remove_node(heap.head)#.right.left)
	print("New case: ")
	heap.print_heap()
	
	revert_to_initial()
	heap._FibHeap__remove_node(heap.head.left.left)
	print("New case: ")
	heap.print_heap()

	revert_to_initial()
	heap._FibHeap__remove_node(heap.head)
	heap._FibHeap__remove_node(heap.head.right)
	heap._FibHeap__remove_node(heap.head.left)
	print("New case: ")
	heap.print_heap()
	
def insert_test_1():
	heap = FibHeap()
	for i in [8, 9, 4, 2, 1]:
		heap.insert(i)
		print(f"Minimum = {heap.min_node}")
		heap.print_heap()

def merge_test_1():
	heap = FibHeap()
	for i in [8, 9, 4, 2, 1]:
		heap.insert(i)

	heap2 = FibHeap()
	for i in [4, 3, 0, 7]:
		heap2.insert(i)

	heap.merge(heap2)
	print("min = ", heap.min_node)
	heap.print_heap()
	print("min = ", heap2.min_node)
	heap2.print_heap()

def merge_test_2():
	heap = FibHeap()
	for i in [8, 9, 4, 2, 1]:
		heap.insert(i)

	heap2 = FibHeap()
	for i in [4, 3, 0, 7]:
		heap2.insert(i)

	heap2.merge(heap)
	print("min = ", heap.min_node)
	heap.print_heap()
	print("min = ", heap2.min_node)
	heap2.print_heap()





"""

	def __consolidate(self):
		self.degree_tree_map = defaultdict(lambda: None)

		self.min_node = self.head
		for cur_root in self.__root_list_generator():
			if cur_root < self.min_node:
				self.min_node = cur_root

			other_root = self.degree_tree_map[cur_root.rank]
			if other_root is None:
				self.degree_tree_map[cur_root.rank] = cur_root
			else:
				self.degree_tree_map[cur_root.rank] = None
				if cur_root <= other_root:
					self.__remove_node(other_root)
					self.__link(cur_root, other_root) 
					combined_root = cur_root
				else:
					self.__remove_node(cur_root)
					self.__link(other_root, cur_root) 
					combined_root = other_root

				self.degree_tree_map[combined_root.rank] = combined_root
"""
