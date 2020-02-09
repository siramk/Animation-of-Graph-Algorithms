import heapq
import matplotlib.pyplot as plt
import networkx as nx 
import matplotlib.patches as mpatches
from collections import defaultdict 
import time
import warnings
import sys

warnings.filterwarnings("ignore")

class graph:

    def __init__(self):
        self.adjMat=[]
        self.vertices=0
        self.g=defaultdict(list)

    def make_graph(self,option):
        if(option==1):
            fp=open("input_mst.txt","r")
            self.vertices=int(fp.readline())
            self.adjMat=[]
            for line in range(self.vertices):
                row=fp.readline()
                self.adjMat.append(list(map(int,row.split())))
        elif(option==2):
            self.vertices=int(input("Enter No.of vertices: "))
            self.adjMat=[]
            print("Enter the adjacency matrix with weights as the values in it(Enter 0 in A[i,j] if there is no edge beween i th and jth vertex )")
            for x in range(self.vertices):
                print("enter "+str(x+1)+"th row:")
                row=input()
                print("")
                self.adjMat.append(list(map(int,row.split())))
        
        graph=nx.Graph()
        # graph.add_nodes_from(range(self.vertices))
        for i in range(self.vertices):
            for j in range(self.vertices):
                if(self.adjMat[i][j]>0):
                    graph.add_edge(i,j,weight=self.adjMat[i][j])
                    self.g[i].append(j)
        # plt.ion()
        pos=nx.spring_layout(graph)
        nx.draw(graph,pos,with_labels=True,node_color='red')
        edge_cost=nx.get_edge_attributes(graph,'weight')
        nx.draw_networkx_edge_labels(graph,pos,edge_labels=edge_cost)
        blue_patch = mpatches.Patch(color='blue', label='Tree Edge') 
        plt.legend(handles=[blue_patch])
        return graph,pos

    def Binary_Search(self,arr,value,l,r):
        # print(value)
        # print(arr)
        
        mid=(l+r)//2
        # print("mid= ",mid)
        # print(arr[mid][0])
        if(arr[mid][0]==value):
            return arr[mid][1]
        elif(arr[mid][0]>value):
            # print("fuck")
            return (self.Binary_Search(arr,value,l,mid-1))
        elif(arr[mid][0]<value):
            return (self.Binary_Search(arr,value,mid+1,r))

        else: 
            return -1

    def draw_graph(self,parent,graph,pos,order_arr):

        order_arr.sort()
        prev=-1
        for i in range(self.vertices):
            
            j=self.Binary_Search(order_arr,i,0,self.vertices-1)
            if(parent[j]!=-1):
                if(prev==-1 or parent[j]==prev):
                    nx.draw_networkx_nodes(graph,pos,nodelist=[parent[j]],node_color='yellow')
                else:
                    nx.draw_networkx_nodes(graph,pos,nodelist=[parent[j],prev],node_color=['yellow','red'])
                    plt.pause(2)
                nx.draw_networkx_edges(graph, pos, edgelist = [(parent[j], j)], width = 4, alpha = 1, edge_color = 'blue')
                nx.draw_networkx_nodes(graph,pos,nodelist=[j,parent[j]],node_color=['yellow','red'])
                prev=j
                plt.pause(2)

        
        # print(parent)
        # print(order_arr)
    
    
    def mst_prims_util(self,v,graph,pos,key,parent,mst_set):

            key[v]=0
            key_pairs=[[key[v],v]]
            heapq.heapify(key_pairs)
            order_arr=[]
            nof_edges=0
            order=0
            while(nof_edges!=(self.vertices)): 
                # print(key_pairs)
                # time.sleep(1)
                active=heapq.heappop(key_pairs)
                active_node=active[1]

                # time.sleep(4)
                   
                

                if(mst_set[active_node]==True):
                    continue
                mst_set[active_node]=True
                nof_edges+=1
                order_arr.append([order,active_node])
                order+=1 
                for u in self.g[active_node]:
                    
                    if(key[u] >self.adjMat[active_node][u] and mst_set[u]==False):
                        key[u]=self.adjMat[active_node][u]
                        heapq.heappush(key_pairs,[key[u],u])
                        parent[u]=active_node
                        
            
            self.draw_graph(parent,graph,pos,order_arr)


    def mst_prims(self,graph,pos):
        key=[float('Inf') for x in range(self.vertices)]
        parent=[-1 for x in range(self.vertices)]
        mst_set=[False for x in range(self.vertices)]

        for  v in range(self.vertices): 
            if(mst_set[v]!=1):
                self.mst_prims_util(v,graph,pos,key,parent,mst_set)

        





#driving code
# print("!!Please mention the no.of vertices and the weight matrix in the file input_mst.txt and press any key after that to continue!!")
G=graph()
while(True):
    option=int(input("\nPlease select a option from the following options:\n1.) Default Graph\n2.) Enter a Graph\n3.)Exit\n\nEnter a option: "))
    if(option==3):
        break
    
    graph,pos=G.make_graph(option)
    G.mst_prims(graph,pos)
    plt.show()

print("\nThank You")