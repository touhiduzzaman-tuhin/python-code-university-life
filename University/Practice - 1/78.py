Node = {
    'A' : ['B', 'C', 'E'],
    'B' : ['A', 'D', 'F'],
    'C' : ['G', 'A'],
    'D' : ['B'],
    'E' : ['F', 'A'],
    'F' : ['E', 'B'],
    'G' : ['C']
        }

def iddfs(root: Node, goal: str, maximum_depth: int = 10):

    for depth in range(0, maximum_depth):
        result = _dls([root], goal, depth)
        if result is None:
            continue
        return result

    raise ValueError('goal not in graph with depth {}'.format(maximum_depth))


def _dls(path: list, goal: str, depth: int):

    current = path[-1]
    if current.label == goal:
        return path
    if depth <= 0:
        return None
    for edge in current.children:
        new_path = list(path)
        new_path.append(edge.destination)
        result = _dls(new_path, goal, depth - 1)
        if result is not None:
            return result


iddfs('D', 'G')
