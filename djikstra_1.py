graph = {
            'A': {'B':1 , 'E':3 },
            'B': {'C':3 , 'D':1},
            'C': {},
            'D': {'C':1},
            'E': {'D':1}
}

def find_shortest(graph):
    unseen_nodes = graph.keys()
    dist = {}
    predec = {}
    source = 'A'
    #initialize the dist for each node as unreachable "-1" and predec as None
    for node in unseen_nodes:
        dist[node] = 999999999
        predec[node] = None

    dist[source] = 0
    predec[source] = None
    #iterate until all nodes are seen
    while unseen_nodes:
        #get minnode first ie. an unseen node that is closest to source
        min_node = None
        for node in unseen_nodes:
            if min_node == None:
                min_node = node
            elif dist[min_node] > dist[node]:
                min_node = node

        #if none found then our graph has converged
        if min_node == None:
            break
        else:
            unseen_nodes.remove(min_node)

        #finally, once you have min node calcualte the distance of its neighbors
        #minimum distance to that neighbor so far
        for neighbor , distance in graph[min_node].items():
            if dist[neighbor] == 999999999 or dist[neighbor] > dist[min_node] + distance:
                dist[neighbor] = dist[min_node] + distance
                predec[neighbor] = min_node

    return dist , predec

print find_shortest(graph)