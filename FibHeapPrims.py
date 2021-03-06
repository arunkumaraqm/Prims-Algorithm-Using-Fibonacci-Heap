# Prims using adjacency lists and Fib heap.

from FibHeap import FibHeapForPrims
from Graph import Graph

def prims_mst(grf):
	precursor = [None] * grf.nfverts
	visited = set()

	src = 0
	heap = FibHeapForPrims(grf.nfverts)

	for _ in range(grf.nfverts):
		u = heap.extract_min()
		#print("After extraction: \n"); heap.print_heap()
		visited.add(u)

		for v, cur_key in grf.graph[u].items():
			if v not in visited and cur_key < heap.fetch_key(v):
				heap.decrease_key(v, cur_key) 
				#print(f"After decrease_key on {v}: \n"); heap.print_heap()
				precursor[v] = u

	return precursor

