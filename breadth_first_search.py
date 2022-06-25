def run( graph ):
    nodes  = graph.keys() 
    result = []
    queue  = []
    discovered = [ False for _ in range(len(nodes)+1) ]

    # This loop is needed for handling graph with multiple components
    for node in nodes:
        if not discovered[node]:
            discovered[node] = True
            queue.append(node)
            bfs( graph, result, discovered, queue )

    print(result)


def bfs( graph, result, discovered, queue ):
    
    while queue:
        node = queue.pop(0)
        result.append(node)

        for n in graph[node]:
            if not discovered[n]:
                queue.append(n)
                discovered[n] = True



if __name__ == '__main__':
    graph = { 1 : [2, 3],
              2 : [1, 5],
              3 : [5, 4, 1],
              4 : [3, 5],
              5 : [2, 3, 4]
            }
    run( graph )