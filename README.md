# Animation-of-Graph-Algorithms

### Dependencies of this project are:
1.)python 3(This code is tested on python 3.6.8)
2.)networkx
3.)matplotlib

### command to install dependencies of networkx:
pip3 install networkx[all]


## Readme for BFS(Breadth First Search)

There is already one default graph, but if user want to give a new graph then user should follow the below steps:
 
### The user should mention the following things when prompted to enter .
1.)no.of vertices
2.)adjacency matrix
3.)start vertex


and then run the program with pyhton3 bfs.py

#### NOTE: A default graph is already placed in input_bfs.txt

### Example of input:
4        ------->no.of vertices
0 1 1 1
0 0 1 0  ------->adjacency matrix
0 1 0 0
0 0 1 0
0        ------->start vertex


## Readme for DFS(Depth For Search)

There is already one default graph, but if user want to give a new graph then user should follow the below steps:
 
The user should mention the following things when prompted to enter .
1.)no.of vertices
2.)adjacency matrix
3.)start vertex

and then run the program with pyhton3 dfs.py

#### NOTE: A default graph is already placed in input_dfs.txt

### Example of input:
5          ------->no.of vertices
0 1 1 0 0
1 0 1 0 0  
1 1 0 1 1  ------->adjacency matrix
0 0 1 0 1
0 0 1 1 0
2          ------->start vertex


## Readme for Prims algorithm

There is already one default graph, but if user want to give a new graph then user should follow the below steps:

The user should mention the following things in the input.txt file available in the current directory.
1.)no.of vertices
2.)adjacency matrix with cost of edges


and then run the program with pyhton3 min_span_tree.py

#### NOTE: A default graph is already placed in input_mst.txt

#### Example of input:
5         --------->no.of vertices
0 2 7 0 0
2 0 3 8 5
7 3 0 1 0 --------->adjacency matrix
0 8 1 0 4
0 5 0 4 0
