graph = {

    'A': ['B','C'],
    'B': ['C','D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C'],

}

queue = []

visited = []

def BFS(start, end):

    queue.append(start)

    while(len(queue) > 0):

        vertex = queue.pop(0)

        if vertex not in visited:

            visited.append(vertex)

            queue.extend(set(graph[vertex]) - set(visited))

        if visited.__contains__(end):

            break

    return visited

v = BFS('A', 'D')

print(v)
