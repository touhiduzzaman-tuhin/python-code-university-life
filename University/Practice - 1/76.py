graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

path = []

visited = []

def find_path(statt, end, graph):

    path.append(statt)

    visited.append(statt)

    return find_path_(statt, end, graph)

def find_path_(statt, end, graph):

    for node in graph[path[len(path) -1]]:

        if node not in visited:
            visited.append(node)

        else:

            continue
        path.append(node)

        if node == end:

            return path
        return find_path_(statt,end,graph)

print(find_path('A', 'D', graph))

path = []

visited = []