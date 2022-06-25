def run( graph ):
    nodes = graph.keys()
    discovered = [ False for _ in range(len(nodes)+1) ]
    result = []

    for node in nodes:
        if not discovered[node]:
            discovered[node] = True
            dfs(node, result, discovered, graph)

    print(result)


def dfs( node, result, discovered, graph ):
    discovered[node] = True 
    
    for n in graph[node]:
        if not discovered[n]:
            dfs( n, result, discovered, graph)

    result.append(node) # Backtracking and storing result
 

if __name__ == '__main__':
    graph = { 1 : [2, 3],
              2 : [1, 5],
              3 : [5, 4, 1],
              4 : [3, 5],
              5 : [2, 3, 4]
            }
    run( graph )
