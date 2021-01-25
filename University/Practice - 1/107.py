graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}


path = []

visited = []

def DFS(start, end, graph):

    path.append(start)

    visited.append(start)

    return DFS_(start, end, graph)

def DFS_(start, end, graph):

    for node in graph[path[len(path) - 1]]:
        if node not in visited:
            visited.append(node)

        else:
            continue
        path.append(node)

        if node == end:
            return path
        return DFS_(start, end, graph)




print(DFS('A', 'D', graph))

path = []

visited = []