
# Note: This Queue class is sub-optimal. Why?
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)



# tough because a sum of all that we've been doing, basically

# consist of nodes and edges
# kind of like binary search trees (type of graph), but can really point to any direction

# undirected vs directed eges -> relationship is mutual
# directional -> connection on linkedin
# undirected -> followers on twitter
# cyclic -> can get back to original node (can be directional or undirected)
# dense/sparse -> dense = most verticies connected ex(flight maps), sparse = less connections ex(subway map), a few
# Weighted graphs -> has edge weights
#directed acyclic graphs -> binary search tree starts from one node, type of dag -> no cycles, directed

# adjacency matrix, graph, adjacency list (most used at lambda)
# get all edges, add edge, add vertex, remove vertex, etc
# adjacency list uses sets => set only has keys, unique, unordered, 

# any graph with a bidirectional edge is a cyclic graph


# representing graphs
# adjacency list and adjacency matrix
# list, below 

# class GraphNode:
#     def __init__(self, value):
#         self.value = value
#         self.edges = [] 

# above, gives you references 
# no edge weight yet

class Graph: 
    
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set() # set of edges
    
    def add_edge(self, v1, v2):
        """Add edge from v1 to v2."""
        # make sure they're in the graph 
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph! ")

    
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        q = Queue()
        q.enqueue(starting_vertex_id)
        # visited
        visited = set()
        # repeat until queue is empty
        while q.size() > 0:
            v = q.dequeue()
            # if it's not visited:
            if v not in visited:
                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)


g = Graph()
g.add_vertex(99)
g.add_vertex(3)
g.add_edge(99,3) # connect the two 
g.add_edge(3, 99) # connect node 3 to node 99

g.bft(99)
print(g.get_neighbors(99))

# how to traverse?

# BREADTH FIRST
# Queue (first in first out): G A F E 
    # while queue isn't empty:
        # dequeue the first first
        # if that vert isn't visited:
            # mark as visited
            # add its unvisited neighbors to the queue
# Add starting node to Queue
# Visited: C B

# Looks like with breadth-first QUEUE, we must visit all of connections first before moving on

# seems to afect the order that you move into visited
# BREADTH FIRST 


# DEPTH-FIRST
# Stack
# Visited

 # while stack isn't empty:
    # pop the first vert
    # if that vert isn't visited:
        # mark as visited
        # push all of unvisited neighbors to stack