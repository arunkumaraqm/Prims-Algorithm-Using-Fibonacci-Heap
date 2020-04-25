from Graph import Graph
from LazyNaivePrims import prims_mst as lazy_naive_prims
from EagerNaivePrims import prims_mst as eager_naive_prims
from BinaryHeapPrims import prims_mst as binary_heap_prims


def compute_mst_and_cost(precursor, grf):
	"""
	Makes the adjacency matrix of the minimum spanning tree,
	returns that graph and also returns the total cost of the MST.
	"""
	
	mst = Graph(grf.nfverts, representation = "matrix")
	mst.fill_with_zeros()
	cost = 0

	# precursor[0] is useless.
	for cur, parent in enumerate(precursor[1:], 1):
		#print(f"(cur, par) = ({cur, parent})")
		mst.graph[parent][cur] = grf.graph[parent][cur]
		cost += grf.graph[parent][cur]
	
	return mst, cost

def main():
	prims = [lazy_naive_prims, eager_naive_prims, binary_heap_prims][1]
	representation = {lazy_naive_prims: "matrix", 
					  eager_naive_prims: "matrix",
					  binary_heap_prims: "lists"} [prims]

	nfverts = int(input())
	grf = Graph(nfverts, representation)
	grf.read_from_stdin()
	
	precursor = prims(grf)
	mst, cost = compute_mst_and_cost(precursor, grf)
	
	print(mst)
	print(f"Cost = {cost}")

main()