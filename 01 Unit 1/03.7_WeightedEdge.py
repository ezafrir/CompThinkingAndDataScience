# Write a WeightedEdge class that extends Edge. Its constructor requires a weight parameter, 
# as well as the parameters from Edge. You should additionally include a getWeight method. 
# The string value of a WeightedEdge from node A to B with a weight of 3 should be "A->B (3)".

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        pass
    def getWeight(self):
        pass
    def __str__(self):
        pass
class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.src) + "->" + str(self.dest) + " (" + str(self.weight) + ")"
