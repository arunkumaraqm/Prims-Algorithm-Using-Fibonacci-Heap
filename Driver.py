import sys
from time import perf_counter as time
from Graph import Graph, compute_mst_and_cost
from LazyNaivePrims import prims_mst as lazy_naive_prims
from EagerNaivePrims import prims_mst as eager_naive_prims
from BinaryHeapPrims import prims_mst as binary_heap_prims
from FibHeapPrims import prims_mst as fib_heap_prims
from VisualizeMst import visualize

def read(grf):

	# Checking if input file is specified as command line argument.
	try:
		fname = sys.argv[1] 
	except IndexError:
		fname = None

	try:
		# Read input file if available otherwise read from stdin.
		with open(fname) if fname else sys.stdin as input_file:
			grf.read_from_file(input_file)
			
	except OSError:
		print("File not found. \nNote: For paths, use forward slash and enclose in double quotes.")
		exit()

def main():
	grf = Graph(representation = "matrix")
	read(grf)
	adj_mat = grf.change_representation()

	prims = [lazy_naive_prims, eager_naive_prims, binary_heap_prims, fib_heap_prims][2]
	representation = {lazy_naive_prims: "matrix", 
					  eager_naive_prims: "matrix",
					  binary_heap_prims: "lists",
					  fib_heap_prims: "lists"} [prims]

	start = time()
	precursor = prims(grf)
	end = time()

	mst, cost = compute_mst_and_cost(precursor, grf)

	print(f"Cost = {cost}")
	print(f"Duration: {(end - start) * 10**(9) : .0f} ns")

	edges_in_mst = [(ind, precursor[ind]) for ind in range(1, grf.nfverts)]
	
	visualize(adj_mat, edges_in_mst)
		
main()