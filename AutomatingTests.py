import sys
from time import perf_counter as time
from Graph import Graph, compute_mst_and_cost
from LazyNaivePrims import prims_mst as lazy_naive_prims
from EagerNaivePrims import prims_mst as eager_naive_prims
from BinaryHeapPrims import prims_mst as binary_heap_prims
from FibHeapPrims import prims_mst as fib_heap_prims
from VisualizeMst import visualize
import pandas as pd

choices = {"l": "lazy_naive_prims", 
           "e": "eager_naive_prims", 
           "b": "binary_heap_prims", 
           "f": "fib_heap_prims"}

representation_for_choice = {lazy_naive_prims: "matrix", 
				 			 eager_naive_prims: "matrix",
				  			 binary_heap_prims: "lists",
				  			 fib_heap_prims: "lists"} 

def read_graph(grf, fname):
	try:
		with open(fname) as input_file:
			grf.read_from_file(input_file)
			
	except OSError:
		print("File not found. \nNote: For paths, use forward slash and enclose in double quotes.")
		exit()

def generate_tests():
	from GraphGeneration import automated_tests
	limit = 999
	for density in [1, 2, 3]:
		lowest_nfverts = 2100
		highest_nfverts = 3500
		step = 100
		for nfverts in range(lowest_nfverts, highest_nfverts + 1, step):
			automated_tests(nfverts, density, limit)
			print(f"Completed {nfverts, density, limit}.")

def implement(implementation_choice, grf):	
	duration = {'l': None, 'e': None, 'b': None, 'f': None}

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

		duration[choice] = int((end - start) * 10**(9))

	return duration

def run_all_prims(fname):
	grf = Graph(representation = "matrix")
	read_graph(grf, fname)
	duration = implement("bf", grf)
	return duration


def time_tests():
	limit = 999
	for density in [1, 2, 3]:
		mylist = []
		for lowest_nfverts, highest_nfverts, step in [(10, 200, 10)]:
			for nfverts in range(lowest_nfverts, highest_nfverts + 1, step):
				fname = f"Tests/Mode {density}/Graph Test ({nfverts}, {density}, {limit}).txt"
				duration = run_all_prims(fname)
				print(f"{fname} complete.")
				mylist.append({'nfverts': nfverts,
						   'l_duration': duration['l'],
						   'e_duration': duration['e'],
						   'b_duration': duration['b'],
						   'f_duration': duration['f']})
		df = pd.DataFrame(mylist, columns = ['nfverts', 'l_duration', 'e_duration', 'b_duration', 'f_duration'])
		df.to_csv(f"Tests/Durations ((10, 200, 10), {density}, 999) (1).csv")


def foo():
	fname = "Tests/Graph Test (10000, 3, 999).txt"
	duration = run_all_prims(fname)
	print(duration)
foo()
