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
