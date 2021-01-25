from collections import defaultdict

class Graph:

    def __init__(self, vertex):

        self.v = vertex

        self.graph = defaultdict(list)


    def addEdge(self, u, v):

        self.graph[u].append(v)

    def DLS(self, src, target, maxDepth):

        if src == target:

            return True

        if maxDepth <= 0:

            return False

        for i in self.graph[src]:
            if(self.DLS(i, target, maxDepth - 1)):
                return True
        return False

g = Graph(7);
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)

target = 5;
maxDepth = 1;
src = 0

if(g.DLS(src, target, maxDepth)) == True:

    print("Target is Reachable from Source"+"With in Max Depth")

else:
    print("Target Not is Reachable from Source" + "With in Max Depth")