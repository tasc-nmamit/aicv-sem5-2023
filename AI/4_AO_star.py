# Define a class named Graph to implement the AO* algorithm.
class Graph:
    # Initialize the graph with input parameters.
    def __init__(self, graph, heuristicNodeList, startNode):
        self.graph = graph
        self.H = heuristicNodeList
        self.start = startNode
        self.parent = {}         # Dictionary to store parent nodes.
        self.status = {}         # Dictionary to store status of nodes.
        self.solutionGraph = {}  # Dictionary to store the final solution path.

    # Method to start the AO* algorithm.
    def applyAOstar(self):
        self.aoStar(self.start, False)

    # Method to retrieve neighbors of a node 'v'.
    def getNeighbors(self, v):
        return self.graph.get(v, [])  # Returns an empty list if the node has no neighbors.

    # Method to get the status of a node 'v'.
    def getStatus(self, v):
        return self.status.get(v, 0)

    # Method to set the status of a node 'v'.
    def setStatus(self, v, val):
        self.status[v] = val

    # Method to get the heuristic value of a node 'n'.ss
    def getHeuristicNodeValue(self, n):
        return self.H.get(n, 0)

    # Method to set the heuristic value of a node 'n'.
    def setHeuristicNodeValue(self, n, value):
        self.H[n] = value

    # Method to print the final solution.
    def printSolution(self):
        print("For Graph Solution, Traverse the graph from the start node:")
        print("------------------------------------------------------------")
        print(self.solutionGraph)
        print("------------------------------------------------------------")

    # Method to compute the minimum cost child node of a given node 'v'.
    def computeMinimumCostChildNode(self, v):
        minimumCost = float('inf')
        costToChildNodeListDicts = {}
        costToChildNodeListDicts[minimumCost] = []
        flag = True
        for nodeInfoTupleList in self.getNeighbors(v):
            cost = 0
            nodeList = []
            for c, weight in nodeInfoTupleList:
                cost = cost + self.getHeuristicNodeValue(c) + weight
                nodeList.append(c)
            if flag:
                minimumCost = cost
                costToChildNodeListDicts[minimumCost] = nodeList
                flag = False
            else:
                if minimumCost > cost:
                    minimumCost = cost
                    costToChildNodeListDicts[minimumCost] = nodeList
        return minimumCost, costToChildNodeListDicts[minimumCost]

    # Recursive AO* algorithm.
    def aoStar(self, v, backTracking):
        print("HEURISTIC VALUES: ", self.H)
        print("SOLUTION GRAPH: ", self.solutionGraph)
        print("PROCESSING NODE: ", v)
        print("------------------------------------------------------------")
        if self.getStatus(v) >= 0:
            minimumCost, childNodeList = self.computeMinimumCostChildNode(v)
            print(minimumCost, childNodeList)
            self.setHeuristicNodeValue(v, minimumCost)
            self.setStatus(v, len(childNodeList))
            solved = True
            for childNode in childNodeList:
                self.parent[childNode] = v
                if self.getStatus(childNode) != -1:
                    solved = solved & False
            if solved:
                self.setStatus(v, -1)
                self.solutionGraph[v] = childNodeList
            if v != self.start:
                self.aoStar(self.parent[v], True)
            if not backTracking:
                for childNode in childNodeList:
                    self.setStatus(childNode, 0)
                    self.aoStar(childNode, False)

# Create a sample graph as a dictionary of nodes and their neighbors with associated weights.
graph_data = {
    'A': [[('B', 1), ('C', 1)],[('D',1)]],
    'B': [[('G', 1)],[('H',1)]],
    'C': [[('J', 1)]],
    'D': [[('E',1),('F',1)]],
    'G': [[('I',1)]]
}

# Initialize the heuristic values, start node, and create a Graph instance.
heuristic_node_list = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F':1, 'G':5, 'H':7, 'I':7,'J':1}
start_node = 'A'
graph = Graph(graph_data, heuristic_node_list, start_node)

# Apply the AO* algorithm to find the solution.
graph.applyAOstar()

# Print the solution graph.
graph.printSolution()
