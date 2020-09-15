class Graph:
    def __init__(self):
        self.numberofnodes = 0
        self.adjacentlist = {}

    def addVertex(self,node):
        self.adjacentlist[node] = []
        self.numberofnodes += 1