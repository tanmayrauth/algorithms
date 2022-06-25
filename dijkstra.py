from collections import defaultdict
import heapq as heap

def dijkstra(G, startingNode):
	visited = set()
	parentsMap = {}
	pq = []
	nodeCosts = defaultdict(lambda: float('inf'))
	nodeCosts[startingNode] = 0
	heap.heappush(pq, (0, startingNode))
 
	while pq:
		# go greedily by always extending the shorter cost nodes first
		_, node = heap.heappop(pq)
		visited.add(node)
 
		for adjNode, weight in G[node].items():
			if adjNode in visited:	continue
				
			newCost = nodeCosts[node] + weight
			if nodeCosts[adjNode] > newCost:
				parentsMap[adjNode] = node
				nodeCosts[adjNode] = newCost
				heap.heappush(pq, (newCost, adjNode))
        
	return parentsMap, nodeCosts


"""

Initialise dist to all vertex as Inf
Create PQ and push element 1-> (0,1)
While PQ is not empty:
    Pop min dist vertex(u) from PQ and add it to visited set
    Loop over adj nodes(v) of u and for each:
        If node(v) is already present in visisted set:
            skip

        If the distance from u to v< current distance:
            update the distance to v
            update parent of v as u
            push the v and its distance to PQ

"""    