from collections import defaultdict
INFINITY = float('inf')

""" For debugging purposes:
teststr = "silent"## Remember to use global when you use this.
def show(something):
	if teststr == "loud": print(something)
def struc(something):
	if teststr == "loud": something.print_heap()
"""

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

		#if teststr == "silent": 
		print(tabwidth*"    ", self.ele, '*' if self.mark else '', sep = "")

		""" Debugging purposes
		elif teststr == "loud":
			print(tabwidth*"    ", end = " ")
			show((self.ele, id(self)))
		#input()#
		"""
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
		self.Node = FibHeapNode

	def merge(self, other):
		if self.head is None:
			self.head = other.head
			return
		elif other.head is None:
			return

		self.min_node = min(self.min_node, other.min_node)
		self.head = self._merge_lls(self.head, other.head)

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
		print(f"### head = {self.head}, min_node = {self.min_node} ###")
		for root in self.__root_list_generator():
			root.print_tree()
		print()

	def _remove_node(self, node):
		# Caution: Updating min_node is not this method's concern
		# Assumes node is not None.
		if node is node.right: # If heap only has one node right now.
			self.head = None
			return

		if self.head is node: # If the head is the node to be popped.
			self.head = self.head.right

		self.__attach(node.left, node.right)
		node.left, node.right = node, node

	def _consolidate(self):		
		self.degree_tree_map = defaultdict(lambda: None)

		def merging_trees(cur_root):
			other_root = self.degree_tree_map[cur_root.rank]


			if other_root is None:
				self.degree_tree_map[cur_root.rank] = cur_root
				return
			else:
				self.degree_tree_map[cur_root.rank] = None
				if cur_root <= other_root:
					self._remove_node(other_root)
					self.__link(cur_root, other_root) 
					combined_root = cur_root
				else:
					self._remove_node(cur_root)
					self.__link(other_root, cur_root) 
					combined_root = other_root

				merging_trees(combined_root)

		for cur_root in self.__root_list_generator():
			merging_trees(cur_root)

		 # Maybe this can be done earlier.
		try:
			roots_iter = filter(lambda node: node is not None, self.degree_tree_map.values())
			self.min_node = min(roots_iter) 
			"""
			Note: This does not have to be the node of the first_occurence of the minimum ele
			since dictionaries are not ordered by their key.
			This means you could have a node with ele 4 as head and another node with ele 4 as tail
			and self.min_node could point to the latter.
			"""
		except ValueError as err:
			if str(err) == "min() arg is an empty sequence":
				self.min_node = None
			else: 
				raise ValueError(err)

	def __attach(self, node1, node2):
		# Connecting node 1 and node 2 such that node 2 is at node 1's right side
		node1.right = node2
		node2.left = node1

	def _merge_lls(self, head_one, head_two):
		# Merging two circular doubly linked lists and returning the new head.
		tail_one, tail_two = head_one.left, head_two.left
		self.__attach(tail_one, head_two)
		self.__attach(tail_two, head_one)
		return head_one

	def extract_min(self):
		if not self.head: 
			raise IndexError("Popping from an empty heap.")

		node_to_be_popped = self.min_node

		if node_to_be_popped.child: 
			# If the node to be popped has any children,
			# Add them to the root list.
			self._merge_lls(self.head, node_to_be_popped.child)

		self._remove_node(node_to_be_popped)
		# node_to_be_popped has now been popped.

		self._consolidate()

		temp = node_to_be_popped.ele
		node_to_be_popped.ele = None # For later
		return temp

	def __cut(self, node):
		# Assumes node is not None and node.parent is not None.

		#print(f"Cutting {node}")
		if node is node.right: # If cdll only has one node right now.
			node.parent.child = None
			
		else:
			if node.parent.child is node: # If the head is the node to be popped.
				node.parent.child = node.parent.child.right

			self.__attach(node.left, node.right)

			node.left, node.right = node, node
	
		node.parent.rank -= 1
		node.parent = None			

		self.__insert_node(node) 

	def __cascading_cut(self, node):
		#print(f"Cascade Cutting {node}")
		# if node is a root
		if node.parent is None or node.parent.ele is None:
			pass

		else:
			if node.mark:
				parent = node.parent
				self.__cut(node)
				self.__cascading_cut(parent)
			else:
				node.mark = True

	def decrease_key(self, node, new_ele):
		if node.ele < new_ele:
			raise ValueError("new_ele is greater than node's current ele.")

		node.ele = new_ele

		"""
		We don't have to change the position of node if 
		node is a root or if decrease key doesn't violate heap property.

		A node is in the root list because
		(i) It was inserted and an extract min hasn't occured since.
		(ii) It was inserted and when the extract min occured, it became a root of a tree.
		(iii) It was cut from its parent during decrease_key.
		(iv) It was on the first level and its parent was extracted, causing it to be added to the root list.

		For cases (i) and (ii), node.parent would be None.
		For case (iii), decrease_key's __cut clears node.parent
		For case (iv), node.parent.ele is set to infinity after extraction, 
		meaning node.ele would be lesser than node.parent.ele.
		"""
		if node.parent is None or node.parent.ele is None:
			if self.min_node > node:
				self.min_node = node
			return

		elif node >= node.parent:
			pass
		else:
			parent = node.parent
			self.__cut(node)
			self.__cascading_cut(parent)

	def __insert_node(self, new_node):
		
		if self.head:
			self._merge_lls(self.head, new_node)

			if new_node < self.min_node: self.min_node = new_node

		else: # empty heap
			self.head = new_node
			self.min_node = new_node

	def insert(self, new_ele):
		# Inserting the newnode at the end of the root list.
		new_node = self.Node(new_ele)
		self.__insert_node(new_node)

class FibHeapNodeForPrims(FibHeapNode):
	def __init__(self, vertex, ele):
		super().__init__(ele)
		self.vertex = vertex

	def __str__(self):
		return str((self.vertex, self.ele))

	def print_tree(self, tabwidth = 0):
		"""
		Tabbed display of nodes
		No. of tabs = level at which that node is
		An asterisk after the value indicates that this node is marked
		"""

		#if teststr == "silent": 
		print(tabwidth*"    ", self.vertex, ':', self.ele, '*' if self.mark else '', sep = "")

		""" Debugging purposes
		elif teststr == "loud":
			print(tabwidth*"    ", end = " ")
			show((self.ele, id(self)))
		#input()#
		"""
		for childtree in self.children_generator():
			childtree.print_tree(tabwidth + 1)



class FibHeapForPrims(FibHeap):
	def __init__(self, nfverts): # Assumes nfverts is a natural no.
		
		# Every node needs to contain a vertex field.
		self.Node = FibHeapNodeForPrims

		src = 0 

		# vertex_heapnode_map is implemented using a list instead of a dict
		# because vertices are labeled from 0 to nfverts - 1 anyway.
		self.vertex_heapnode_map = []

		head = self.Node(src, 0)
		tail = head
		self.vertex_heapnode_map.append(head)

		for vx in range(1, nfverts):
			node = self.Node(vx, INFINITY)
			self.vertex_heapnode_map.append(node)
			
			tail.right = node
			node.left = tail
			tail = node

		tail.right = head
		head.left = tail

		self.head = self.min_node = head

	def extract_min(self):
		if not self.head: 
			raise IndexError("Popping from an empty heap.")

		node_to_be_popped = self.min_node

		if node_to_be_popped.child: 
			# If the node to be popped has any children,
			# Add them to the root list.
			self._merge_lls(self.head, node_to_be_popped.child)

		self._remove_node(node_to_be_popped)
		# node_to_be_popped has now been popped.

		self._consolidate()

		node_to_be_popped.ele = None # For later
		return node_to_be_popped.vertex


	def decrease_key(self, vertex, new_key):
		# Decreases the key for a given vertex to new_key.

		node = self.vertex_heapnode_map[vertex]
		super().decrease_key(node, new_key)

	def fetch_key(self, vertex):
		return self.vertex_heapnode_map[vertex].ele
