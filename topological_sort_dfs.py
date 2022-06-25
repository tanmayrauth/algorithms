 
class DirectedGraph:
    def __init__(self, no_of_nodes):
        self.graph       = dict()
        self.no_of_nodes = no_of_nodes
        
    def addEdge(self, u, v):
        if self.graph.get(u, None):
            self.graph[u].append(v) 
        else:
            self.graph[u] = [v]
 
    def topological_sort_util(self, node, discovered, stack):
        discovered[node] = True

        for n in self.graph.get(node, []):
            if not discovered[n]:
                self.topological_sort_util(n, discovered, stack)

        stack.append(node)

    def topological_sort(self): 
        discovered = [False] * self.no_of_nodes
        stack = []

        for node in self.graph:
            if not discovered[node]:
                self.topological_sort_util(node, discovered, stack)

        return stack[::-1]


if __name__ == '__main__':
    dg = DirectedGraph(6)
    dg.addEdge(5, 2)
    dg.addEdge(5, 0)
    dg.addEdge(4, 0)
    dg.addEdge(4, 1)
    dg.addEdge(2, 3)
    dg.addEdge(3, 1)

    print(dg.topological_sort())
