import sys
import os
from time import perf_counter as time
from Graph import Graph, compute_mst_and_cost
from LazyNaivePrims import prims_mst as lazy_naive_prims
from EagerNaivePrims import prims_mst as eager_naive_prims
from BinaryHeapPrims import prims_mst as binary_heap_prims
from FibHeapPrims import prims_mst as fib_heap_prims
from VisualizeMst import visualize

choices = {"l": "lazy_naive_prims", 
           "e": "eager_naive_prims", 
           "b": "binary_heap_prims", 
           "f": "fib_heap_prims"}

representation_for_choice = {lazy_naive_prims: "matrix", 
				 			 eager_naive_prims: "matrix",
				  			 binary_heap_prims: "lists",
				  			 fib_heap_prims: "lists"} 

def read_graph(grf):

	# Checking if input file is specified as command line argument.
	try:
		fname = sys.argv[1] 
		print(f"You have chosen the test file \"{fname}\"")
	except IndexError:
		fname = input("Enter test file name: ")

	try:
		with open(fname) as input_file:
			grf.read_from_file(input_file)
			
	except OSError:
		print("File not found. \nNote: For paths, use forward slash and enclose in double quotes.")
		exit()

def read_choices():
	implementation_choice = input("\nWhich implementation(s)? \nlazy_naive, eager_naive, binary_heap, or fib_heap \nEnter: ")
	display_choice = int(input("\nHow to display MST? \n1. None \n2. Adjacency Matrix \n3. Graph Visualization \nEnter: "))
	print()
	return implementation_choice, display_choice

def implement(implementation_choice, grf):	
	for choice in implementation_choice:
		prims_str = choices[choice]
		prims = eval(prims_str)

		if representation_for_choice[prims] == 'lists':
			grf.matrix_to_lists()
		else:
			grf.lists_to_matrix()

		start = time()
		precursor = prims(grf)
		end = time()

		print("Duration for " + f"{prims_str}: ".ljust(20) + f"{(end - start) * 10**(9) : .0f} ns".rjust(20))
	print()
	return precursor

def display_mst(display_choice, grf, adj_mat, precursor, mst, cost):

	print(f"Cost of MST = {cost}")

	if display_choice == 1:
		pass

	elif display_choice == 2:
		if grf.nfverts > 20:
			yn = input("Graph is too large. \nAre you sure you want to see the adjacency matrix of MST? ").lower()
			if yn == 'yes' or yn == 'y':
				print("Adjacency Matrix for MST: ")
				print(mst)
		else:
			print("Adjacency Matrix for MST: ")
			print(mst)

	elif display_choice == 3:
		if grf.nfverts > 15:
			print("Graph is too large to display!")
		elif grf.nfverts > 10:
			print("Stripping edge weights for clearer graph.")
			edges_in_mst = [(ind, precursor[ind]) for ind in range(1, grf.nfverts)]
			visualize(adj_mat, edges_in_mst, strip_edge_weights = True)
		else:
			edges_in_mst = [(ind, precursor[ind]) for ind in range(1, grf.nfverts)]
			visualize(adj_mat, edges_in_mst)

def main():
	grf = Graph(representation = "matrix")
	os.system("clear")
	read_graph(grf)
	adj_mat = grf.graph

	implementation_choice, display_choice = read_choices()	
	precursor = implement(implementation_choice, grf)
	mst, cost = compute_mst_and_cost(precursor, grf)
	display_mst(display_choice, grf, adj_mat, precursor, mst, cost)

if __name__ == "__main__":
	main()
