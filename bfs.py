import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import warnings

warnings.filterwarnings("ignore")
 
def find_index(value):
	global backTrack
	for x in range(len(backTrack)):
		if(backTrack[x]==value):
			return x
	return -2

def bfs_traversal(Graph, start): 
	pos = nx.spring_layout(Graph)
	nx.draw(Graph, pos, with_labels = True,node_color='red')  

	blue_patch = mpatches.Patch(color='blue', label='Tree Edge') #for legend
	plt.legend(handles=[blue_patch])

	global backTrack
	visited = [0]*(len(Graph.nodes()))
	trackNodes = []		
	trackNodes.append(start)
	visited[start] = 1
	while trackNodes:
		activeNode = trackNodes.pop(0)
		for i in Graph[activeNode]:  
				
			nx.draw_networkx_nodes(Graph,pos,nodelist=[activeNode],node_color=["yellow"],alpha=1)
			plt.pause(1)


			if visited[i] == 0:
				trackNodes.append(i)
				visited[i] = 1
				nx.draw_networkx_edges(Graph, pos, edgelist = [(activeNode,i)], width = 4, alpha = 1, edge_color = 'blue')
				plt.draw()
				plt.pause(1)
		node_colors=["red" for i in range(len(Graph.nodes())) ]
		nodes_list=[i for i in range(len(Graph.nodes()))]
		nx.draw_networkx_nodes(Graph,pos,nodelist=nodes_list,node_color=node_colors,alpha=1)
		plt.pause(1)
		
	return

backTrack=[]


def makeGraph(option):
	Graph = nx.Graph()
	if(option==1):
		f_in = open('input_bfs.txt')
		n = int(f_in.readline())
		adjMat = []
		for i in range(n):
			line = list(map(int,(f_in.readline()).split()))
			adjMat.append(line)
		start = int(f_in.readline())  
		for i in range(n):
			for j in range(n):
				if adjMat[i][j] > 0:
						Graph.add_edge(i, j) 
	elif(option==2):
		n=int(input("Enter No.of vertices: "))
		adjMat=[]
		print("\nEnter the Adjacency Matrix")
		for x in range(n):
			print("enter "+str(x+1)+"th row:")
			row=input()
			print("")
			adjMat.append(list(map(int,row.split())))
		start=int(input("Enter the start vertex:"))
		for i in range(n):
			for j in range(n):
				if adjMat[i][j] > 0:
						Graph.add_edge(i, j)
	
	global backTrack
	backTrack=[0 for x in range(len(Graph.nodes()))]
	return Graph, start





#driving code
while(True):
	option=int(input("\nPlease select a option from the following options:\n1.) Default Graph\n2.) Enter a Graph\n3.) Exit\n\nEnter a option: "))
	if(option==3):
		break
	Graph, start = makeGraph(option)
	bfs_traversal(Graph, start)
	plt.pause(1)

print("Thank You")
plt.show()


