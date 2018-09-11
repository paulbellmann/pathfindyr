import xmltodict

def grab_data(file):
    with open(file) as fd:
        data = xmltodict.parse(fd.read())

    graph = {}
    graph_helper = {}

    # prep data
    for each in data["nodes"]["node"]:
        graph[int(each["@id"])] = {}
        graph_helper[int(each["@id"])] = {}
        graph_helper[int(each["@id"])]["name"] = each["@name"]
        graph_helper[int(each["@id"])]["lng"] = each["coordinates"]["longitude"]
        graph_helper[int(each["@id"])]["lat"] = each["coordinates"]["latitude"]
        graph_helper[int(each["@id"])]["id"] = int(each["@id"])

        for miau in each["edges"]["edge"]:
            graph[int(each["@id"])][int(miau["@to"])] = int(miau["@distance"])

    return graph, graph_helper

def dijkstra(graph, start, end):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
 
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
 
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
 
    currentNode = end
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    if shortest_distance[end] != infinity:
        # print('Shortest distance is ' + str(shortest_distance[end]))
        # print('And the path is ' + str(path))
        return path