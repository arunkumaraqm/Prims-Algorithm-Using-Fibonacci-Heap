# Reference: https://code.activestate.com/recipes/511508-binomial-queues/

class BinomialTree:
	def __init__(self, value):
		self.value = value
		self.rank = 0
		self.children = [] # List of binomial trees

	def add_child(self, childtree): 
	# childtree will have the same rank as self
	# childtree will maintain heap property 
		self.children.append(childtree)
		self.rank += 1

	def display(self, tabwidth = 0):
		print(tabwidth*"    ", self.value, sep = "")
		for childtree in self.children:
			childtree.display(tabwidth + 1)

class BinomialHeap:
	def __init__(self, trees = None):
		if trees == None: trees = []
		elif trees[-1] != None: trees.append(None) 
		# The trees list should always end with a NoneType object
		# (Refer to add_tree method for reason) 
		# except if the trees list is empty in which case it wouldn't matter.
		# (pad_upto will take care of that)

		self.trees = trees # List of binomial trees

	def pad_upto(self, newrank):
		"If newrank exceeds the largest rank in the heap,\
		then pad the trees array with None until and including newrank."
		
		rank_of_largest_tree = len(self.trees) - 1
		i = rank_of_largest_tree
		while i <= newrank:
			self.trees.append(None)
			i += 1

	def link(self, one: BinomialTree, two: BinomialTree):
		"Combining two trees of the same rank"

		if one.value > two.value:
			one, two = two, one # swap
		one.add_child(two) # rank of one is incremented within
		return one 

	def add_tree(self, newtree):
		self.pad_upto(newtree.rank) # otherwise IndexError will be raised
		while self.trees[newtree.rank] is not None:
			rank = newtree.rank
			oldtree = self.trees[rank]
			newtree = self.link(oldtree, newtree) # rank is incremented within
			self.trees[rank] = None
		self.trees[newtree.rank] = newtree

		# Let's take the case where the bino heap is 111. If you add
		# a 0-deg tree, it becomes 1000. If tree[-1] is not None, then an 
		# IndexError will be raised when you try that.
		if self.trees[-1] != None: self.trees.append(None)

	def meld(self, other):
		"Merges two BinomialHeaps into self.\
		 Also clears other so that those BinomialTrees \
		 cannot be accessed using other."

		assert self is not other, "You cannot meld a heap with itself."
		for ind, tree in enumerate(other.trees):
			if tree: 
				self.add_tree(tree) 
		other.trees = []

	def insert(self, ele):
		newtree = BinomialTree(ele)
		self.add_tree(newtree)

	def find_min(self):
		"Returns value of min root if there is at least one root,\
		 else returns None"
		
		minn = float('inf')
		for tree in self.trees:
			try: minn = min(tree.value, minn)
			except AttributeError: continue
		return minn if minn != float('inf') else None

	def __find_min_ind(self):
		"Returns index of min root if there is at least one root,\
		 else returns None"

		minn = float('inf')
		minind = None
		for ind, tree in enumerate(self.trees):
			try: 
				if minn > tree.value:
					minn = tree.value
					minind = ind
			except AttributeError: continue
		return minind if minn != float('inf') else None

	def extract_min(self):
		"Removes min root and adds its children to the BinomialHeap"
		
		min_ind = self.__find_min_ind()
		if min_ind == None: return None
		
		tree = self.trees[min_ind]
		minn = tree.value
		newheap = BinomialHeap(trees = tree.children + [None])

		self.trees[min_ind] = None
		# Ensuring there is exactly one NoneType object at the end.
		rank_of_largest_tree = len(self.trees) - 1
		if min_ind == rank_of_largest_tree: self.trees.pop()

		self.meld(newheap)
		return minn		

	def display(self):
		"Displays heap in tabbed fashion."

		for tree in self.trees:
			try: tree.display()
			except AttributeError: print(None)

	def binary(self):
		"Returns representation of the binomial heap as a binary number"
		if len(self.trees) == 0: return ""
		binary_rep = ""
		for tree in self.trees[:-1]:
			if tree:
				binary_rep += "1"
			else: binary_rep += "0"
		binary_rep = binary_rep[::-1]
		return binary_rep


# Tests for extract min 
def test9():
	mylist = [67, 89, 32, 12, 34, 67, 94]
	ah = BinomialHeap()
	for ele in mylist: ah.insert(ele)
	ah.display(); input()

	for i in range(7):
		minn = ah.extract_min()
		print("Minimum : {}".format(minn))
		ah.display(); input()
test9()

# Tests for meld
def test8():
	ah = BinomialHeap([78, None])
	ah.meld(ah) # Should raise Assertion error

def test7():
	ah = BinomialHeap()
	for ele in []:
		ah.insert(ele)
	
	print("First bino heap:")
	ah.display()
	print("------")
		
	bh = BinomialHeap()
	for ele in [20]:
		bh.insert(ele)
	
	print("Second bino heap:")
	bh.display()
	print("------")
		
	print("Result after melding")
	ah.meld(bh)
	ah.display()

def test6():
	ah = BinomialHeap()
	for ele in [67, 89, 32, 12, 34, 67, 94]:
		ah.insert(ele)
	
	print("First bino heap:")
	ah.display()
	print("------")
		
	bh = BinomialHeap()
	for ele in [9, 74, 25, 78, 19, 32]:
		bh.insert(ele)
	
	print("Second bino heap:")
	bh.display()
	print("------")
		
	print("Result after melding")
	print("AH: ")
	ah.meld(bh)
	ah.display()
	print("BH: ", end = " ")
	bh.display() # BH should be empty

# Tests for find_min
def test5():
	ah = BinomialHeap()
	print(ah.find_min())
	ah.insert(80)
	print(ah.find_min())

def test4():
	from random import shuffle
	mylist = [67, 89, 32, 12, 34, 67, 94]
	for i in range(5):
		shuffle(mylist)
		ah = BinomialHeap()
		for ele in mylist:
			ah.insert(ele)
		#ah.display()
		print("Min: ", ah.find_min())
# Tests for insert
def test3():
	ah = BinomialHeap()
	for ele in [67, 89, 32, 12, 34, 67, 94]:
		ah.insert(ele)
	
	print("First bino heap:")
	ah.display()
	print("------")
		
	bh = BinomialHeap()
	for ele in [9, 74, 25, 78, 19, 32]:
		bh.insert(ele)
	
	print("Second bino heap:")
	bh.display()
	print("------")
		
	print("Result after doing first bino heap += last tree of second bino heap")
	ah.add_tree(bh.trees[-2])
	ah.display()
	# Obviously any changes you make to that last tree of the \
	# second bino heap are reflected on the first bino heap\
	# and vice versa.

def test2():
	from random import randint
	randy = lambda: randint(1, 99)
	ah = BinomialHeap()
	for ele in [46, 58, 66, 42]:
		print("Inserting {}".format(ele))
		ah.insert(ele)
		ah.display()
		input()
	for _ in range(5):
		ele = randy()
		print("Inserting {}".format(ele))
		ah.insert(ele)
		ah.display()
		input()

def test1():
	a = BinomialTree(40)
	b = BinomialTree(50)
	c = BinomialTree(60)
	d = BinomialTree(70)
	a.add_child(c)
	b.add_child(d)
	b.add_child(a)
	b.display()


