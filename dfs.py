import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import warnings

warnings.filterwarnings("ignore")


plt.show()

def find_index(value):
	global backTrack
	for x in range(len(backTrack)):
		if(backTrack[x]==value):
			return x
	return -2


def dfsUtil(Graph, v, parent, visited,pos,u): 
	visited[v] = 1
	global backTrack
	
	for i in Graph[v]:
		
		if visited[i] == 0:
			parent[i]=v
			

			change=find_index(-1)
			
			if(change!=-2):
				
				backTrack=[0 for x in range(len(Graph.nodes())) ]
				nx.draw_networkx_nodes(Graph,pos,nodelist=[v,change],node_color=["yellow","red"],alpha=1)
				plt.pause(1)

			nx.draw_networkx_edges(Graph, pos, edgelist = [(v,i)], width = 4, alpha = 1, edge_color = 'b',arrows=True)
			nx.draw_networkx_nodes(Graph,pos,nodelist=[i,v],node_color=["yellow","red"],alpha=1)
			plt.draw()
			plt.pause(1)
			dfsUtil(Graph, i, parent, visited,pos,v)
			
		elif(parent[v]!=i):
			
			
			nx.draw_networkx_edges(Graph, pos, edgelist = [(v,i)], width = 4, alpha = 1, edge_color = 'g',arrows=True)
			plt.draw()
			plt.pause(1)
	node_colors=["red" for i in range(len(Graph.nodes())) ]
	node_colors[v]="yellow"
	nodes_list=[i for i in range(len(Graph.nodes()))]
	nx.draw_networkx_nodes(Graph,pos,nodelist=nodes_list,node_color=node_colors,alpha=1)
	plt.pause(1)
	backTrack=[0 for x in range(len(Graph.nodes())) ]
	backTrack[v]=-1

def dfs(Graph, start): 
	# plt.ion()
	pos = nx.spring_layout(Graph)
	nx.draw(Graph, pos, with_labels = True,node_color='red')

	blue_patch = mpatches.Patch(color='blue', label='Tree Edge')    #for legend
	green_patch = mpatches.Patch(color='green', label='Back Edge')
	plt.legend(handles=[blue_patch,green_patch])
	visited = [0]*(len(Graph.nodes()))
	parent=[-1 for i in range(len(Graph.nodes())) ]
	stack =[ ] 
	stack.append(dfsUtil(Graph, start, parent, visited,pos,-1))
	for i in range(len(Graph.nodes())):
		if visited[i] == 0:
			
			stack.append(dfsUtil(Graph, i,parent,visited,pos,-1))
	return stack
			

backTrack=[] 

def makeGraph(option):
	global backTrack
	Graph = nx.Graph()
	if(option==1):
		f_in = open('input_dfs.txt')
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

	backTrack=[0 for j in range(len(Graph.nodes())) ] #for initialization
	return Graph,start

#driving code
while(True):
	option=int(input("\nPlease select a option from the following options:\n1.) Default Graph\n2.) Enter a Graph\n3.) Exit\n\nEnter a option: "))
	if(option==3):
		break
	Graph, start = makeGraph(option)
	dfs(Graph, start)
	plt.pause(1)

print("Thank You")
plt.show()


