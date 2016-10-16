#
# Testing for libgraph
# 

import graph
from node import Node

g = graph.Graph()

i = 0
while(i < 5):
    node = Node( str(i) )
    g.NodeList.append(node)
    i += 1
    
for node in g.NodeList:
    for n in g.NodeList:
        if(n.id == node.id ):
            continue
        
        if( int(node.id) + 1 == int(n.id) ):
            node.adyacentList.append( (n, -1) )
        elif( node.id == "4" and n.id == "1"):
            n.adyacentList.append( (node, -1) )
            node.adyacentList.append( (n, -1) )
    
for n in g.NodeList:
    n.Print()

origin = g.NodeList[0]
dest = "4"

rbfs = g.BFS(origin, dest)
rdfs = g.DFS(origin, dest)

print("BFS(0,4)", rbfs)
print("DFS:(0,4)", rdfs)