from util import Queue

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # first, you should check if both v1 and v2 are in the graph
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        
        else:
            raise ValueError("Vertex does not exist")


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # if vertex_id
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("Vertex does not exist")

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # similar to bft, but must use paths
        #Create a queue
        q = Queue()
        visited = set()
        q.enqueue([starting_vertex])
     
        while q.size() > 0:
            #Dequeue the first path, and then grab the vertext from the end of the path in order to check for it in the set
            path = q.dequeue()
            last_vertex = path[-1]
            #check if it's been visited
            if last_vertex not in visited:
                #add to it
                visited.add(last_vertex)

                if last_vertex == destination_vertex:
                    return path

                # add a path to vertex neighbors
                for neighbor in self.get_neighbors(last_vertex):
                    #make a copy of the path
                    path_copy = path.copy()
                    #append neighbors to new path + enqueue 
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)
        