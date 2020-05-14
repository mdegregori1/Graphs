# essentially, looking for the longest path possible between starting_node and ancestors
from graph import Graph 
from util import Queue

def earliest_ancestor(ancestors, starting_node, parents=False):
    # must keep track of node and its ancestor, call in queue and graph
    # after, must create graph -> loop through passed in ancestors, and if not already there, add both vertices and an edge between them
    # add add the inputed starting node into the queue to initiate loop
    # while loop
    # dequeue, and then grab grab the last thing in the value passed into queue, in this case, the child
        # if the child is not the same as passed in starting node
            # if the len of that path > the initialized val of depth for zero, then set the ancestor to current_node, and set the ancestor to updated len path
    

    current_depth = 0
    earliest_ancestor = -1
    graph = Graph()
    q = Queue()

    for parent, child in ancestors:
        if parent not in graph.vertices:
            graph.add_vertex(parent)
        if child not in graph.vertices:
            graph.add_vertex(child)
         
        graph.add_edge(child,parent)


    q.enqueue([starting_node])
    while q.size() > 0:
        path = q.dequeue()
        current_node = path[-1]
        if current_node != starting_node:
            if len(path) > current_depth:
                earliest_ancestor = current_node
                current_depth = len(path)
            elif len(path) == current_depth and earliest_ancestor > current_node:
                earliest_ancestor = current_node

        # create copyied path, and append the val of current node to it
        for neighbor in graph.get_neighbors(current_node):
            path_copy = path.copy()
            path_copy.append(neighbor)
            q.enqueue(path_copy)
        

    return earliest_ancestor



       










test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),(4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 10), "== -1")