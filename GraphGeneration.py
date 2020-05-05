# Program to generate a test case for Prim's and Krukal's algorithms
# The graph generated will be connected.
from random import shuffle, sample, randint

# modify these two values for generating desired graph
nfverts = 200 # noof vertices
lim = 999 # maximum edge weight
rint = lambda: randint(1, lim)

def print_mat(mat):
	# Printing the test case
	print(nfverts)
	for i in mat[1:]:
		for j in i[1:]:
			print("{:02d}".format(j), end = " ")
		print()

def generate_random_spanning_tree(mat):
	mylist = list(range(1, nfverts + 1))
	shuffle(mylist)
	visited = [mylist[0]]
	for v in mylist[1:]:
		u = sample(visited, 1)[0] # sample function returns a list
		mat[u][v] = rint()
		mat[v][u] = mat[u][v]
		visited += [v]

# random_weight is 0 three out of five times 
# and it is a random int two out of five times
random_weight = lambda: [rint(), rint(), rint(), rint(), rint()][randint(0, 4)]

def add_some_more_edges(mat):
	for i in range(1, nfverts + 1 - 1):
		for j in range(i + 1, nfverts + 1):
			if not mat[i][j]:
				mat[i][j] = random_weight()
				mat[j][i] = mat[i][j]
				
mat = [[0 for i in range(nfverts + 1)] \
          for j in range(nfverts + 1)]

generate_random_spanning_tree(mat)
add_some_more_edges(mat)       
print_mat(mat)
	

