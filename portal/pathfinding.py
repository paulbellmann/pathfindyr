import xmltodict

def dijkstra(graph, start, end):
    """Main function that calculates the shortest path

    Args:
        graph (dict): Graph network - example: {id1: {edge3: dist}, id2: {edge8: dist, edge6: dist }, ...}.
        start (int): Id from the start node.
        end (int): Id from the end node.

    Returns:
        Shortes path as an array (if possible).
    """

    shortest_dist = {}
    queque = {}
    unvisited = graph
    infinity = 9999999
    path = []

    # set all the nodes to infinity except the start
    for node in unvisited:
        shortest_dist[node] = infinity
    shortest_dist[start] = 0
 
    # loop through all the nodes
    while unvisited:
        min_node = None
        for node in unvisited:
            if min_node is None:
                min_node = node
            elif shortest_dist[node] < shortest_dist[min_node]:
                min_node = node

        # loop through all the neighbours in current node
        for child_node, weight in graph[min_node].items():
            if weight + shortest_dist[min_node] < shortest_dist[child_node]:
                shortest_dist[child_node] = weight + shortest_dist[min_node]
                queque[child_node] = min_node

        # remove node from unvisited graph
        unvisited.pop(min_node)
 
    curr_node = end
    while curr_node != start:
        try:
            path.insert(0, curr_node)
            curr_node = queque[curr_node]
        except KeyError:
            return 'Path not reachable'
            break
    path.insert(0,start)
    if shortest_dist[end] != infinity:
        return path


def grab_data(file):
    """Helper function that gets the data from an XML file.

    Args:
        file (str): Path to file - example: 'my_great_file.xml'

    Returns:
        The graph needed for the dijkstra function, and a helper graph that contains
        additional information (lat, lng, name)
    """


    with open(file) as fd:
        data = xmltodict.parse(fd.read())

    graph = {}
    graph_helper = {}

    # read data from xml and save it in a dictionary
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