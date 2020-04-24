from BinaryHeapStandard import MinHeap, heapsort

# Tests for heapsort
def heapsort_test_1():
	print(heapsort([]))
def heapsort_test_2():
	print(heapsort([0]))
def heapsort_test_3():
	print(heapsort([3, 2]))
def heapsort_test_4():
	print(heapsort([4, 2, 8, 3, 6, 1, 6, 3, 6, 30, 20, 10, -5, 7, 3]))
def heapsort_test_5():
	print(heapsort([3, 5, 7, 9]))
def heapsort_test_6():
	print(heapsort([9, 7, 5, 3]))

def heapsort_test_runner():
	for testno in range(1, 6 + 1):
		eval("heapsort_test_" + str(testno))()
		print()
heapsort_test_runner()

# Tests for extract_min:
def extract_min_test_1():
	heap = MinHeap([10, 20, 25, 22, 30, 25, 28], already_heap = True)
	print(f"Original: {heap}")
	for i in range(1, 8):
		print(heap.extract_min(), heap)

def extract_min_test_2():
	heap = MinHeap([90, 90, 90], already_heap = True)
	print(f"Original: {heap}")
	for i in range(3):
		print(heap.extract_min(), heap)

def extract_min_test_3():
	heap = MinHeap([], already_heap = True)
	for i in range(3):
		print(heap.extract_min(), heap)

def extract_min_test_runner():
	for testno in range(1, 3 + 1):
		eval("extract_min_test_" + str(testno))()
		print()
extract_min_test_runner()

#Tests for decrease_key:

def decrease_key_test_1():
	heap = MinHeap([10, 20, 25, 22, 30, 25, 28], already_heap = True)
	for i in range(7):
		heap.decrease_key(i, heap.arr[i] - 1)
	print(heap)

def decrease_key_test_2():
	heap = MinHeap([10, 20, 25, 22, 30, 25, 28], already_heap = True)
	heap.decrease_key(6, 0)
	print(heap)

def decrease_key_test_3():
	heap = MinHeap([10, 20, 25, 22, 30, 25, 28], already_heap = True)
	heap.decrease_key(0, 11) # Supposed to throw an error
	print(heap)

def decrease_key_test_runner():
	for testno in range(1, 3 + 1):
		eval("decrease_key_test_" + str(testno))()
		print()
decrease_key_test_runner()

#Tests for insert:

def insert_test_1():
	heap = MinHeap()
	for i in [60, 20, 10, 70, 35, 24]:
		heap.insert(i)
		print(heap)

def insert_test_2():
	heap = MinHeap([10, 20, 30, 40, 50])
	for i in [40, 30, 20, 10]:
		heap.insert(i)
		print(heap)

def insert_test_runner():
	for testno in range(1, 2 + 1):
		eval("insert_test_" + str(testno))()
		print()
insert_test_runner()


#Tests for build_heap:
def build_heap_test_1():
	heap = MinHeap([60, 20, 10, 70, 35, 24])
	print(heap)

def build_heap_test_2():
	heap = MinHeap()
	heap.build_heap([10, 20, 30, 40, 50, 40, 30, 20, 10])
	print(heap)

def build_heap_test_runner():
	for testno in range(1, 2 + 1):
		eval("build_heap_test_" + str(testno))()
		print()
build_heap_test_runner()

#Tests for sift_up:
def sift_up_test_1():
	heap = MinHeap([10, 20, 25, 22, 30, 25, 28], already_heap = True)
	print(f"Original: {heap}")
	for i in range(7):
		heap.sift_up(i)
		print(heap) # No change expected

def sift_up_test_2():
	heap = MinHeap([10, 20, 25, 22, 30, 25, 18], already_heap = True)
	print(f"Original: {heap}")
	heap.sift_up(6)
	print(heap)

def sift_up_test_3():
	heap = MinHeap([10, 20, 25, 22, 30, 25, 9], already_heap = True)
	print(f"Original: {heap}")
	heap.sift_up(6)
	print(heap)

def sift_up_test_4():
	heap = MinHeap([10, 20, 25, 18, 19, 25, 28], already_heap = True)
	print(f"Original: {heap}")
	heap.sift_up(4)
	heap.sift_up(3)
	print(heap)

def sift_up_test_runner():
	for testno in range(1, 4 + 1):
		eval("sift_up_test_" + str(testno))()
		print()

sift_up_test_runner()


#Tests for sift_down:
def sift_down_test_1():
	heap = MinHeap([10, 20, 25, 22, 30, 25, 28], already_heap = True)
	print(f"Original: {heap}")
	for i in range(len(heap)):
		heap.sift_down(i)
		print(heap) # No changes should occur.

def sift_down_test_2():
	heap = MinHeap([10, 20, 25, 22, 30, 25, 18], already_heap = True)
	print(f"Original: {heap}")
	heap.sift_down(2)
	print(heap)

def sift_down_test_3():
	heap = MinHeap([10, 20, 25, 12, 30, 25, 28], already_heap = True)
	print(f"Original: {heap}")
	heap.sift_down(1)
	print(heap)

def sift_down_test_4():
	heap = MinHeap([70, 20, 25, 22, 30, 25, 28], already_heap = True)
	print(f"Original: {heap}")
	heap.sift_down(0)
	print(heap)

def sift_down_test_runner():
	for testno in range(1, 4 + 1):
		eval("sift_down_test_" + str(testno))()
		print()
sift_down_test_runner()
