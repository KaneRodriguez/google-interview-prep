class GraphAdjList:
	def __init__(self, nodes = []):
		self.nodes = nodes

class NodeAdjList:
	def __init__(self, val, adj = []):
		self.adj = adj
		self.val = val
		self.visited = False
