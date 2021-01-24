graph = {'Oradea': ['Zerind', 'Siblu'],
         'Zerind': ['Arad', 'Oradea'],
         'Arad': ['Siblu', 'Timisoara', 'Zerind'],
         'Timisoara': ['Lugoj', 'Arad'],
         'Lugoj': ['Mehedia', 'Timisoara'],
         'Mehedia': ['Lugoj', 'Dobreta'],
         'Dobreta': ['Mehedia', 'Cralova'],
         'Cralova': ['Dobreta', 'Pitesti', 'Rimnicu Vilcea'],
         'Pitesti': ['Bucharest', 'Rimnicu Vilcea', 'Cralova'],
         'Bucharest': ['Pitesti', 'Glurglu', 'Pagaras', 'Urziceni'],
         'Pagaras': ['Siblu', 'Bucharest'],
         'Siblu': ['Pagaras', 'Rimnicu Vilcea', 'Arad', 'Oradea'],
         'Rimnicu Vilcea': ['Pitesti', 'Siblu', 'Cralova'],
         'Urziceni': ['Bucharest', 'Vaslul', 'Hirsova'],
         'Neamt': ['Issl'],
         'Issl': ['Neamt', 'Vaslul'],
         'Vaslul': ['Issl', 'Urziceni'],
         'Hirsova': ['Urziceni', 'Etorie'],
         'Glurglu': ['Bucharest'],
         'Etorie': ['Hirsova']
}

queue = []

visited = []

def BFS(start, end):

    queue.append(start)

    while(len(queue) > 0):

        vertex = queue.pop()

        if vertex not in visited:

            visited.append(vertex)

            queue.extend(set(graph[vertex]) - set(visited))

        if visited.__contains__(end):

            break

    return visited

v = BFS('Arad', 'Pagaras')

print(v)