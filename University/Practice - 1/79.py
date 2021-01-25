graph = {
    'A' : ['B', 'C', 'E'],
    'B' : ['A', 'D', 'F'],
    'C' : ['G', 'A'],
    'D' : ['B'],
    'E' : ['F', 'A'],
    'F' : ['E', 'B'],
    'G' : ['C']
        }



def dfs(route, depth, goal, graph):
    if depth == 0:
        return
    if route[-1] == goal:
        return route
    for move in graph(route[-1]):
        if move not in route:
            next_route = dfs(route + [move], depth - 1)
            if next_route:
                return next_route

print(dfs('A', 2, 'D', graph))