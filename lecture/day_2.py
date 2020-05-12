print('day deux')

# mazes - depth first

# *explore*:
    #print this node
    # *explore* all of its unvisited neighbors
    # return 


def dft_recursive(self, start_vert, visited=None):
    print(start_vert)

    if visited is None:
        visited = set()
    
    visited.add(start_vert)

    for child_vert in self.vertices[start_vert]:
        if child_vert not in visited:
            self.dft_recursive(child_vert, visited)

def dfs_recursive(self, start_vert, target_value, visited=None, path=None):
    print(start_vert)

    if visited is None:
        visited = set()
    
    if path is None:
        path = []

    visited.add(start_vert)
    
    #make a copy
    path = path + [start_vert]

    # base case
    if start_vert == target == value:
        return path 

    for child_vert in self.vertices[start_vert]:
        if child_vert not in visited:
            new_path = self.dft_recursive(child_vert, target_value, visited, path)

            if new_path:
                return new_path


# how to solve any graph problem 

"""
1. Translate the problem into graph terminology
2. Build the graph 
3. Traverse it 

Word Ladders Problem 
--------------------

begin: hit 
end: cog 

hit -> hot -> cot -> cog

begin: sail
end: boat

sail -> s

begin: hungry
end: happy

None

On graph -> connect words that have one letter differenc

"""
# above

def find_ladders(begin_word, end_word):
    visited = set()
    q = Queue()

    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()

        v = path[-1]

        if v not in visited:
            visited.add(v)

            if v == end_word:
                return path

            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)

    
# read in all of the words into a list
with open('words.txt') as f:
    words = f.read().split()

word_set = set()

for w in words:
    word_set.add(w.lower())

letters = list(string.ascii_lowercase)

def get_neighbors(word):
    neighbors = []
    string_word = list(word) 

    for i in range(len(string_word)):
        for letter in letters:
            temp_word = list(string_word)
            temp_word[i] = letter

            w = "".join(temp_word)
            if w != and w in word_set:
                neighbors.append(w)