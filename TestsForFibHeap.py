from FibHeap import *

# Some __methods have been since renamed _methods; so you'll need to change that here too.

class DKTests_FibHeap(FibHeap):
	def insert(self, new_ele):
		# Inserting the newnode at the end of the root list.
		new_node = FibHeapNode(new_ele)
		self._FibHeap__insert_node(new_node)
		return new_node


def print_details(mylist):
	for node in mylist:
		print(node, node.parent, node.left, node.right, node.child, node.rank, node.mark)

def decrease_key_test_1():
	heap = DKTests_FibHeap()
	
	addrs = [heap.insert(i) for i in [20]]
	heap.print_heap()

	try:
		heap.decrease_key(addrs[0], 30)
	except ValueError as err:
		print(err)

	heap.decrease_key(addrs[0], 19)
		
	heap.print_heap()


def decrease_key_test_2():
	heap = DKTests_FibHeap()
	
	addrs = [heap.insert(i) for i in [40, 12, 18]]
	heap.print_heap()

	heap.decrease_key(addrs[0], 20)
	heap.print_heap()
	heap.decrease_key(addrs[2], 11)
	heap.print_heap()

def decrease_key_test_3():
	heap = DKTests_FibHeap()
	
	addrs = [heap.insert(i) for i in [40, 12, 10]]
	heap.extract_min()
	heap.print_heap()

	heap.decrease_key(addrs[0], 20)
	heap.print_heap()
	heap.decrease_key(addrs[0], 11)
	heap.print_heap()

def decrease_key_test_4():
	heap = DKTests_FibHeap()
	
	addrs = [heap.insert(i) for i in [0, 30, 10, 20, 25]]
	heap.extract_min()
	heap.print_heap()
	heap.decrease_key(addrs[4], -INFINITY)
	heap.extract_min()
	heap.print_heap()
	# Heap looks like (10(20, 30)) now.

	heap.decrease_key(addrs[3], -20)
	heap.print_heap()
	print_details(addrs)

decrease_key_test_4()

def decrease_key_test_5():
	heap = DKTests_FibHeap()
	
	addrs = [heap.insert(i) for i in [0, 30, 10, 20, 25]]
	print(addrs)
	heap.extract_min()
	heap.decrease_key(addrs[4], -INFINITY)
	heap.extract_min()
	heap.print_heap()
	
	addrs += [heap.insert(j) for j in [40, 70, 50, 1]]
	heap.extract_min()
	heap.print_heap()

	heap.decrease_key(addrs[3], 5)
	heap.print_heap()
	heap.decrease_key(addrs[1], 5)
	heap.print_heap()
	heap.extract_min()
	heap.print_heap()

def decrease_key_test_6():
	heap = DKTests_FibHeap()
	
	addrs = [heap.insert(i) for i in [0, 30, 10, 20, 25]]
	print(addrs)
	heap.extract_min()
	heap.decrease_key(addrs[4], -INFINITY)
	heap.extract_min()	
	addrs += [heap.insert(j) for j in [40, 70, 50, 1]]
	heap.extract_min()
	heap.print_heap()

	heap.decrease_key(addrs[2], -10)
	heap.print_heap()
	heap.decrease_key(addrs[1], -30)
	heap.print_heap()
	print_details(addrs)

def decrease_key_test_7():
	# Testing whether cascade cut works
	heap = DKTests_FibHeap()
	
	"""
	(0, 28), (1, 60), (2, -8), (3, -6), (4, -15), (5, -36), 
	(6, 46), (7, 34), (8, -7), (9, 5), (10, -54), (11, -18), 
	(12, -18), (13, 50), (14, 51), (15, -19), (16, -44), 
	(17, -24), (18, 23), (19, 10),
	"""

	mylist = [28, 60, -8, -6, -15, -36, 46, 34, -7, 5, -27\
	         -27, -18, -18, 50, 51, -19, -44, -24, 23, 10]
	addrs = [heap.insert(i) for i in mylist]

	def deckey(ind):
		print(f"Decreasing {addrs[ind].ele} to {addrs[ind].ele - 50}.")
		heap.decrease_key(addrs[ind], addrs[ind].ele - 50)
		heap.print_heap()
		#input()

	heap.extract_min()
	heap.print_heap()
	deckey(4)
	deckey(3)
	deckey(1)
	deckey(0)
	heap.extract_min()
	heap.print_heap()

def extract_min_test(mylist):
	heap = FibHeap()
	
	for i in mylist:
		heap.insert(i)
	print("After all insertions:")
	heap.print_heap()#

	for x in range(len(mylist)):
		print(f"After {x + 1}th extraction:")
		heap.extract_min()
		heap.print_heap()

	try: heap.extract_min()
	except IndexError as err:
		if str(err) == "Popping from an empty heap.":
			pass
		else: raise IndexError(err)

extract_min_test_1 = lambda: extract_min_test([1, 2])
extract_min_test_2 = lambda: extract_min_test([1, 2, 3, 4])
extract_min_test_3 = lambda: extract_min_test([10, 20, 30, 40, 50, 60, 70, 80])
extract_min_test_4 = lambda: extract_min_test([8, 8, 2, 4, 1, 4, 2, 9, 10, 4, 2, 7])
extract_min_test_5 = lambda: extract_min_test([10])
extract_min_test_6 = lambda: extract_min_test([20, 10, 40, 28, 46, 10, 35, 26, 83, 18, 32, 46])
extract_min_test_7 = lambda: extract_min_test([])

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



