# Program to generate a test case (adjacency matrix) for Prim's and Krukal's algorithms
# The graph generated will be connected.

from random import shuffle, sample, randint
import sys

def read():
	nfverts = int(input("Number of vertices: "))
	density = int(input("Density (Medium 1, High 2 or Complete 3): "))
	limit = float(input("Upper limit of edge weight: "))
	limit = int(limit) if int(limit) else limit
	return nfverts, density, limit

def print_mat(nfverts, mat, fname):
	with open(fname, 'w') as fil:
		fil.write(f"{nfverts}\n")

		for i in mat[1:]:
			for j in i[1:]:
				fil.write(f"{j} ")
			fil.write("\n")

def generate_random_spanning_tree(nfverts, mat, rint):
	mylist = list(range(1, nfverts + 1))
	shuffle(mylist)
	visited = [mylist[0]]
	for v in mylist[1:]:
		u = sample(visited, 1)[0] # sample function returns a list
		mat[u][v] = rint()
		mat[v][u] = mat[u][v]
		visited += [v]

def add_some_more_edges(nfverts, mat, probability_distro_func):
	for i in range(1, nfverts + 1 - 1):
		for j in range(i + 1, nfverts + 1):
			if not mat[i][j]:
				mat[i][j] = probability_distro_func()
				mat[j][i] = mat[i][j]
				
if __name__ == "__main__":
	nfverts, density, limit = read()				
	mat = [[0 for i in range(nfverts + 1)] \
	          for j in range(nfverts + 1)]

	rint = lambda: randint(1, limit)
	random_weight_lambdas = {

		# density: random_weight_lambda	
		1: lambda: [rint(), 0, 0][randint(0,2)],
		2: lambda: [rint(), rint(), 0][randint(0,2)],
		3: lambda: [rint(), rint(), rint()][randint(0,2)]
	}
	probability_distro_func = random_weight_lambdas[density]

	generate_random_spanning_tree(nfverts, mat, rint)
	add_some_more_edges(nfverts, mat, probability_distro_func)     

	fname = f"Tests/Graph Test ({nfverts}, {density}, {limit}).txt"  
	print_mat(nfverts, mat, fname)
	
def automated_tests(nfverts, density, limit):		
	mat = [[0 for i in range(nfverts + 1)] \
	          for j in range(nfverts + 1)]

	rint = lambda: randint(1, limit)
	random_weight_lambdas = {

		# density: random_weight_lambda	
		1: lambda: [rint(), 0, 0][randint(0,2)],
		2: lambda: [rint(), rint(), 0][randint(0,2)],
		3: lambda: [rint(), rint(), rint()][randint(0,2)]
	}
	probability_distro_func = random_weight_lambdas[density]

	generate_random_spanning_tree(nfverts, mat, rint)
	add_some_more_edges(nfverts, mat, probability_distro_func)     

	fname = f"Tests/Mode {density}/Graph Test ({nfverts}, {density}, {limit}).txt"  
	print_mat(nfverts, mat, fname)


