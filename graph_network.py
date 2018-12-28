import networkx as nx
import matplotlib.pyplot as plt
g=nx.Graph()

filename="graph_modified.txt"

file1=open(filename,"r")



for line in file1:
	words=line.split()
	l1=[]
	for ele in words:
		int_ele=int(ele)
		l1.append(int_ele)
	t1=tuple(l1)
	l2=[t1]
	g.add_weighted_edges_from(l2)


'''
g.add_weighted_edges_from([(2,5,25)])   
g.add_weighted_edges_from([(1,2,0.125),(1,3,0.75),(2,4,1.2),(3,4,0.375)])
'''
nx.write_gml(g,"graph_main")
nx.draw(g)
plt.savefig("master_graph.png",dpi=2000)
plt.show()


print(g.number_of_nodes())
print(g.number_of_edges())
print(g.nodes())
print(g.edges())
